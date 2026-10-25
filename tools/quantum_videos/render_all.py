"""Master runner to synthesize TTS, render Manim, and mux all 4 Quantum Information seminar videos."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

TOOLS_DIR = Path(__file__).resolve().parents[1]
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from quantum_videos.build_pipeline import build_voiced_lesson  # noqa: E402
from quantum_videos import (  # noqa: E402
    ep1_recap_and_deutsch as ep1,
    ep2_secret_key_bv as ep2,
    ep3_drug_discovery_phase as ep3,
    ep4_shor_and_frontier as ep4,
)

EPISODES = {
    "ep1": {
        "lesson_id": "ep1-recap-and-deutsch",
        "title": "第1話：量子回路の読み方と、素朴な回路が失敗する理由（Deutschの必然）",
        "description": "前回の復習（X・Z・Hゲートと量子干渉）から始め、素朴な回路がエンタングルメントで干渉を失う理由と、固有状態|−⟩による位相キックバックの必然性を視覚化する。",
        "domain": "第1回復習 ＆ 第2回導入",
        "source_py": Path(ep1.__file__),
        "scene_class": "Ep1RecapAndDeutsch",
        "cues_spec": ep1.CUES_EP1,
        "check_fn": ep1.run_checks,
    },
    "ep2": {
        "lesson_id": "ep2-secret-key-bv",
        "title": "第2話：100万回の質問を1回にする「秘密の鍵」一発抽出（Bernstein–Vazirani）",
        "description": "ターゲットを|−⟩にしたCNOTがコントロール側のZゲートになる性質から出発し、n桁の秘密の鍵sをたった1回の質問で一斉転写するBernstein–Vazirani回路を解き明かす。",
        "domain": "量子アルゴリズムと一斉位相転写",
        "source_py": Path(ep2.__file__),
        "scene_class": "Ep2SecretKeyBV",
        "cues_spec": ep2.CUES_EP2,
        "check_fn": ep2.run_checks,
    },
    "ep3": {
        "lesson_id": ep3.LESSON_ID,
        "title": ep3.TITLE,
        "description": ep3.DESCRIPTION,
        "domain": ep3.DOMAIN,
        "source_py": Path(ep3.__file__),
        "scene_class": "Ep3DrugDiscoveryPhaseScene",
        "cues_spec": ep3.CUES_EP3,
        "check_fn": ep3.run_checks,
    },
    "ep4": {
        "lesson_id": ep4.LESSON_ID,
        "title": ep4.TITLE,
        "description": ep4.DESCRIPTION,
        "domain": ep4.DOMAIN,
        "source_py": Path(ep4.__file__),
        "scene_class": "Ep4ShorAndFrontierScene",
        "cues_spec": ep4.CUES_EP4,
        "check_fn": ep4.run_checks,
    },
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Render voiced Manim Quantum Information videos."
    )
    parser.add_argument(
        "--episodes",
        nargs="*",
        default=["ep1", "ep2", "ep3", "ep4"],
        choices=["ep1", "ep2", "ep3", "ep4"],
        help="Episodes to build (default: all 4).",
    )
    parser.add_argument(
        "--quality",
        default="high",
        choices=["preview", "medium", "high"],
        help="Render quality (preview=540p15, medium=720p30, high=1080p30).",
    )
    args = parser.parse_args(argv)

    for key in args.episodes:
        spec = EPISODES[key]
        print("\n=======================================================")
        print(f"Running mathematical self-checks for {key}: {spec['title']}")
        print("=======================================================")
        spec["check_fn"]()
        build_voiced_lesson(
            lesson_id=spec["lesson_id"],
            title=spec["title"],
            description=spec["description"],
            domain=spec["domain"],
            source_py=spec["source_py"],
            scene_class=spec["scene_class"],
            cues_spec=spec["cues_spec"],
            quality=args.quality,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
