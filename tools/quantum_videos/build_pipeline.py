"""End-to-end build pipeline for voiced Manim Quantum Information videos."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import tempfile
import wave

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[2]
ANIMA_PYTHON = Path("~/Code/Projects/anima/.venv/bin/python").expanduser()
MANIM_PROJECT = Path("~/Code/Skills/learning/tools/manim-learning-video").expanduser()
MANIM_PYTHON = MANIM_PROJECT / ".venv" / "bin" / "python"
MANIM_SRC = MANIM_PROJECT / "src"
OUTPUT_DIR = REPO_ROOT / "quarto" / "assets" / "videos"
CACHE_DIR = REPO_ROOT / "quarto" / "assets" / "videos" / ".tts_cache"

QUALITIES = {
    "preview": (960, 540, 15),
    "medium": (1280, 720, 30),
    "high": (1920, 1080, 30),
}


def clock_vtt(seconds: float) -> str:
    millis = round(seconds * 1000)
    hours, rem = divmod(millis, 3_600_000)
    minutes, rem = divmod(rem, 60_000)
    secs, ms = divmod(rem, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}.{ms:03d}"


def read_wav_float32(path: Path) -> tuple[np.ndarray, int]:
    with wave.open(str(path), "rb") as w:
        sr = w.getframerate()
        n = w.getnframes()
        raw = w.readframes(n)
    arr = np.frombuffer(raw, dtype="<i2").astype(np.float32) / 32767.0
    return arr, sr


def write_wav_float32(path: Path, audio: np.ndarray, sr: int = 48000) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pcm = (np.clip(audio, -1.0, 1.0) * 32767.0).astype("<i2").tobytes()
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(pcm)


def polish_voice_clip(audio: np.ndarray, sr: int = 48000) -> np.ndarray:
    """Trim excess leading/trailing silence, apply 25ms cosine fade, and normalize RMS."""
    if len(audio) == 0:
        return audio
    # Compute short-time envelope (10ms window)
    win = max(1, int(sr * 0.01))
    env = np.sqrt(np.convolve(audio**2, np.ones(win) / win, mode="same"))
    active = np.where(env > 0.006)[0]
    if len(active) > 0:
        pad_head = int(sr * 0.05)
        pad_tail = int(sr * 0.08)
        start = max(0, int(active[0]) - pad_head)
        end = min(len(audio), int(active[-1]) + pad_tail)
        audio = audio[start:end].copy()

    # Cosine fade-in / fade-out (25 ms)
    fade_len = min(int(sr * 0.025), len(audio) // 4)
    if fade_len > 1:
        t = np.linspace(0, math.pi, fade_len, dtype=np.float32)
        fade_in = 0.5 * (1.0 - np.cos(t))
        fade_out = fade_in[::-1]
        audio[:fade_len] *= fade_in
        audio[-fade_len:] *= fade_out

    # Normalize RMS to target ~0.13 (-17.7 dBFS) with soft limiting at 0.92
    rms = float(np.sqrt(np.mean(audio**2)) + 1e-8)
    gain = min(3.5, 0.135 / rms)
    audio = audio * gain
    peak = float(np.max(np.abs(audio)) + 1e-8)
    if peak > 0.92:
        audio = audio * (0.92 / peak)
    return audio.astype(np.float32)


def make_chapter_chime(sr: int = 48000, duration: float = 0.65) -> np.ndarray:
    """Subtle, warm 2-note harmonic chime for chapter transitions."""
    t = np.linspace(0, duration, int(sr * duration), endpoint=False, dtype=np.float32)
    f1, f2 = 523.25, 783.99  # C5 + G5 gentle fifth
    env = np.exp(-5.5 * t) * np.minimum(1.0, t / 0.015)
    wave_sig = (
        0.032
        * env
        * (0.65 * np.sin(2 * math.pi * f1 * t) + 0.35 * np.sin(2 * math.pi * f2 * t))
    )
    return wave_sig.astype(np.float32)


TTS_WORKER_CODE = r"""
import json, sys, wave, hashlib
from pathlib import Path
import numpy as np
from mlx_audio.tts.utils import load_model

manifest_path = Path(sys.argv[1])
cache_dir = Path(sys.argv[2])
cache_dir.mkdir(parents=True, exist_ok=True)
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

model_dir = Path("~/AIData/models/anima/speech/Irodori-TTS-v4.1-Small-MF-fp16").expanduser()
model = load_model(model_dir)
sr = model.sample_rate

def save_raw_wav(path, audio):
    pcm = (np.clip(audio, -1.0, 1.0) * 32767.0).astype("<i2").tobytes()
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(pcm)

# Ensure consistent narrator reference clip exists
ref_wav = cache_dir / "narrator_ref_v1.wav"
if not ref_wav.is_file():
    ref_caption = "20代前半の女性、透明感のある落ち着いた優しい声。科学番組のナレーターのように、聞き取りやすく明瞭で、親しみやすく話す。"
    ref_text = "みなさん、こんにちは。前回のゼミでは、量子回路の基本的な読み方と、ゲートが状態ベクトルをどう変えるかを一緒に学びましたね。"
    chunks = []
    for res in model.generate(text=ref_text, ref_audio=None, caption=ref_caption, rng_seed=101):
        chunks.append(np.asarray(res.audio, dtype=np.float32))
    save_raw_wav(ref_wav, np.concatenate(chunks))

delivery_caption = "落ち着いた優しい声で、聞き取りやすく明瞭に説明する。"
for item in manifest["cues"]:
    tts_text = item["tts"]
    h = hashlib.sha256(tts_text.encode("utf-8")).hexdigest()[:16]
    raw_out = cache_dir / f"raw_{item['id']}_{h}.wav"
    if not raw_out.is_file():
        chunks = []
        for res in model.generate(text=tts_text, ref_audio=str(ref_wav), caption=delivery_caption, rng_seed=101):
            chunks.append(np.asarray(res.audio, dtype=np.float32))
        save_raw_wav(raw_out, np.concatenate(chunks))
        print(f"  [TTS] Synthesized {item['id']}: {tts_text[:34]}...", flush=True)
"""


def synthesize_and_verify_cues(
    lesson_id: str, cues_spec: list[dict], verify_asr: bool = True
) -> Path:
    """Synthesize all cues via Irodori-TTS, polish audio, verify with Whisper, and write timing JSON."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    manifest_path = CACHE_DIR / f"{lesson_id}_tts_request.json"
    manifest_path.write_text(
        json.dumps({"cues": cues_spec}, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    subprocess.run(
        [str(ANIMA_PYTHON), "-c", TTS_WORKER_CODE, str(manifest_path), str(CACHE_DIR)],
        check=True,
    )

    timed_cues = []
    for item in cues_spec:
        tts_text = item["tts"]
        h = hashlib.sha256(tts_text.encode("utf-8")).hexdigest()[:16]
        raw_wav = CACHE_DIR / f"raw_{item['id']}_{h}.wav"
        polished_wav = CACHE_DIR / f"polished_{item['id']}_{h}.wav"
        asr_cache = CACHE_DIR / f"asr_{item['id']}_{h}.txt"

        if not polished_wav.is_file():
            arr, sr = read_wav_float32(raw_wav)
            arr_clean = polish_voice_clip(arr, sr)
            write_wav_float32(polished_wav, arr_clean, sr)
        else:
            arr_clean, sr = read_wav_float32(polished_wav)

        dur = round(len(arr_clean) / float(sr), 3)

        asr_text = ""
        if verify_asr:
            if asr_cache.is_file():
                asr_text = asr_cache.read_text(encoding="utf-8").strip()
            else:
                try:
                    res = subprocess.run(
                        [
                            "curl",
                            "-s",
                            "http://127.0.0.1:8001/v1/audio/transcriptions",
                            "-F",
                            f"file=@{polished_wav}",
                            "-F",
                            "model=mlx-community--whisper-large-v3-turbo-asr-fp16",
                        ],
                        capture_output=True,
                        text=True,
                        timeout=15,
                        check=False,
                    )
                    if res.returncode == 0 and res.stdout.strip():
                        asr_text = json.loads(res.stdout).get("text", "").strip()
                        asr_cache.write_text(asr_text, encoding="utf-8")
                except Exception:
                    pass

        timed_cues.append(
            {
                "id": item["id"],
                "display": item["display"],
                "tts": tts_text,
                "asr": asr_text,
                "wav": str(polished_wav),
                "duration": dur,
            }
        )

    timing_json_path = CACHE_DIR / f"{lesson_id}_timing.json"
    timing_json_path.write_text(
        json.dumps(
            {"lesson_id": lesson_id, "cues": timed_cues}, ensure_ascii=False, indent=2
        ),
        encoding="utf-8",
    )
    return timing_json_path


def probe_media(path: Path) -> dict:
    res = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "stream=codec_type,codec_name,width,height,avg_frame_rate,sample_rate:format=duration",
            "-of",
            "json",
            str(path),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    data = json.loads(res.stdout)
    streams = data.get("streams", [])
    v_stream = next((s for s in streams if s.get("codec_type") == "video"), None)
    a_stream = next((s for s in streams if s.get("codec_type") == "audio"), None)
    if not v_stream:
        raise RuntimeError(f"No video stream in {path}")
    return {
        "duration": round(float(data["format"]["duration"]), 3),
        "width": int(v_stream["width"]),
        "height": int(v_stream["height"]),
        "fps": float(Fraction(v_stream["avg_frame_rate"])),
        "has_audio": a_stream is not None,
        "audio_sr": int(a_stream["sample_rate"])
        if a_stream and "sample_rate" in a_stream
        else 0,
    }


def build_voiced_lesson(
    lesson_id: str,
    title: str,
    description: str,
    domain: str,
    source_py: Path,
    scene_class: str,
    cues_spec: list[dict],
    quality: str = "high",
) -> Path:
    """Full pipeline: TTS -> Manim -> Master 48kHz Audio -> FFmpeg MP4 + VTT + Poster."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(
        f"\n=== [1/4] Synthesizing & Verifying 48kHz Local TTS for {lesson_id} ===",
        flush=True,
    )
    timing_json_path = synthesize_and_verify_cues(lesson_id, cues_spec, verify_asr=True)
    timing_data = json.loads(timing_json_path.read_text(encoding="utf-8"))
    cue_map = {c["id"]: c for c in timing_data["cues"]}

    for c in timing_data["cues"]:
        print(
            f"  Cue {c['id']:6s} ({c['duration']:4.2f}s) | ASR: {c['asr']}", flush=True
        )

    width, height, fps = QUALITIES[quality]
    print(
        f"\n=== [2/4] Rendering Manim Scene {scene_class} ({width}x{height} @ {fps}fps) ===",
        flush=True,
    )

    cache_path = CACHE_DIR / "manim_cache" / f"{lesson_id}-{width}x{height}-{fps}fps"
    cache_path.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix=f"{lesson_id}_") as tmp_dir:
        tmp = Path(tmp_dir)
        raw_movie = tmp / "raw.mp4"
        raw_meta = tmp / "scene.json"

        env = os.environ.copy()
        py_paths = [str(REPO_ROOT / "tools"), str(MANIM_SRC)]
        if env.get("PYTHONPATH"):
            py_paths.append(env["PYTHONPATH"])
        env["PYTHONPATH"] = os.pathsep.join(py_paths)
        env["QUANTUM_VIDEO_TIMING_JSON"] = str(timing_json_path)

        cmd = [
            str(MANIM_PYTHON),
            "-m",
            "learning_video.worker",
            "--source",
            str(source_py.resolve()),
            "--scene",
            scene_class,
            "--id",
            lesson_id,
            "--cache",
            str(cache_path),
            "--movie",
            str(raw_movie),
            "--metadata",
            str(raw_meta),
            "--width",
            str(width),
            "--height",
            str(height),
            "--fps",
            str(fps),
        ]
        subprocess.run(cmd, env=env, check=True)

        scene_meta = json.loads(raw_meta.read_text(encoding="utf-8"))
        total_dur = float(scene_meta["scene_duration"])
        print(f"  Manim render complete: duration = {total_dur:.2f}s", flush=True)

        print(
            "\n=== [3/4] Assembling Sample-Accurate 48kHz Master Audio ===", flush=True
        )
        sr = 48000
        total_samples = int(math.ceil((total_dur + 0.5) * sr))
        master_audio = np.zeros(total_samples, dtype=np.float32)

        # Add gentle chapter transition chime
        chime = make_chapter_chime(sr=sr)
        for ch in scene_meta.get("chapters", []):
            ch_idx = max(0, int(round(float(ch["start"]) * sr)))
            end_idx = min(total_samples, ch_idx + len(chime))
            master_audio[ch_idx:end_idx] += chime[: end_idx - ch_idx]

        # Place each voiced cue at its exact recorded start timestamp
        prev_voice_end = 0.0
        recorded_cues = scene_meta.get("cues", [])
        if len(recorded_cues) != len(cues_spec):
            raise RuntimeError(
                f"Cue count mismatch: Manim recorded {len(recorded_cues)} cues, spec has {len(cues_spec)}"
            )

        for idx, rec_cue in enumerate(recorded_cues):
            cid = rec_cue.get("cue_id") or cues_spec[idx]["id"]
            c_info = cue_map[cid]
            clip, clip_sr = read_wav_float32(Path(c_info["wav"]))
            assert clip_sr == sr, f"Expected {sr}Hz, got {clip_sr}Hz"

            start_sec = float(rec_cue["start"])
            clip_dur = len(clip) / float(sr)

            if start_sec < prev_voice_end - 0.02:
                raise RuntimeError(
                    f"Voice overlap detected at cue {cid}: starts at {start_sec:.2f}s before previous ended at {prev_voice_end:.2f}s"
                )
            prev_voice_end = start_sec + clip_dur

            s_idx = int(round(start_sec * sr))
            e_idx = min(total_samples, s_idx + len(clip))
            master_audio[s_idx:e_idx] += clip[: e_idx - s_idx]

            rec_cue["cue_id"] = cid
            rec_cue["voice_duration"] = round(clip_dur, 3)
            rec_cue["asr"] = c_info["asr"]

        # Trim master audio to exact video duration
        exact_samples = int(round(total_dur * sr))
        master_audio = np.clip(master_audio[:exact_samples], -0.98, 0.98)
        master_wav = tmp / "master.wav"
        write_wav_float32(master_wav, master_audio, sr=sr)

        print(
            "\n=== [4/4] Muxing Final MP4, Poster, and WebVTT Subtitles ===",
            flush=True,
        )
        final_mp4 = OUTPUT_DIR / f"{lesson_id}.mp4"
        poster_jpg = OUTPUT_DIR / f"{lesson_id}.jpg"
        vtt_path = OUTPUT_DIR / f"{lesson_id}.vtt"
        json_path = OUTPUT_DIR / f"{lesson_id}.lesson.json"

        subprocess.run(
            [
                "ffmpeg",
                "-hide_banner",
                "-loglevel",
                "error",
                "-y",
                "-i",
                str(raw_movie),
                "-i",
                str(master_wav),
                "-map",
                "0:v:0",
                "-map",
                "1:a:0",
                "-c:v",
                "copy",
                "-c:a",
                "aac",
                "-b:a",
                "192k",
                "-ar",
                "48000",
                "-shortest",
                "-movflags",
                "+faststart",
                str(final_mp4),
            ],
            check=True,
        )

        # Extract poster frame at 22% of video duration
        poster_time = min(14.0, total_dur * 0.22)
        subprocess.run(
            [
                "ffmpeg",
                "-hide_banner",
                "-loglevel",
                "error",
                "-y",
                "-ss",
                f"{poster_time:.2f}",
                "-i",
                str(final_mp4),
                "-frames:v",
                "1",
                "-vf",
                "scale=1280:-2",
                "-q:v",
                "2",
                str(poster_jpg),
            ],
            check=True,
        )

        # Write WebVTT subtitles
        vtt_lines = ["WEBVTT", ""]
        for i, cue in enumerate(recorded_cues, 1):
            vtt_lines.append(str(i))
            vtt_lines.append(f"{clock_vtt(cue['start'])} --> {clock_vtt(cue['end'])}")
            vtt_lines.append(cue["text"])
            vtt_lines.append("")
        vtt_path.write_text("\n".join(vtt_lines), encoding="utf-8")

        info = probe_media(final_mp4)
        assert info["has_audio"], f"Missing audio track in {final_mp4}"
        assert info["width"] == width and info["height"] == height

        lesson_meta = {
            "id": lesson_id,
            "title": title,
            "description": description,
            "domain": domain,
            "video": final_mp4.name,
            "poster": poster_jpg.name,
            "captions": vtt_path.name,
            "duration": info["duration"],
            "chapters": scene_meta.get("chapters", []),
            "cues": recorded_cues,
            "render": info,
        }
        json_path.write_text(
            json.dumps(lesson_meta, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(
            f"✅ Completed {final_mp4} ({info['duration']:.1f}s, {width}x{height}, 48kHz audio)",
            flush=True,
        )
        return final_mp4
