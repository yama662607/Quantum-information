"""Episode 3: 創薬×量子コンピュータと位相時計 (Hadamardテストの仕組み).

Covers:
1. Why drug discovery cares about binding energy ΔE and hits the 2^N wall
2. Schrödinger equation as a "phase clock": energy E = rotation speed θ = -Et/ℏ
3. Why global phase |e^(iθ)|^2 = 1 vanishes and how Controlled-U(t) keeps a reference hand
4. Hadamard test continuous animation: sweeping θ ∈ [0, 2π] on the unit circle vs p(0) wave
5. Minimal drug pocket model H = -gX: bonding |+⟩ (E = -g) vs antibonding |-⟩ (E = +g)
"""

from __future__ import annotations

import math
from pathlib import Path
import numpy as np
from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    always_redraw,
    Arrow,
    Circle,
    DashedLine,
    Dot,
    FadeIn,
    FadeOut,
    ImageMobject,
    Line,
    RoundedRectangle,
    ValueTracker,
    VGroup,
)
from learning_video.theme import (
    AMBER,
    BLUE,
    GRID,
    MINT,
    MUTED,
    PINK,
    RED,
    WHITE,
    code_text,
    panel,
    text,
)
from quantum_videos.voiced_engine import (
    CARD_ALT,
    CARD_BG,
    CYAN,
    SOFT_WHITE,
    VIOLET,
    VoicedTeachingScene,
    make_gate_box,
    make_ket_badge,
    make_meter_box,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
DRUG_IMG_PATH = REPO_ROOT / "quarto" / "assets" / "videos" / "img_drug_pocket.jpg"

LESSON_ID = "ep3-drug-discovery-phase"
TITLE = "第3話：創薬×量子コンピュータ — 分子エネルギーを「位相の時計」で測る"
DESCRIPTION = "なぜ創薬で量子コンピュータが注目されるのか？2^Nの壁からシュレーディンガー方程式の位相回転、Hadamardテストによる結合エネルギー測定までを視覚化する。"
DOMAIN = "量子化学・位相推定・Hadamardテスト"

CUES_EP3: list[dict[str, str]] = [
    {
        "id": "ep3_c01",
        "display": "第2話で見た「計算を位相の角度に刻んでHゲートで読み出す」発想は、創薬でどう役立つのでしょうか？",
        "tts": "第二話で見た、計算を位相の角度に刻んでエイチゲートで読み出すという発想は、創薬でどう役立つのでしょうか？",
    },
    {
        "id": "ep3_c02",
        "display": "薬が標的タンパク質のポケットにピタッと結合するかどうかは、基底状態のエネルギー E で決まります。",
        "tts": "薬が標的タンパク質のポケットにピタッと結合するかどうかは、基底状態のエネルギー、イーで決まります。",
    },
    {
        "id": "ep3_c03",
        "display": "しかし電子の軌道が N 個あると状態数は 2 の N 乗に爆発し、60軌道で古典スパコンのメモリ限界を超えます。",
        "tts": "しかし、電子の軌道がエヌ個あると、状態数は二のエヌ乗に爆発し、六十軌道で古典スパコンのメモリ限界を超えます。",
    },
    {
        "id": "ep3_c04",
        "display": "一方、量子コンピュータなら N 個の量子ビットに分子の状態をそのまま載せて時間発展させることができます。",
        "tts": "一方、量子コンピュータなら、エヌ個の量子ビットに分子の状態をそのまま載せて、時間発展させることができます。",
    },
    {
        "id": "ep3_c05",
        "display": "シュレーディンガー方程式によれば、エネルギー E の状態は、時間 t で位相が θ = -E t / ℏ だけ回ります。",
        "tts": "シュレーディンガー方程式によれば、エネルギー、イーの状態は、時間ティーで、位相がシータ・イコール・マイナス・イー・ティー割るエイチバーだけ回ります。",
    },
    {
        "id": "ep3_c06",
        "display": "つまり分子のエネルギー E とは、複素平面の「位相の時計」の針が回るスピードそのものなのです。",
        "tts": "つまり、分子のエネルギー、イーとは、複素平面の「位相の時計」の針が回るスピードそのものなのです。",
    },
    {
        "id": "ep3_c07",
        "display": "ところが、分子の量子状態だけを直接測定しても、絶対値の2乗は 1 になり、位相角 θ は消えてしまいます。",
        "tts": "ところが、分子の量子状態だけを直接測定しても、絶対値の二乗はイチになり、位相角シータは消えてしまいます。",
    },
    {
        "id": "ep3_c08",
        "display": "角度 θ を測るには「回っていない基準の針 |0⟩」と「θ だけ回った針 |1⟩」を干渉させる必要があります。",
        "tts": "角度シータを測るには、回っていない基準の針、ゼロ状態と、シータだけ回った針、イチ状態を、干渉させる必要があります。",
    },
    {
        "id": "ep3_c09",
        "display": "これを実現するのが Hadamard テストです。補助ビットが |1⟩ のときだけ分子を時間発展させます。",
        "tts": "これを実現するのがアダマールテストです。補助ビットがイチのときだけ、分子を時間発展させます。",
    },
    {
        "id": "ep3_c10",
        "display": "最後に補助ビットへ H ゲートをかけると、基準の針 1 と回転した針 e^(iθ) が足し合わされます。",
        "tts": "最後に補助ビットへエイチゲートを掛けると、基準の針イチと、回転した針、エクスポネンシャル・アイ・シータが足し合わされます。",
    },
    {
        "id": "ep3_c11",
        "display": "位相角 θ が 0 から 2π まで回ると、0 が測られる確率 p(0) = (1 + cos θ)/2 が波のように変化します！",
        "tts": "位相角シータがゼロから二パイまで回ると、ゼロが測られる確率、二分の一プラス・コサイン・シータが、波のように変化します！",
    },
    {
        "id": "ep3_c12",
        "display": "さらに Sダガーゲートを挟めば sin θ も測れるため、角度の符号まで一意に特定できます。",
        "tts": "さらにエスダガーゲートを挟めば、サイン・シータも測れるため、角度の符号まで一意に特定できます。",
    },
    {
        "id": "ep3_c13",
        "display": "では創薬ポケットの最小モデル H = -g X で実験しましょう。電子が共有される結合性状態 |+⟩ はエネルギー -g で安定化します。",
        "tts": "では、創薬ポケットの最小モデル、マイナス・ジー・エックスで実験しましょう。電子が共有される結合性状態、プラス状態は、エネルギー、マイナス・ジーで安定化します。",
    },
    {
        "id": "ep3_c14",
        "display": "Hadamard テストで CRX(-2gt) を動かせば、結合性状態と反結合性状態のエネルギー差がコサインの波として直接読み出せます。",
        "tts": "アダマールテストでシーアールエックスゲートを動かせば、結合性状態と反結合性状態のエネルギー差が、コサインの波として直接読み出せます。",
    },
]


def run_checks() -> None:
    """Verify Hamiltonian H = -gX eigenstates, time evolution, and Hadamard test probabilities."""
    X = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    ket_plus = np.array([1.0, 1.0], dtype=complex) / math.sqrt(2.0)
    ket_minus = np.array([1.0, -1.0], dtype=complex) / math.sqrt(2.0)

    g = 1.2
    H_op = -g * X
    assert np.allclose(H_op @ ket_plus, -g * ket_plus)
    assert np.allclose(H_op @ ket_minus, +g * ket_minus)

    for theta in np.linspace(0, 2 * math.pi, 9):
        # Hadamard test state on ancilla for eigenphase theta:
        # |0⟩ -> (|0⟩ + e^(i theta)|1⟩)/sqrt(2) -> H -> ((1+e^(i theta))/2)|0⟩ + ((1-e^(i theta))/2)|1⟩
        amp0_cos = 0.5 * (1.0 + np.exp(1j * theta))
        p0_cos = abs(amp0_cos) ** 2
        assert abs(p0_cos - 0.5 * (1.0 + math.cos(theta))) < 1e-12

        # With S^\dagger (-i on |1⟩):
        amp0_sin = 0.5 * (1.0 - 1j * np.exp(1j * theta))
        p0_sin = abs(amp0_sin) ** 2
        assert abs(p0_sin - 0.5 * (1.0 + math.sin(theta))) < 1e-12


class Ep3DrugDiscoveryPhaseScene(VoicedTeachingScene):
    """Voiced Manim scene for Episode 3: Drug Discovery & Hadamard Test."""

    def construct(self):
        run_checks()
        self.setup_shell(
            "第3話：創薬×量子コンピュータと位相時計",
            "創薬の「鍵と鍵穴」と 2^N の壁",
        )

        # =====================================================================
        # CHAPTER 1: Drug Discovery "Lock & Key" and the 2^N Wall
        # =====================================================================
        self.mark_chapter("創薬の「鍵と鍵穴」と 2^N の壁")

        img_frame = RoundedRectangle(
            width=5.8,
            height=4.0,
            corner_radius=0.18,
            stroke_color=CYAN,
            stroke_width=2.6,
            fill_color=CARD_BG,
            fill_opacity=0.95,
        ).move_to([-3.55, -0.35, 0])
        img_caption = text(
            "標的タンパク質ポケットと薬分子の電子雲（共有結合軌道）",
            17,
            CYAN,
            max_width=5.4,
        ).move_to([-3.55, -2.10, 0])

        if DRUG_IMG_PATH.is_file():
            drug_img = ImageMobject(str(DRUG_IMG_PATH))
            drug_img.set_width(5.45)
            drug_img.move_to([-3.55, -0.22, 0])
        else:
            drug_img = panel(5.4, 3.2, [-3.55, -0.22, 0])

        right_card = panel(6.6, 4.0, [3.10, -0.35, 0])
        right_title = text(
            "結合エネルギー ΔE と計算量の壁", 23, AMBER, max_width=6.0
        ).move_to([3.10, 1.25, 0])
        delta_e_eq = text(
            "ΔE = E(複合体) − [ E(タンパク質) + E(薬) ]", 20, WHITE, max_width=5.9
        ).move_to([3.10, 0.68, 0])
        delta_e_sub = text(
            "ΔE < 0 が大きくなるほど、薬がポケットに強く安定結合！",
            17,
            MINT,
            max_width=5.9,
        ).move_to([3.10, 0.25, 0])

        self.say_cue(
            "ep3_c01",
            "第2話で見た「計算を位相の角度に刻んでHゲートで読み出す」発想は、創薬でどう役立つのでしょうか？",
        )
        self.play(
            FadeIn(img_frame), FadeIn(drug_img), FadeIn(img_caption), run_time=1.0
        )
        self.finish_cue("ep3_c01")

        self.say_cue(
            "ep3_c02",
            "薬が標的タンパク質のポケットにピタッと結合するかどうかは、基底状態のエネルギー E で決まります。",
        )
        self.play(
            FadeIn(right_card),
            FadeIn(right_title),
            FadeIn(delta_e_eq),
            FadeIn(delta_e_sub),
            run_time=1.0,
        )
        self.finish_cue("ep3_c02")

        # 2^N explosion bars inside right_card
        scale_rows = VGroup(
            VGroup(
                code_text("N = 20 軌道", 18, SOFT_WHITE).move_to([0.90, -0.35, 0]),
                RoundedRectangle(
                    width=0.95,
                    height=0.32,
                    corner_radius=0.06,
                    stroke_color=BLUE,
                    fill_color=BLUE,
                    fill_opacity=0.6,
                ).move_to([2.40, -0.35, 0]),
                text("2^20 ≈ 100万 (PCで一瞬)", 16, BLUE, max_width=3.0).move_to(
                    [4.55, -0.35, 0]
                ),
            ),
            VGroup(
                code_text("N = 50 軌道", 18, AMBER).move_to([0.90, -0.92, 0]),
                RoundedRectangle(
                    width=1.80,
                    height=0.32,
                    corner_radius=0.06,
                    stroke_color=AMBER,
                    fill_color=AMBER,
                    fill_opacity=0.6,
                ).move_to([2.82, -0.92, 0]),
                text("2^50 ≈ 18 PB (スパコン限界)", 16, AMBER, max_width=2.3).move_to(
                    [4.98, -0.92, 0]
                ),
            ),
            VGroup(
                code_text("N = 60 軌道", 18, RED).move_to([0.90, -1.48, 0]),
                RoundedRectangle(
                    width=2.45,
                    height=0.32,
                    corner_radius=0.06,
                    stroke_color=RED,
                    fill_color=RED,
                    fill_opacity=0.75,
                ).move_to([3.15, -1.48, 0]),
                text("2^60 ≈ 18 EB (メモリ崩壊)", 16, RED, max_width=1.8).move_to(
                    [5.35, -1.48, 0]
                ),
            ),
        )

        self.say_cue(
            "ep3_c03",
            "しかし電子の軌道が N 個あると状態数は 2 の N 乗に爆発し、60軌道で古典スパコンのメモリ限界を超えます。",
        )
        self.play(
            FadeIn(scale_rows[0]),
            FadeIn(scale_rows[1]),
            FadeIn(scale_rows[2]),
            run_time=1.1,
        )
        self.finish_cue("ep3_c03")

        q_rescue_badge = RoundedRectangle(
            width=6.1,
            height=0.58,
            corner_radius=0.12,
            stroke_color=MINT,
            stroke_width=2.4,
            fill_color="#064E3B",
            fill_opacity=0.95,
        ).move_to([3.10, -2.02, 0])
        q_rescue_txt = text(
            "量子コンピュータ：N = 60 軌道 → たった 60 量子ビットで直接表現！",
            18,
            MINT,
            max_width=5.85,
        ).move_to([3.10, -2.02, 0])

        self.say_cue(
            "ep3_c04",
            "一方、量子コンピュータなら N 個の量子ビットに分子の状態をそのまま載せて時間発展させることができます。",
        )
        self.play(
            FadeOut(scale_rows[2][2]),
            FadeIn(q_rescue_badge),
            FadeIn(q_rescue_txt),
            run_time=0.9,
        )
        self.finish_cue("ep3_c04")

        self.play(
            FadeOut(img_frame),
            FadeOut(drug_img),
            FadeOut(img_caption),
            FadeOut(right_card),
            FadeOut(right_title),
            FadeOut(delta_e_eq),
            FadeOut(delta_e_sub),
            FadeOut(scale_rows),
            FadeOut(q_rescue_badge),
            FadeOut(q_rescue_txt),
            run_time=0.5,
        )

        # =====================================================================
        # CHAPTER 2: Energy E = Rotation Speed of the Phase Clock
        # =====================================================================
        self.mark_chapter("エネルギー E ＝「位相の時計」の回転速度")

        top_formula_card = panel(12.6, 1.15, [0.0, 1.45, 0])
        top_formula = text(
            "U(t) |ψ_E⟩ = exp(−i H t / ℏ) |ψ_E⟩ = exp(−i E t / ℏ) |ψ_E⟩ = e^(iθ) |ψ_E⟩",
            22,
            AMBER,
            max_width=12.0,
        ).move_to([0.0, 1.62, 0])
        top_formula_sub = text(
            "位相角 θ = −E t / ℏ  （エネルギー E が大きいほど、時間 t で位相の針が速く回る！）",
            19,
            SOFT_WHITE,
            max_width=12.0,
        ).move_to([0.0, 1.18, 0])

        # Two phase clocks side by side
        left_clock_panel = panel(6.0, 3.35, [-3.3, -1.05, 0])
        right_clock_panel = panel(6.0, 3.35, [3.3, -1.05, 0])

        lc_title = text(
            "安定な結合状態（エネルギー E_1 が低い）", 20, MINT, max_width=5.6
        ).move_to([-3.3, 0.25, 0])
        rc_title = text(
            "不安定な反発状態（エネルギー E_2 が高い）", 20, RED, max_width=5.6
        ).move_to([3.3, 0.25, 0])

        c1_center = np.array([-3.3, -1.20, 0.0])
        c2_center = np.array([3.3, -1.20, 0.0])
        rad = 1.05

        c1_circle = Circle(
            radius=rad,
            stroke_color=MINT,
            stroke_width=2.6,
            fill_color=CARD_ALT,
            fill_opacity=0.6,
        ).move_to(c1_center)
        c2_circle = Circle(
            radius=rad,
            stroke_color=RED,
            stroke_width=2.6,
            fill_color=CARD_ALT,
            fill_opacity=0.6,
        ).move_to(c2_center)
        c1_axes = VGroup(
            DashedLine(
                c1_center + LEFT * rad, c1_center + RIGHT * rad, stroke_color=GRID
            ),
            DashedLine(c1_center + DOWN * rad, c1_center + UP * rad, stroke_color=GRID),
        )
        c2_axes = VGroup(
            DashedLine(
                c2_center + LEFT * rad, c2_center + RIGHT * rad, stroke_color=GRID
            ),
            DashedLine(c2_center + DOWN * rad, c2_center + UP * rad, stroke_color=GRID),
        )

        time_tracker = ValueTracker(0.0)
        hand1 = always_redraw(
            lambda: Arrow(
                c1_center,
                c1_center
                + rad
                * np.array(
                    [
                        math.cos(0.9 * time_tracker.get_value()),
                        math.sin(0.9 * time_tracker.get_value()),
                        0.0,
                    ]
                ),
                buff=0.0,
                color=MINT,
                stroke_width=5.0,
                max_tip_length_to_length_ratio=0.22,
            )
        )
        hand2 = always_redraw(
            lambda: Arrow(
                c2_center,
                c2_center
                + rad
                * np.array(
                    [
                        math.cos(-2.7 * time_tracker.get_value()),
                        math.sin(-2.7 * time_tracker.get_value()),
                        0.0,
                    ]
                ),
                buff=0.0,
                color=RED,
                stroke_width=5.0,
                max_tip_length_to_length_ratio=0.22,
            )
        )
        c1_lbl = text("ゆっくり回転 (|θ| 小)", 18, MINT).move_to([-3.3, -2.45, 0])
        c2_lbl = text("高速に回転 (|θ| 大)", 18, RED).move_to([3.3, -2.45, 0])

        self.say_cue(
            "ep3_c05",
            "シュレーディンガー方程式によれば、エネルギー E の状態は、時間 t で位相が θ = -E t / ℏ だけ回ります。",
        )
        self.play(
            FadeIn(top_formula_card),
            FadeIn(top_formula),
            FadeIn(top_formula_sub),
            FadeIn(left_clock_panel),
            FadeIn(right_clock_panel),
            FadeIn(lc_title),
            FadeIn(rc_title),
            FadeIn(c1_circle),
            FadeIn(c2_circle),
            FadeIn(c1_axes),
            FadeIn(c2_axes),
            FadeIn(hand1),
            FadeIn(hand2),
            FadeIn(c1_lbl),
            FadeIn(c2_lbl),
            run_time=1.0,
        )
        self.finish_cue("ep3_c05")

        self.say_cue(
            "ep3_c06",
            "つまり分子のエネルギー E とは、複素平面の「位相の時計」の針が回るスピードそのものなのです。",
        )
        self.play(time_tracker.animate.set_value(2.4), run_time=3.4)
        self.finish_cue("ep3_c06")

        self.play(
            FadeOut(top_formula_card),
            FadeOut(top_formula),
            FadeOut(top_formula_sub),
            FadeOut(left_clock_panel),
            FadeOut(right_clock_panel),
            FadeOut(lc_title),
            FadeOut(rc_title),
            FadeOut(c1_circle),
            FadeOut(c2_circle),
            FadeOut(c1_axes),
            FadeOut(c2_axes),
            FadeOut(hand1),
            FadeOut(hand2),
            FadeOut(c1_lbl),
            FadeOut(c2_lbl),
            run_time=0.5,
        )

        # =====================================================================
        # CHAPTER 3: The Global Phase Trap & Hadamard Test Circuit
        # =====================================================================
        self.mark_chapter("グローバル位相の罠と Hadamard テスト回路")

        trap_box = RoundedRectangle(
            width=12.6,
            height=1.10,
            corner_radius=0.14,
            stroke_color=RED,
            stroke_width=2.4,
            fill_color="#3B1219",
            fill_opacity=0.92,
        ).move_to([0.0, 1.50, 0])
        trap_txt = text(
            "罠：分子レジスタ e^(iθ)|ψ⟩ をそのまま測定しても、確率 |e^(iθ)|^2 = 1 となり角度 θ は完全に消える！",
            21,
            RED,
            max_width=12.1,
        ).move_to([0.0, 1.50, 0])

        self.say_cue(
            "ep3_c07",
            "ところが、分子の量子状態だけを直接測定しても、絶対値の2乗は 1 になり、位相角 θ は消えてしまいます。",
        )
        self.play(FadeIn(trap_box), FadeIn(trap_txt), run_time=0.9)
        self.finish_cue("ep3_c07")

        # Hadamard Test Circuit Panel
        ht_panel = panel(12.6, 3.45, [0.0, -0.95, 0])
        ht_title = text(
            "解決策：Hadamard テスト — 補助ビットに「基準の針」と「回転した針」を作って干渉させる",
            20,
            MINT,
            max_width=12.0,
        ).move_to([0.0, 0.42, 0])

        y_anc = -0.45
        y_mol = -1.75
        w_anc = Line(
            [-4.6, y_anc, 0], [2.4, y_anc, 0], stroke_color=WHITE, stroke_width=3.0
        )
        w_mol = Line(
            [-4.6, y_mol, 0], [2.4, y_mol, 0], stroke_color=CYAN, stroke_width=3.0
        )

        in_anc = make_ket_badge("補助 |0⟩", [-5.45, y_anc, 0], color=BLUE, width=1.45)
        in_mol = make_ket_badge("分子 |ψ⟩", [-5.45, y_mol, 0], color=CYAN, width=1.45)

        h1_gate = make_gate_box("H", [-3.2, y_anc, 0], color=BLUE)
        ctrl_line = Line(
            [-1.1, y_anc, 0],
            [-1.1, y_mol + 0.48, 0],
            stroke_color=AMBER,
            stroke_width=3.2,
        )
        ctrl_dot = Dot([-1.1, y_anc, 0], radius=0.11, color=AMBER)
        u_box = make_gate_box(
            "U(t)", [-1.1, y_mol, 0], color=AMBER, size=0.96, font_size=24
        )
        h2_gate = make_gate_box("H", [1.0, y_anc, 0], color=BLUE)
        meter = make_meter_box([2.4, y_anc, 0], color=MINT)

        mid_state_badge = RoundedRectangle(
            width=4.3,
            height=0.56,
            corner_radius=0.10,
            stroke_color=AMBER,
            stroke_width=2.0,
            fill_color=CARD_ALT,
            fill_opacity=0.95,
        ).move_to([-1.1, -2.42, 0])
        mid_state_txt = text(
            "(|0⟩ + e^(iθ)|1⟩) / √2 ⊗ |ψ⟩", 18, AMBER, max_width=4.0
        ).move_to([-1.1, -2.42, 0])

        out_state_badge = RoundedRectangle(
            width=3.25,
            height=1.10,
            corner_radius=0.12,
            stroke_color=MINT,
            stroke_width=2.2,
            fill_color=CARD_ALT,
            fill_opacity=0.95,
        ).move_to([4.50, -0.95, 0])
        out_state_txt1 = text("p(0) = (1 + cos θ)/2", 18, MINT, max_width=3.0).move_to(
            [4.50, -0.68, 0]
        )
        out_state_txt2 = text("p(1) = (1 − cos θ)/2", 18, PINK, max_width=3.0).move_to(
            [4.50, -1.22, 0]
        )

        self.say_cue(
            "ep3_c08",
            "角度 θ を測るには「回っていない基準の針 |0⟩」と「θ だけ回った針 |1⟩」を干渉させる必要があります。",
        )
        self.play(
            FadeIn(ht_panel),
            FadeIn(ht_title),
            FadeIn(w_anc),
            FadeIn(w_mol),
            FadeIn(in_anc),
            FadeIn(in_mol),
            FadeIn(h1_gate),
            run_time=1.0,
        )
        self.finish_cue("ep3_c08")

        self.say_cue(
            "ep3_c09",
            "これを実現するのが Hadamard テストです。補助ビットが |1⟩ のときだけ分子を時間発展させます。",
        )
        self.play(
            FadeIn(ctrl_line),
            FadeIn(ctrl_dot),
            FadeIn(u_box),
            FadeIn(mid_state_badge),
            FadeIn(mid_state_txt),
            run_time=1.0,
        )
        self.finish_cue("ep3_c09")

        self.say_cue(
            "ep3_c10",
            "最後に補助ビットへ H ゲートをかけると、基準の針 1 と回転した針 e^(iθ) が足し合わされます。",
        )
        self.play(
            FadeIn(h2_gate),
            FadeIn(meter),
            FadeIn(out_state_badge),
            FadeIn(out_state_txt1),
            FadeIn(out_state_txt2),
            run_time=1.0,
        )
        self.finish_cue("ep3_c10")

        self.play(
            FadeOut(trap_box),
            FadeOut(trap_txt),
            FadeOut(ht_panel),
            FadeOut(ht_title),
            FadeOut(w_anc),
            FadeOut(w_mol),
            FadeOut(in_anc),
            FadeOut(in_mol),
            FadeOut(h1_gate),
            FadeOut(ctrl_line),
            FadeOut(ctrl_dot),
            FadeOut(u_box),
            FadeOut(h2_gate),
            FadeOut(meter),
            FadeOut(mid_state_badge),
            FadeOut(mid_state_txt),
            FadeOut(out_state_badge),
            FadeOut(out_state_txt1),
            FadeOut(out_state_txt2),
            run_time=0.5,
        )

        # =====================================================================
        # CHAPTER 4: Continuous Sweep of θ on Unit Circle vs Probability Wave
        # =====================================================================
        self.mark_chapter("位相が確率の波に変わる瞬間 (cos θ と sin θ)")

        left_wave_panel = panel(5.5, 4.5, [-3.65, -0.35, 0])
        right_wave_panel = panel(6.9, 4.5, [2.95, -0.35, 0])

        lw_title = text(
            "複素平面：基準 1/2 ＋ 回転 e^(iθ)/2", 20, WHITE, max_width=5.1
        ).move_to([-3.65, 1.52, 0])
        rw_title = text("測定確率 p(0) の干渉波形", 20, WHITE, max_width=6.4).move_to(
            [2.95, 1.52, 0]
        )

        uc_center = np.array([-3.65, -0.55, 0.0])
        uc_rad = 1.45
        uc_circle = Circle(
            radius=uc_rad,
            stroke_color=BLUE,
            stroke_width=2.2,
            fill_color=CARD_ALT,
            fill_opacity=0.45,
        ).move_to(uc_center)
        uc_axes = VGroup(
            DashedLine(
                uc_center + LEFT * uc_rad, uc_center + RIGHT * uc_rad, stroke_color=GRID
            ),
            DashedLine(
                uc_center + DOWN * uc_rad, uc_center + UP * uc_rad, stroke_color=GRID
            ),
        )

        theta_tracker = ValueTracker(0.0)

        # Vector 1/2 (fixed along +x) and e^(iθ)/2 (tip-to-tail from 1/2)
        vec_ref = Arrow(
            uc_center,
            uc_center + np.array([uc_rad * 0.5, 0.0, 0.0]),
            buff=0.0,
            color=BLUE,
            stroke_width=4.5,
            max_tip_length_to_length_ratio=0.22,
        )
        vec_rot = always_redraw(
            lambda: Arrow(
                uc_center + np.array([uc_rad * 0.5, 0.0, 0.0]),
                uc_center
                + np.array(
                    [
                        uc_rad * 0.5 * (1.0 + math.cos(theta_tracker.get_value())),
                        uc_rad * 0.5 * math.sin(theta_tracker.get_value()),
                        0.0,
                    ]
                ),
                buff=0.0,
                color=AMBER,
                stroke_width=4.5,
                max_tip_length_to_length_ratio=0.22,
            )
        )
        vec_sum = always_redraw(
            lambda: Line(
                uc_center,
                uc_center
                + np.array(
                    [
                        uc_rad * 0.5 * (1.0 + math.cos(theta_tracker.get_value())),
                        uc_rad * 0.5 * math.sin(theta_tracker.get_value()),
                        0.0,
                    ]
                ),
                stroke_color=MINT,
                stroke_width=5.5,
            )
        )
        sum_dot = always_redraw(
            lambda: Dot(
                uc_center
                + np.array(
                    [
                        uc_rad * 0.5 * (1.0 + math.cos(theta_tracker.get_value())),
                        uc_rad * 0.5 * math.sin(theta_tracker.get_value()),
                        0.0,
                    ]
                ),
                radius=0.10,
                color=MINT,
            )
        )

        # Right side plot axes manually mapped for clean appearance
        x0, x1 = 0.25, 5.75
        y0, y1 = -1.62, 0.78
        ax_x = Line([x0, y0, 0], [x1, y0, 0], stroke_color=MUTED, stroke_width=2.2)
        ax_y = Line([x0, y0, 0], [x0, y1, 0], stroke_color=MUTED, stroke_width=2.2)
        lbl_y1 = code_text("1.0", 16, MUTED).move_to([x0 - 0.35, y1, 0])
        lbl_y05 = code_text("0.5", 16, MUTED).move_to([x0 - 0.35, 0.5 * (y0 + y1), 0])
        lbl_y0 = code_text("0.0", 16, MUTED).move_to([x0 - 0.35, y0, 0])
        lbl_x0 = code_text("0", 15, MUTED).move_to([x0, y0 - 0.25, 0])
        lbl_xpi = code_text("π", 15, MUTED).move_to([0.5 * (x0 + x1), y0 - 0.25, 0])
        lbl_x2pi = code_text("2π", 15, MUTED).move_to([x1, y0 - 0.25, 0])

        def pt_on_plot(th: float, prob: float) -> np.ndarray:
            px = x0 + (th / (2 * math.pi)) * (x1 - x0)
            py = y0 + prob * (y1 - y0)
            return np.array([px, py, 0.0])

        # Pre-draw smooth cosine curve and sine curve using short line segments
        thetas = np.linspace(0, 2 * math.pi, 80)
        cos_curve = VGroup(
            *[
                Line(
                    pt_on_plot(thetas[i], 0.5 * (1.0 + math.cos(thetas[i]))),
                    pt_on_plot(thetas[i + 1], 0.5 * (1.0 + math.cos(thetas[i + 1]))),
                    stroke_color=MINT,
                    stroke_width=3.8,
                )
                for i in range(len(thetas) - 1)
            ]
        )
        sin_curve = VGroup(
            *[
                Line(
                    pt_on_plot(thetas[i], 0.5 * (1.0 - math.sin(thetas[i]))),
                    pt_on_plot(thetas[i + 1], 0.5 * (1.0 - math.sin(thetas[i + 1]))),
                    stroke_color=VIOLET,
                    stroke_width=3.0,
                    stroke_opacity=0.85,
                )
                for i in range(len(thetas) - 1)
            ]
        )

        moving_cos_dot = always_redraw(
            lambda: Dot(
                pt_on_plot(
                    theta_tracker.get_value(),
                    0.5 * (1.0 + math.cos(theta_tracker.get_value())),
                ),
                radius=0.11,
                color=MINT,
            )
        )
        cos_legend = text(
            "実部テスト: p_cos(0) = (1 + cos θ)/2", 18, MINT, max_width=6.0
        ).move_to([2.95, 1.12, 0])
        sin_legend = text(
            "虚部テスト(S†追加): p_sin(0) = (1 − sin θ)/2", 17, VIOLET, max_width=6.0
        ).move_to([2.95, -2.28, 0])

        self.say_cue(
            "ep3_c11",
            "位相角 θ が 0 から 2π まで回ると、0 が測られる確率 p(0) = (1 + cos θ)/2 が波のように変化します！",
        )
        self.play(
            FadeIn(left_wave_panel),
            FadeIn(right_wave_panel),
            FadeIn(lw_title),
            FadeIn(rw_title),
            FadeIn(uc_circle),
            FadeIn(uc_axes),
            FadeIn(vec_ref),
            FadeIn(vec_rot),
            FadeIn(vec_sum),
            FadeIn(sum_dot),
            FadeIn(ax_x),
            FadeIn(ax_y),
            FadeIn(lbl_y1),
            FadeIn(lbl_y05),
            FadeIn(lbl_y0),
            FadeIn(lbl_x0),
            FadeIn(lbl_xpi),
            FadeIn(lbl_x2pi),
            FadeIn(cos_curve),
            FadeIn(moving_cos_dot),
            FadeIn(cos_legend),
            run_time=1.0,
        )
        self.play(theta_tracker.animate.set_value(2 * math.pi), run_time=4.2)
        self.finish_cue("ep3_c11")

        self.say_cue(
            "ep3_c12",
            "さらに Sダガーゲートを挟めば sin θ も測れるため、角度の符号まで一意に特定できます。",
        )
        self.play(FadeIn(sin_curve), FadeIn(sin_legend), run_time=1.0)
        self.finish_cue("ep3_c12")

        self.play(
            FadeOut(left_wave_panel),
            FadeOut(right_wave_panel),
            FadeOut(lw_title),
            FadeOut(rw_title),
            FadeOut(uc_circle),
            FadeOut(uc_axes),
            FadeOut(vec_ref),
            FadeOut(vec_rot),
            FadeOut(vec_sum),
            FadeOut(sum_dot),
            FadeOut(ax_x),
            FadeOut(ax_y),
            FadeOut(lbl_y1),
            FadeOut(lbl_y05),
            FadeOut(lbl_y0),
            FadeOut(lbl_x0),
            FadeOut(lbl_xpi),
            FadeOut(lbl_x2pi),
            FadeOut(cos_curve),
            FadeOut(sin_curve),
            FadeOut(moving_cos_dot),
            FadeOut(cos_legend),
            FadeOut(sin_legend),
            run_time=0.5,
        )

        # =====================================================================
        # CHAPTER 5: Minimal Drug Pocket Model H = -gX
        # =====================================================================
        self.mark_chapter("創薬ポケットの最小量子モデル H = −gX")

        model_panel = panel(12.6, 4.5, [0.0, -0.35, 0])
        model_title = text(
            "練習問題：ポケットと薬の間を電子が飛び移る最小モデル  H = −g X",
            23,
            AMBER,
            max_width=12.0,
        ).move_to([0.0, 1.48, 0])

        bond_card = RoundedRectangle(
            width=5.6,
            height=2.25,
            corner_radius=0.14,
            stroke_color=MINT,
            stroke_width=2.6,
            fill_color="#064E3B",
            fill_opacity=0.85,
        ).move_to([-3.1, 0.0, 0])
        bond_t1 = text(
            "結合性状態 |+⟩ = (|0⟩ + |1⟩)/√2", 21, MINT, max_width=5.2
        ).move_to([-3.1, 0.65, 0])
        bond_t2 = code_text("H |+⟩ = −g |+⟩   (E_+ = −g < 0)", 20, WHITE).move_to(
            [-3.1, 0.05, 0]
        )
        bond_t3 = text(
            "電子雲が共有されエネルギー低下 → 安定結合！", 18, MINT, max_width=5.2
        ).move_to([-3.1, -0.55, 0])

        anti_card = RoundedRectangle(
            width=5.6,
            height=2.25,
            corner_radius=0.14,
            stroke_color=RED,
            stroke_width=2.6,
            fill_color="#450A0A",
            fill_opacity=0.85,
        ).move_to([3.1, 0.0, 0])
        anti_t1 = text(
            "反結合性状態 |−⟩ = (|0⟩ − |1⟩)/√2", 21, RED, max_width=5.2
        ).move_to([3.1, 0.65, 0])
        anti_t2 = code_text("H |−⟩ = +g |−⟩   (E_− = +g > 0)", 20, WHITE).move_to(
            [3.1, 0.05, 0]
        )
        anti_t3 = text(
            "電子雲の符号が反転し反発 → 不安定化！", 18, RED, max_width=5.2
        ).move_to([3.1, -0.55, 0])

        qiskit_bar = RoundedRectangle(
            width=11.8,
            height=1.0,
            corner_radius=0.12,
            stroke_color=CYAN,
            stroke_width=2.2,
            fill_color=CARD_ALT,
            fill_opacity=0.95,
        ).move_to([0.0, -1.85, 0])
        qiskit_txt1 = text(
            "時間発展 U(t) = exp(i g t X) = RX(−2gt)  ⇒  制御付きゲート CRX(−2gt) 1個で実装可能！",
            19,
            CYAN,
            max_width=11.2,
        ).move_to([0.0, -1.65, 0])
        qiskit_txt2 = text(
            "次話：この「位相の時計」の箱 U を、素因数分解の周期発見に差し替えると Shor のアルゴリズムになる！",
            18,
            AMBER,
            max_width=11.2,
        ).move_to([0.0, -2.08, 0])

        self.say_cue(
            "ep3_c13",
            "では創薬ポケットの最小モデル H = -g X で実験しましょう。電子が共有される結合性状態 |+⟩ はエネルギー -g で安定化します。",
        )
        self.play(
            FadeIn(model_panel),
            FadeIn(model_title),
            FadeIn(bond_card),
            FadeIn(bond_t1),
            FadeIn(bond_t2),
            FadeIn(bond_t3),
            FadeIn(anti_card),
            FadeIn(anti_t1),
            FadeIn(anti_t2),
            FadeIn(anti_t3),
            run_time=1.1,
        )
        self.finish_cue("ep3_c13")

        self.say_cue(
            "ep3_c14",
            "Hadamard テストで CRX(-2gt) を動かせば、結合性状態と反結合性状態のエネルギー差がコサインの波として直接読み出せます。",
        )
        self.play(
            FadeIn(qiskit_bar), FadeIn(qiskit_txt1), FadeIn(qiskit_txt2), run_time=1.0
        )
        self.finish_cue("ep3_c14", extra_pad=0.8)
