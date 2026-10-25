"""Episode 4: Shorの因数分解と量子優位の直感マップ・2026最前線.

Covers:
1. Replacing molecular U(t) with modular multiplication U_a|x⟩ = |ax mod N⟩ (Shor's period finding on N=15)
2. The 4-Category Quantum Advantage Intuition Map (Simulation / Periodic Interference / Grover / Classical)
3. 2025-2026 Frontier (Google DQI, Google Willow & Quantum Echoes, IBM Logical Qubits + HPC) & Grand Finale
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
    Arrow,
    FadeIn,
    FadeOut,
    ImageMobject,
    RoundedRectangle,
    Transform,
    VGroup,
)
from learning_video.theme import (
    AMBER,
    BLUE,
    MINT,
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
    make_ket_badge,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
HERO_IMG_PATH = REPO_ROOT / "quarto" / "assets" / "videos" / "img_phase_clock_hero.jpg"

LESSON_ID = "ep4-shor-and-frontier"
TITLE = "第4話：Shorの因数分解から「量子優位の直感マップ」・2026最前線へ"
DESCRIPTION = "創薬の位相推定とShorの素因数分解がまったく同じ骨格であることを示し、どんな課題で量子コンピュータが速くなるかを見抜く4分類マップと2026年最新動向をまとめる。"
DOMAIN = "Shorのアルゴリズム・量子優位性・2026最前線"

CUES_EP4: list[dict[str, str]] = [
    {
        "id": "ep4_c01",
        "display": "第3話では、分子の時間発展 U(t) が回る角度 θ から創薬の結合エネルギーを読み出しました。",
        "tts": "第三話では、分子の時間発展、ユー・ティーが回る角度シータから、創薬の結合エネルギーを読み出しました。",
    },
    {
        "id": "ep4_c02",
        "display": "もしこの箱 U を、分子ではなく「2倍して15で割った余り」を計算する箱 U_2 に差し替えたらどうなるでしょうか？",
        "tts": "もしこの箱ユーを、分子ではなく、二倍して十五で割った余りを計算する箱、ユーツーに差し替えたらどうなるでしょうか？",
    },
    {
        "id": "ep4_c03",
        "display": "|1⟩ から始めると、1 → 2 → 4 → 8 → 1 と 4ステップ周期 (r = 4) でぐるぐる回ります。",
        "tts": "イチから始めると、イチ、ニ、ヨン、ハチ、イチと、四ステップ周期、アール・イコール・ヨンでぐるぐる回ります。",
    },
    {
        "id": "ep4_c04",
        "display": "このサイクルの固有状態を作ると、1ステップごとに位相が θ = 2πk / r だけ回る「位相の時計」になります！",
        "tts": "このサイクルの固有状態を作ると、一ステップごとに位相が、シータ・イコール・二パイ・ケー割るアールだけ回る、位相の時計になります！",
    },
    {
        "id": "ep4_c05",
        "display": "位相推定で周期 r = 4 を読み出せば、最大公約数 gcd(2^2 ± 1, 15) から 15 = 3 × 5 と一瞬で因数分解できます。これが Shor のアルゴリズムです。",
        "tts": "位相推定で周期四を読み出せば、最大公約数の計算から、十五は三かける五だと、一瞬で因数分解できます。これがショアのアルゴリズムです。",
    },
    {
        "id": "ep4_c06",
        "display": "では、私たちが解きたい課題に出会ったとき、量子で速くなるかをどう見抜けばよいでしょうか？ 4つの分類で整理しましょう。",
        "tts": "では、私たちが解きたい課題に出会ったとき、量子で速くなるかをどう見抜けばよいでしょうか？四つの分類で整理しましょう。",
    },
    {
        "id": "ep4_c07",
        "display": "第1は「量子シミュレーション」。創薬・触媒・電池など、相手自体が量子力学で動く問題は 2^N の壁を直接突破できます。",
        "tts": "第一は、量子シミュレーション。創薬・触媒・電池など、相手自体が量子力学で動く問題は、二のエヌ乗の壁を直接突破できます。",
    },
    {
        "id": "ep4_c08",
        "display": "第2は「周期・代数的構造と大域的干渉」。Shor の因数分解や、2024年に Google が発表した DQI がここに入ります。",
        "tts": "第二は、周期・代数的構造と大域的干渉。ショアの因数分解や、二千二十四年にグーグルが発表したディー・キュー・アイがここに入ります。",
    },
    {
        "id": "ep4_c09",
        "display": "第3は「構造のない探索（Grover）」。√N 回の二次加速が得られますが、誤り訂正のオーバーヘッドには注意が必要です。",
        "tts": "第三は、構造のない探索、グローバー。ルート・エヌ回の二次加速が得られますが、誤り訂正のオーバーヘッドには注意が必要です。",
    },
    {
        "id": "ep4_c10",
        "display": "第4は「古典ビッグデータ処理や逐次計算」。データの読み込み自体がボトルネックになるため、ここは古典GPUの独壇場です。",
        "tts": "第四は、古典ビッグデータ処理や逐次計算。データの読み込み自体がボトルネックになるため、ここは古典ジー・ピー・ユーの独壇場です。",
    },
    {
        "id": "ep4_c11",
        "display": "そして2025年から2026年、Google の Willow チップによる誤り訂正実証や Quantum Echoes、IBM の創薬向けハイブリッド計算など、実用化への扉が開き始めています。",
        "tts": "そして二千二十五年から二千二十六年、グーグルのウィロウ・チップによる誤り訂正実証や、クォンタム・エコーズ、アイ・ビー・エムの創薬向けハイブリッド計算など、実用化への扉が開き始めています。",
    },
    {
        "id": "ep4_c12",
        "display": "「重ね合わせで広げ、位相に答えを刻み、干渉で1点に絞る」——この統一視点こそが、すべての量子アルゴリズムの心臓部です！",
        "tts": "重ね合わせで広げ、位相に答えを刻み、干渉で一点に絞る。この統一視点こそが、すべての量子アルゴリズムの心臓部です！",
    },
]


def run_checks() -> None:
    """Verify Shor's 4-state cycle U_2 on {1, 2, 4, 8} mod 15 and its eigenphases."""
    # Basis order: |1⟩, |2⟩, |4⟩, |8⟩
    # U_2 sends |1⟩->|2⟩, |2⟩->|4⟩, |4⟩->|8⟩, |8⟩->|1⟩
    U2 = np.array(
        [
            [0, 0, 0, 1],
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
        ],
        dtype=complex,
    )

    u_states = []
    for k in range(4):
        vec = (
            np.array(
                [np.exp(-2j * math.pi * k * s / 4.0) for s in range(4)], dtype=complex
            )
            / 2.0
        )
        eigval = np.exp(2j * math.pi * k / 4.0)
        assert np.allclose(U2 @ vec, eigval * vec)
        u_states.append(vec)

    # Verify average of eigenstates equals |1⟩ = [1, 0, 0, 0]
    superpos = sum(u_states) / 2.0
    assert np.allclose(superpos, np.array([1.0, 0.0, 0.0, 0.0], dtype=complex))

    # Verify gcd(2^(4/2) ± 1, 15) gives 3 and 5
    r = 4
    p = math.gcd(2 ** (r // 2) - 1, 15)
    q = math.gcd(2 ** (r // 2) + 1, 15)
    assert {p, q} == {3, 5} and p * q == 15


class Ep4ShorAndFrontierScene(VoicedTeachingScene):
    """Voiced Manim scene for Episode 4: Shor's Factoring, 4-Category Map & 2026 Frontier."""

    def construct(self):
        run_checks()
        self.setup_shell(
            "第4話：Shorの因数分解と量子優位の直感マップ",
            "創薬の時計を「倍々ゲーム」に差し替える (Shorの周期発見)",
        )

        # =====================================================================
        # CHAPTER 1: From Molecular Phase Clock to Shor's Modular Cycle
        # =====================================================================
        self.mark_chapter("創薬の時計を「倍々ゲーム」に差し替える (Shorの周期発見)")

        hero_frame = RoundedRectangle(
            width=5.8,
            height=4.1,
            corner_radius=0.18,
            stroke_color=AMBER,
            stroke_width=2.6,
            fill_color=CARD_BG,
            fill_opacity=0.95,
        ).move_to([-3.55, -0.35, 0])
        hero_caption = text(
            "統一原理：創薬の分子軌道(左)も素因数分解の周期(右)も同じ「位相の時計」",
            16,
            AMBER,
            max_width=5.5,
        ).move_to([-3.55, -2.15, 0])

        if HERO_IMG_PATH.is_file():
            hero_img = ImageMobject(str(HERO_IMG_PATH))
            hero_img.set_width(5.45)
            hero_img.move_to([-3.55, -0.22, 0])
        else:
            hero_img = panel(5.4, 3.2, [-3.55, -0.22, 0])

        cycle_panel = panel(6.6, 4.1, [3.10, -0.35, 0])
        cycle_title = text(
            "N = 15 の素因数分解：U_2 |x⟩ = |2x mod 15⟩", 22, CYAN, max_width=6.2
        ).move_to([3.10, 1.32, 0])

        self.say_cue(
            "ep4_c01",
            "第3話では、分子の時間発展 U(t) が回る角度 θ から創薬の結合エネルギーを読み出しました。",
        )
        self.play(
            FadeIn(hero_frame), FadeIn(hero_img), FadeIn(hero_caption), run_time=1.0
        )
        self.finish_cue("ep4_c01")

        self.say_cue(
            "ep4_c02",
            "もしこの箱 U を、分子ではなく「2倍して15で割った余り」を計算する箱 U_2 に差し替えたらどうなるでしょうか？",
        )
        self.play(FadeIn(cycle_panel), FadeIn(cycle_title), run_time=0.9)
        self.finish_cue("ep4_c02")

        # 4-state cycle diamond inside cycle_panel
        pos_top = np.array([3.10, 0.62, 0.0])
        pos_right = np.array([4.65, -0.38, 0.0])
        pos_bot = np.array([3.10, -1.38, 0.0])
        pos_left = np.array([1.55, -0.38, 0.0])

        node_1 = make_ket_badge(
            "|1⟩", pos_top, color=MINT, width=1.15, height=0.56, font_size=22
        )
        node_2 = make_ket_badge(
            "|2⟩", pos_right, color=BLUE, width=1.15, height=0.56, font_size=22
        )
        node_4 = make_ket_badge(
            "|4⟩", pos_bot, color=AMBER, width=1.15, height=0.56, font_size=22
        )
        node_8 = make_ket_badge(
            "|8⟩", pos_left, color=VIOLET, width=1.15, height=0.56, font_size=22
        )

        arr_12 = Arrow(
            pos_top + RIGHT * 0.62,
            pos_right + UP * 0.32,
            buff=0.08,
            color=SOFT_WHITE,
            stroke_width=3.0,
        )
        arr_24 = Arrow(
            pos_right + DOWN * 0.32,
            pos_bot + RIGHT * 0.62,
            buff=0.08,
            color=SOFT_WHITE,
            stroke_width=3.0,
        )
        arr_48 = Arrow(
            pos_bot + LEFT * 0.62,
            pos_left + DOWN * 0.32,
            buff=0.08,
            color=SOFT_WHITE,
            stroke_width=3.0,
        )
        arr_81 = Arrow(
            pos_left + UP * 0.32,
            pos_top + LEFT * 0.62,
            buff=0.08,
            color=SOFT_WHITE,
            stroke_width=3.0,
        )
        r_center_lbl = code_text("周期 r = 4", 22, AMBER).move_to([3.10, -0.38, 0.0])

        self.say_cue(
            "ep4_c03",
            "|1⟩ から始めると、1 → 2 → 4 → 8 → 1 と 4ステップ周期 (r = 4) でぐるぐる回ります。",
        )
        self.play(
            FadeIn(node_1),
            FadeIn(node_2),
            FadeIn(node_4),
            FadeIn(node_8),
            FadeIn(arr_12),
            FadeIn(arr_24),
            FadeIn(arr_48),
            FadeIn(arr_81),
            FadeIn(r_center_lbl),
            run_time=1.1,
        )
        self.finish_cue("ep4_c03")

        eig_bar = RoundedRectangle(
            width=6.2,
            height=0.55,
            corner_radius=0.10,
            stroke_color=AMBER,
            stroke_width=2.0,
            fill_color=CARD_ALT,
            fill_opacity=0.96,
        ).move_to([3.10, -2.02, 0])
        eig_txt = text(
            "U_2 |u_k⟩ = exp(i 2πk / 4) |u_k⟩  (位相 θ = 2πk / r)",
            18,
            AMBER,
            max_width=5.8,
        ).move_to([3.10, -2.02, 0])

        self.say_cue(
            "ep4_c04",
            "このサイクルの固有状態を作ると、1ステップごとに位相が θ = 2πk / r だけ回る「位相の時計」になります！",
        )
        self.play(FadeIn(eig_bar), FadeIn(eig_txt), run_time=0.9)
        self.finish_cue("ep4_c04")

        gcd_txt = text(
            "r = 4 ⇒ gcd(2^2 − 1, 15) = 3,  gcd(2^2 + 1, 15) = 5 !",
            18,
            MINT,
            max_width=5.8,
        ).move_to([3.10, -2.02, 0])
        self.say_cue(
            "ep4_c05",
            "位相推定で周期 r = 4 を読み出せば、最大公約数 gcd(2^2 ± 1, 15) から 15 = 3 × 5 と一瞬で因数分解できます。これが Shor のアルゴリズムです。",
        )
        self.play(
            Transform(eig_txt, gcd_txt),
            eig_bar.animate.set_stroke(color=MINT),
            run_time=0.9,
        )
        self.finish_cue("ep4_c05")

        self.play(
            FadeOut(hero_frame),
            FadeOut(hero_img),
            FadeOut(hero_caption),
            FadeOut(cycle_panel),
            FadeOut(cycle_title),
            FadeOut(node_1),
            FadeOut(node_2),
            FadeOut(node_4),
            FadeOut(node_8),
            FadeOut(arr_12),
            FadeOut(arr_24),
            FadeOut(arr_48),
            FadeOut(arr_81),
            FadeOut(r_center_lbl),
            FadeOut(eig_bar),
            FadeOut(eig_txt),
            run_time=0.5,
        )

        # =====================================================================
        # CHAPTER 2: The 4-Category Quantum Advantage Intuition Map
        # =====================================================================
        self.mark_chapter("「量子で速くなる問題」を見抜く 4 分類マップ")

        map_intro = text(
            "どんな課題なら量子コンピュータで速くなるのか？ — 4つの質問で見抜く直感マップ",
            22,
            WHITE,
            max_width=12.4,
        ).move_to([0.0, 1.72, 0])

        def make_quadrant(
            center, border_col, badge_str, title_str, desc_str, speed_str
        ):
            card = RoundedRectangle(
                width=6.15,
                height=1.88,
                corner_radius=0.14,
                stroke_color=border_col,
                stroke_width=2.6,
                fill_color=CARD_BG,
                fill_opacity=0.96,
            ).move_to(center)
            b_txt = text(badge_str, 16, border_col, max_width=5.8).move_to(
                [center[0], center[1] + 0.62, 0]
            )
            t_txt = text(title_str, 21, WHITE, max_width=5.8).move_to(
                [center[0], center[1] + 0.18, 0]
            )
            d_txt = text(desc_str, 16, SOFT_WHITE, max_width=5.8).move_to(
                [center[0], center[1] - 0.25, 0]
            )
            s_txt = code_text(speed_str, 17, border_col).move_to(
                [center[0], center[1] - 0.66, 0]
            )
            return VGroup(card, b_txt, t_txt, d_txt, s_txt)

        q_a = make_quadrant(
            [-3.25, 0.42, 0],
            MINT,
            "分類 A ★最有力（指数加速）",
            "量子シミュレーション（創薬・触媒・材料・化学）",
            "対象自体が量子力学で動く問題。2^N の状態空間を N 量子ビットに直載せ",
            "古典 O(2^N)  →  量子 O(poly(N))",
        )
        q_b = make_quadrant(
            [3.25, 0.42, 0],
            CYAN,
            "分類 B ★指数〜超多項式加速",
            "周期・代数的構造・大域的干渉（Shor / BV / DQI）",
            "巨大な重ね合わせの位相に周期や代数構造を刻み、フーリエ変換等で1点集中",
            "古典 指数時間  →  量子 O(poly(n))",
        )
        q_c = make_quadrant(
            [-3.25, -1.68, 0],
            AMBER,
            "分類 C ▲二次加速（条件付き）",
            "構造のない探索・組合せ最適化（Grover 等）",
            "当たり判定オラクルだけで探す問題。誤り訂正の通信・ゲートオーバーヘッドに注意",
            "古典 O(N)  →  量子 O(√N)",
        )
        q_d = make_quadrant(
            [3.25, -1.68, 0],
            RED,
            "分類 D ✕量子優位なし（古典圧勝）",
            "古典ビッグデータ処理・日常業務・逐次計算",
            "巨大な古典データのI/Oがボトルネックになる問題や並列化できない逐次処理",
            "古典 GPU / スパコンが圧倒的に高速",
        )

        self.say_cue(
            "ep4_c06",
            "では、私たちが解きたい課題に出会ったとき、量子で速くなるかをどう見抜けばよいでしょうか？ 4つの分類で整理しましょう。",
        )
        self.play(FadeIn(map_intro), run_time=0.8)
        self.finish_cue("ep4_c06")

        self.say_cue(
            "ep4_c07",
            "第1は「量子シミュレーション」。創薬・触媒・電池など、相手自体が量子力学で動く問題は 2^N の壁を直接突破できます。",
        )
        self.play(FadeIn(q_a), run_time=0.9)
        self.finish_cue("ep4_c07")

        self.say_cue(
            "ep4_c08",
            "第2は「周期・代数的構造と大域的干渉」。Shor の因数分解や、2024年に Google が発表した DQI がここに入ります。",
        )
        self.play(FadeIn(q_b), run_time=0.9)
        self.finish_cue("ep4_c08")

        self.say_cue(
            "ep4_c09",
            "第3は「構造のない探索（Grover）」。√N 回の二次加速が得られますが、誤り訂正のオーバーヘッドには注意が必要です。",
        )
        self.play(FadeIn(q_c), run_time=0.9)
        self.finish_cue("ep4_c09")

        self.say_cue(
            "ep4_c10",
            "第4は「古典ビッグデータ処理や逐次計算」。データの読み込み自体がボトルネックになるため、ここは古典GPUの独壇場です。",
        )
        self.play(FadeIn(q_d), run_time=0.9)
        self.finish_cue("ep4_c10")

        self.play(
            FadeOut(map_intro),
            FadeOut(q_a),
            FadeOut(q_b),
            FadeOut(q_c),
            FadeOut(q_d),
            run_time=0.5,
        )

        # =====================================================================
        # CHAPTER 3: 2025-2026 Frontier & Grand Finale
        # =====================================================================
        self.mark_chapter("2025〜2026年の最前線と量子アルゴリズムの統一視点")

        f_cards = VGroup()
        frontier_specs = [
            (
                -4.25,
                CYAN,
                "Google DQI (2024–2025)",
                "復号化量子干渉法",
                "代数的構造（誤り訂正復号）を位相干渉に\n変換し、最適化問題で古典を超える！",
            ),
            (
                0.0,
                MINT,
                "Google Willow & Echoes (2025)",
                "閾値下誤り訂正 ＆ OTOC 干渉",
                "量子ビットを増やすほどエラーが減る実証と\n分子分光(NMR)に繋がる量子エコー観測！",
            ),
            (
                4.25,
                AMBER,
                "IBM × 理研 創薬・化学 (2025–2026)",
                "量子中心スーパーコンピューティング",
                "量子プロセッサとスパコン「富岳」を密結合し\n鉄硫黄クラスター等の強相関分子を計算！",
            ),
        ]
        for cx, col, tag, head, body in frontier_specs:
            c_box = RoundedRectangle(
                width=4.0,
                height=2.65,
                corner_radius=0.14,
                stroke_color=col,
                stroke_width=2.5,
                fill_color=CARD_BG,
                fill_opacity=0.96,
            ).move_to([cx, 0.55, 0])
            t1 = text(tag, 17, col, max_width=3.65).move_to([cx, 1.48, 0])
            t2 = text(head, 20, WHITE, max_width=3.65).move_to([cx, 0.96, 0])
            t3 = (
                VGroup(
                    *(
                        text(line, 16, SOFT_WHITE, max_width=3.65)
                        for line in body.split("\n")
                    )
                )
                .arrange(DOWN, buff=0.14)
                .move_to([cx, 0.02, 0])
            )
            f_cards.add(VGroup(c_box, t1, t2, t3))

        self.say_cue(
            "ep4_c11",
            "そして2025年から2026年、Google の Willow チップによる誤り訂正実証や Quantum Echoes、IBM の創薬向けハイブリッド計算など、実用化への扉が開き始めています。",
        )
        self.play(
            FadeIn(f_cards[0]), FadeIn(f_cards[1]), FadeIn(f_cards[2]), run_time=1.1
        )
        self.finish_cue("ep4_c11")

        finale_banner = RoundedRectangle(
            width=12.5,
            height=1.35,
            corner_radius=0.16,
            stroke_color=MINT,
            stroke_width=3.0,
            fill_color="#064E3B",
            fill_opacity=0.95,
        ).move_to([0.0, -1.78, 0])
        finale_t1 = text(
            "量子アルゴリズムの黄金律：① 重ね合わせで広げ → ② 位相に答えを刻み → ③ 干渉で1点に絞る",
            22,
            MINT,
            max_width=12.0,
        ).move_to([0.0, -1.52, 0])
        finale_t2 = text(
            "Deutsch / Bernstein–Vazirani / 創薬の位相推定 / Shor / DQI —— すべてはこの1本の幹で繋がっている！",
            18,
            WHITE,
            max_width=12.0,
        ).move_to([0.0, -2.04, 0])

        self.say_cue(
            "ep4_c12",
            "「重ね合わせで広げ、位相に答えを刻み、干渉で1点に絞る」——この統一視点こそが、すべての量子アルゴリズムの心臓部です！",
        )
        self.play(
            FadeIn(finale_banner), FadeIn(finale_t1), FadeIn(finale_t2), run_time=1.0
        )
        self.finish_cue("ep4_c12", extra_pad=0.9)
