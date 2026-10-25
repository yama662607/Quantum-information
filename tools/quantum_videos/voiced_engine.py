"""Audio-first voiced Manim video engine for Quantum Information seminar videos.

Combines:
1. Local 48 kHz Japanese TTS (Irodori-TTS v4.1 Small MF fp16 via anima venv) with
   SHA-256 caching, silence trimming, cosine fade-in/out, RMS loudness normalization,
   and automatic Whisper ASR verification (via local omlx-server on port 8001).
2. Manim Community 0.21.0 + TimelineRenderer (via manim-learning-video venv) with
   exact cue duration synchronization so visual animations and spoken narration
   never drift, overlap, or clip.
3. Sample-accurate 48 kHz master audio assembly + FFmpeg H.264/AAC muxing + WebVTT
   subtitles + poster frame extraction.
"""

from __future__ import annotations

import os
import json
from pathlib import Path
from manim import (
    PI,
    Arc,
    Circle,
    Dot,
    Line,
    RoundedRectangle,
    VGroup,
)
from learning_video.theme import (
    AMBER,
    BLUE,
    GRID,
    MINT,
    MUTED,
    RED,
    WHITE,
    TeachingScene,
    code_text,
    panel,
    text,
)

DARK_BG = "#101827"
CARD_BG = "#182338"
CARD_ALT = "#1E2D47"
CYAN = "#38BDF8"
VIOLET = "#C084FC"
GREEN = "#4ADE80"
SOFT_WHITE = "#F4F6FC"


class VoicedTeachingScene(TeachingScene):
    """TeachingScene synchronized to pre-synthesized 48 kHz TTS cue durations."""

    def setup(self):
        super().setup()
        timing_path = os.environ.get("QUANTUM_VIDEO_TIMING_JSON", "")
        self.cue_durations: dict[str, float] = {}
        if timing_path and Path(timing_path).is_file():
            data = json.loads(Path(timing_path).read_text(encoding="utf-8"))
            for item in data.get("cues", []):
                self.cue_durations[item["id"]] = float(item["duration"])
        self._cue_started_at: float = 0.0
        self._current_cue_id: str | None = None

    def say_cue(self, cue_id: str, display_text: str):
        """Show 1-2 line subtitle and mark exact start timestamp for TTS placement."""
        self.say(display_text)
        if self.lesson_cues:
            self.lesson_cues[-1]["cue_id"] = cue_id
        self._cue_started_at = float(self.time)
        self._current_cue_id = cue_id

    def finish_cue(self, cue_id: str | None = None, extra_pad: float = 0.42):
        """Wait until the spoken TTS clip for this cue has completely finished + pad."""
        cid = cue_id or self._current_cue_id
        audio_dur = self.cue_durations.get(cid, 3.2) if cid else 3.2
        elapsed = float(self.time) - self._cue_started_at
        remaining = (audio_dur + extra_pad) - elapsed
        self.wait(max(0.25, remaining))

    def setup_shell(self, domain: str, title: str):
        return self.start_lesson(domain, title)

    def mark_chapter(self, title: str):
        return self.chapter(title)


# ---------------------------------------------------------------------------
# Reusable Quantum Circuit & Visual Building Blocks for Manim
# ---------------------------------------------------------------------------


def make_ket_badge(
    label_str: str,
    center,
    color: str = BLUE,
    width: float = 1.45,
    height: float = 0.68,
    font_size: int = 26,
) -> VGroup:
    box = RoundedRectangle(
        width=width,
        height=height,
        corner_radius=0.14,
        stroke_color=color,
        stroke_width=2.2,
        fill_color=CARD_ALT,
        fill_opacity=0.96,
    ).move_to(center)
    lbl = text(label_str, font_size, color, max_width=width - 0.18).move_to(center)
    return VGroup(box, lbl)


def make_gate_box(
    label_str: str, center, color: str = BLUE, size: float = 0.86, font_size: int = 28
) -> VGroup:
    box = RoundedRectangle(
        width=size,
        height=size,
        corner_radius=0.12,
        stroke_color=color,
        stroke_width=2.6,
        fill_color=CARD_BG,
        fill_opacity=0.98,
    ).move_to(center)
    lbl = text(label_str, font_size, WHITE, max_width=size - 0.14).move_to(center)
    return VGroup(box, lbl)


def make_wide_gate_box(
    label_str: str,
    sub_str: str,
    center,
    color: str = AMBER,
    width: float = 1.45,
    height: float = 2.1,
    font_size: int = 28,
) -> VGroup:
    box = RoundedRectangle(
        width=width,
        height=height,
        corner_radius=0.15,
        stroke_color=color,
        stroke_width=2.8,
        fill_color=CARD_BG,
        fill_opacity=0.98,
    ).move_to(center)
    lbl = text(label_str, font_size, color, max_width=width - 0.16).move_to(
        [center[0], center[1] + 0.25, 0]
    )
    sub = text(sub_str, 19, SOFT_WHITE, max_width=width - 0.16).move_to(
        [center[0], center[1] - 0.32, 0]
    )
    return VGroup(box, lbl, sub)


def make_cnot_symbol(
    x: float, y_ctrl: float, y_targ: float, color: str = MINT
) -> VGroup:
    line = Line([x, y_ctrl, 0], [x, y_targ, 0], stroke_color=color, stroke_width=3.2)
    ctrl_dot = Dot([x, y_ctrl, 0], radius=0.11, color=color)
    targ_circle = Circle(
        radius=0.24,
        stroke_color=color,
        stroke_width=2.8,
        fill_color=CARD_BG,
        fill_opacity=1.0,
    ).move_to([x, y_targ, 0])
    plus_h = Line(
        [x - 0.16, y_targ, 0],
        [x + 0.16, y_targ, 0],
        stroke_color=color,
        stroke_width=2.6,
    )
    plus_v = Line(
        [x, y_targ - 0.16, 0],
        [x, y_targ + 0.16, 0],
        stroke_color=color,
        stroke_width=2.6,
    )
    return VGroup(line, ctrl_dot, targ_circle, plus_h, plus_v)


def make_meter_box(center, size: float = 0.82, color: str = AMBER) -> VGroup:
    box = RoundedRectangle(
        width=size,
        height=size,
        corner_radius=0.12,
        stroke_color=color,
        stroke_width=2.4,
        fill_color="#0F172A",
        fill_opacity=0.98,
    ).move_to(center)
    arc = Arc(
        radius=0.24,
        start_angle=0.15 * PI,
        angle=0.7 * PI,
        stroke_color=WHITE,
        stroke_width=2.2,
    ).move_to([center[0], center[1] - 0.06, 0])
    needle = Line(
        [center[0], center[1] - 0.18, 0],
        [center[0] + 0.16, center[1] + 0.16, 0],
        stroke_color=color,
        stroke_width=2.6,
    )
    return VGroup(box, arc, needle)


def make_heatmap_2x2(
    vals, center, title_str: str, subtitle_str: str, offdiag_color: str = BLUE
) -> VGroup:
    """Create a 2x2 density matrix visual card."""
    card = panel(4.1, 3.6, center)
    t_lbl = text(title_str, 21, WHITE, max_width=3.8).move_to(
        [center[0], center[1] + 1.38, 0]
    )
    s_lbl = text(subtitle_str, 17, offdiag_color, max_width=3.8).move_to(
        [center[0], center[1] + 0.98, 0]
    )

    cells = VGroup()
    cell_size = 1.05
    grid_y0 = center[1] - 0.35
    row_labels = ["|0⟩", "|1⟩"]
    col_labels = ["⟨0|", "⟨1|"]

    for r in range(2):
        rl = text(row_labels[r], 18, MUTED).move_to(
            [center[0] - 1.38, grid_y0 + (0.5 - r) * cell_size, 0]
        )
        cl = text(col_labels[r], 18, MUTED).move_to(
            [center[0] + (r - 0.5) * cell_size, grid_y0 - 1.25, 0]
        )
        cells.add(rl, cl)
        for c in range(2):
            v = vals[r][c]
            cx = center[0] + (c - 0.5) * cell_size
            cy = grid_y0 + (0.5 - r) * cell_size
            is_diag = r == c
            if is_diag:
                fill_c = "#1E3A8A"
                stroke_c = BLUE
                txt_c = WHITE
                role = "確率"
            else:
                if abs(v) < 1e-6:
                    fill_c = "#1F2937"
                    stroke_c = GRID
                    txt_c = MUTED
                    role = "干渉消滅!"
                elif v > 0:
                    fill_c = "#065F46"
                    stroke_c = MINT
                    txt_c = MINT
                    role = "干渉 (+)"
                else:
                    fill_c = "#7F1D1D"
                    stroke_c = RED
                    txt_c = RED
                    role = "干渉 (−)"
            rect = RoundedRectangle(
                width=cell_size - 0.08,
                height=cell_size - 0.08,
                corner_radius=0.08,
                stroke_color=stroke_c,
                stroke_width=2.0,
                fill_color=fill_c,
                fill_opacity=0.92,
            ).move_to([cx, cy, 0])
            v_str = f"{v:+.1f}" if not is_diag and abs(v) > 1e-6 else f"{v:.1f}"
            v_txt = code_text(v_str, 22, txt_c).move_to([cx, cy + 0.14, 0])
            r_txt = text(role, 14, txt_c, max_width=0.9).move_to([cx, cy - 0.22, 0])
            cells.add(rect, v_txt, r_txt)

    return VGroup(card, t_lbl, s_lbl, cells)
