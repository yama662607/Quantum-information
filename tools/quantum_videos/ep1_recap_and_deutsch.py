"""Episode 1: 量子回路の読み方と、素朴な回路が失敗する理由（Deutschの必然）"""

from __future__ import annotations

import numpy as np
from manim import (
    LEFT,
    UP,
    Create,
    FadeIn,
    Line,
    RoundedRectangle,
    Transform,
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
    VoicedTeachingScene,
    make_gate_box,
    make_heatmap_2x2,
    make_ket_badge,
    make_meter_box,
    make_wide_gate_box,
)

# ---------------------------------------------------------------------------
# Mathematical verification of all states & matrices shown in Episode 1
# ---------------------------------------------------------------------------


def run_checks() -> None:
    H = np.array([[1, 1], [1, -1]], dtype=float) / np.sqrt(2)
    X = np.array([[0, 1], [1, 0]], dtype=float)
    Z = np.array([[1, 0], [0, -1]], dtype=float)
    I2 = np.eye(2)
    ket0 = np.array([1.0, 0.0])
    ket1 = np.array([0.0, 1.0])
    ket_plus = H @ ket0
    ket_minus = H @ ket1

    # 1. H Z H |0> = X |0> = |1>
    assert np.allclose(H @ Z @ H @ ket0, ket1)
    # 2. Eigenstate X |-> = -|->
    assert np.allclose(X @ ket_minus, -ket_minus)
    # 3. Naive circuit on f(a)=a (CNOT): (H x I) CNOT (H x I) |00>
    CNOT = np.array(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
        ],
        dtype=float,
    )
    psi_bell = CNOT @ np.kron(ket_plus, ket0)
    psi_naive_out = np.kron(H, I2) @ psi_bell
    assert np.allclose(psi_naive_out, np.array([0.5, 0.5, 0.5, -0.5]))
    # Partial trace over b of |Phi+><Phi+| is 0.5 * I_2 (zero off-diagonal!)
    rho_bell = np.outer(psi_bell, psi_bell)
    rho_a = rho_bell.reshape(2, 2, 2, 2).trace(axis1=1, axis2=3)
    assert np.allclose(rho_a, 0.5 * I2)


CUES_EP1 = [
    {
        "id": "ep1_c01",
        "display": "第2回ゼミへようこそ！まずは前回の復習から始めましょう。\n量子回路は左から右へ時間を追い、箱（ゲート）で状態を変換します。",
        "tts": "第二回ゼミへようこそ！まずは前回の復習から始めましょう。りょうし回路は、左から右へ時間を追い、箱で表されるゲートで状態を変換していきます。",
    },
    {
        "id": "ep1_c02",
        "display": "基本の部品は3つです。Xゲートは |0⟩ と |1⟩ を入れ替え、\nHゲートは 0 と 1 の均等な重ね合わせ |+⟩ を作ります。",
        "tts": "基本の部品は三つです。エックスゲートは、ゼロとイチを入れ替え、エイチゲートは、ゼロとイチの均等な重ね合わせ、プラス状態を作ります。",
    },
    {
        "id": "ep1_c03",
        "display": "そこへ Zゲートで |1⟩ の符号だけをマイナスに反転させて |−⟩ にし、\nもう一度 Hゲートを掛けると、波の干渉が起きます！",
        "tts": "そこへゼットゲートで、イチの符号だけをマイナスに反転させてマイナス状態にし、もう一度エイチゲートを掛けると、波の干渉が起きます！",
    },
    {
        "id": "ep1_c04",
        "display": "|0⟩ へ向かう2つの経路がプラスとマイナスで打ち消し合い、\n|1⟩ だけが強め合って確率 100% で現れます。これが量子干渉です。",
        "tts": "ゼロへ向かう二つの経路がプラスとマイナスで打ち消しあい、イチだけが強めあって、確率百パーセントで現れます。これが量子干渉です。",
    },
    {
        "id": "ep1_c05",
        "display": "では、ブラックボックス関数 f(0) と f(1) が「同じか違うか」を\n1回で見分ける回路はどう作ればよいでしょうか？",
        "tts": "では、ブラックボックスの関数、エフゼロとエフイチが、同じか違うかを一回で見分ける回路は、どう作ればよいでしょうか？",
    },
    {
        "id": "ep1_c06",
        "display": "誰もが最初に試したくなるのが、下を |0⟩ のままにして、\n上だけを H → Uf → H で挟む「素朴な回路」です。",
        "tts": "誰もが最初に試したくなるのが、下の量子ビットをゼロのままにして、上だけをエイチ、ユーエフ、エイチで挟む、素朴な回路です。",
    },
    {
        "id": "ep1_c07",
        "display": "ところが f(0)≠f(1) のとき、Uf を通ると下のビットが |0⟩ と |1⟩ に分裂し、\n(|00⟩ + |11⟩)/√2 というエンタングル状態になってしまいます！",
        "tts": "ところが、エフゼロとエフイチが違うとき、ユーエフを通ると、下の量子ビットがゼロとイチに分かれて、ゼロゼロとイチイチのエンタングル状態になってしまいます！",
    },
    {
        "id": "ep1_c08",
        "display": "すると最後のHを掛けても、「下が0の部屋」と「下が1の部屋」に分かれているため、\nプラスとマイナスが干渉できず、測定確率は 50% ずつのコイントスに潰れます。",
        "tts": "すると最後のエイチを掛けても、下がゼロの部屋と下がイチの部屋に分かれているため、プラスとマイナスが干渉できず、測定確率は五十パーセントずつのコイントスに潰れてしまいます。",
    },
    {
        "id": "ep1_c09",
        "display": "第2・3章の密度行列で見ると、原因が一目でわかります。\n干渉を起こす力は、行列の右上と左下の「非対角成分」にあります。",
        "tts": "教科書の第二章・第三章で学んだ密度行列で見ると、原因が一目でわかります。干渉を起こす力は、行列の右上と左下の、非対角成分にあります。",
    },
    {
        "id": "ep1_c10",
        "display": "素朴な回路で下のビットを無視（部分トレース）すると、直交する |0⟩ と |1⟩ の\n内積が 0 になるため、非対角成分が完全に消滅してしまうのです！",
        "tts": "素朴な回路で下のビットを部分トレースすると、直交するゼロとイチの内積がゼロになるため、非対角成分が完全に消滅してしまうのです！",
    },
    {
        "id": "ep1_c11",
        "display": "失敗の原因がわかれば、解決策はただ1つです！\n下に X が掛かっても「状態の形が変わらず、符号だけが出る状態」を置けばよいのです。",
        "tts": "失敗の原因がわかれば、解決策はただ一つです！下にエックスが掛かっても、状態の形が変わらず、符号だけが出る状態を置けばよいのです。",
    },
    {
        "id": "ep1_c12",
        "display": "それが固有状態 |−⟩ = (|0⟩−|1⟩)/√2 です！\n|−⟩ に X を掛けると、0と1が入れ替わってちょうど −|−⟩ になります。",
        "tts": "それが固有状態、マイナス状態です！マイナス状態にエックスを掛けると、ゼロとイチが入れ替わって、ちょうどマイナス一倍のマイナス状態になります。",
    },
    {
        "id": "ep1_c13",
        "display": "下を |−⟩ にしておけば、Uf を通っても下は |−⟩ のまま共通にくくり出せて、\n関数値に応じた符号 (−1)^f(a) だけが上の量子ビットへ跳ね返ります！",
        "tts": "下をマイナス状態にしておけば、ユーエフを通っても下はマイナス状態のまま共通にくくり出せて、関数に応じた符号だけが上の量子ビットへ跳ね返ります！",
    },
    {
        "id": "ep1_c14",
        "display": "これが「位相キックバック」です。こじつけのトリックではなく、\nエンタングルによる干渉の消滅を防ぐための必然の設計だったのです。",
        "tts": "これが位相キックバックです。決してこじつけのトリックではなく、エンタングルによる干渉の消滅を防ぐための、必然の設計だったのです。",
    },
    {
        "id": "ep1_c15",
        "display": "最後に上のHで干渉させれば、同じ関数なら必ず 0、違う関数なら必ず 1 が出ます。\nこの基本パーツを使って、次は100万桁の秘密の鍵を1回で抜いてみましょう！",
        "tts": "最後に上のエイチで干渉させれば、同じ関数なら必ずゼロ、違う関数なら必ずイチが出ます。この基本パーツを使って、次は百万桁の秘密の鍵を一回で抜いてみましょう！",
    },
]


class Ep1RecapAndDeutsch(VoicedTeachingScene):
    def construct(self):
        run_checks()
        self.start_lesson(
            "第1回復習 ＆ 第2回導入",
            "量子回路の読み方と、Deutsch回路が生まれた必然の理由",
        )

        # ===================================================================
        # Chapter 1: 量子回路の読み方と3つの基本ゲート (X, Z, H)
        # ===================================================================
        self.chapter("01  量子回路の読み方と、3つの基本ゲート（X・Z・H）")

        left_card = panel(6.8, 4.3, [-3.3, -0.35, 0])
        right_card = panel(6.4, 4.3, [3.5, -0.35, 0])
        left_title = text("量子回路：左から右へゲートを通す", 22, BLUE).move_to(
            [-3.3, 1.38, 0]
        )
        right_title = text("状態ベクトルの振幅（プラスとマイナス）", 22, AMBER).move_to(
            [3.5, 1.38, 0]
        )

        wire = Line(
            [-5.8, -0.35, 0], [-0.8, -0.35, 0], stroke_color=WHITE, stroke_width=3.2
        )
        in_ket = make_ket_badge(
            "|0⟩", [-6.0, -0.35, 0], color=BLUE, width=1.0, height=0.62
        )
        g_h1 = make_gate_box("H", [-4.4, -0.35, 0], color=BLUE)
        g_z = make_gate_box("Z", [-3.1, -0.35, 0], color=RED)
        g_h2 = make_gate_box("H", [-1.8, -0.35, 0], color=BLUE)

        # Right side amplitude bar chart axes
        zero_line = Line(
            [1.1, -0.55, 0], [5.9, -0.55, 0], stroke_color=GRID, stroke_width=2.0
        )
        lbl_ket0 = text("|0⟩ の振幅", 20, WHITE).move_to([2.4, -2.1, 0])
        lbl_ket1 = text("|1⟩ の振幅", 20, WHITE).move_to([4.6, -2.1, 0])

        bar0 = RoundedRectangle(
            width=1.1,
            height=1.25,
            corner_radius=0.08,
            stroke_color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.88,
        )
        bar0.move_to([2.4, -0.55 + 0.625, 0])
        val0 = code_text("+1.00", 21, BLUE).move_to([2.4, -0.55 + 1.48, 0])

        bar1 = RoundedRectangle(
            width=1.1,
            height=0.06,
            corner_radius=0.03,
            stroke_color=MUTED,
            fill_color=MUTED,
            fill_opacity=0.6,
        )
        bar1.move_to([4.6, -0.55 + 0.03, 0])
        val1 = code_text("0.00", 21, MUTED).move_to([4.6, -0.55 + 0.32, 0])

        state_formula = text("現在の状態： |0⟩", 24, MINT).move_to([-3.3, -1.65, 0])

        self.say_cue("ep1_c01", CUES_EP1[0]["display"])
        self.play(
            FadeIn(left_card),
            FadeIn(right_card),
            FadeIn(left_title),
            FadeIn(right_title),
            Create(wire),
            FadeIn(in_ket),
            Create(zero_line),
            FadeIn(lbl_ket0),
            FadeIn(lbl_ket1),
            FadeIn(bar0),
            FadeIn(val0),
            FadeIn(bar1),
            FadeIn(val1),
            FadeIn(state_formula),
            run_time=1.4,
        )
        self.finish_cue("ep1_c01")

        # Cue 2: H gate creates |+>
        self.say_cue("ep1_c02", CUES_EP1[1]["display"])
        bar0_plus = RoundedRectangle(
            width=1.1,
            height=1.06,
            corner_radius=0.08,
            stroke_color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.88,
        ).move_to([2.4, -0.55 + 0.53, 0])
        bar1_plus = RoundedRectangle(
            width=1.1,
            height=1.06,
            corner_radius=0.08,
            stroke_color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.88,
        ).move_to([4.6, -0.55 + 0.53, 0])
        val0_plus = code_text("+0.71", 22, BLUE).move_to([2.4, -0.55 + 1.28, 0])
        val1_plus = code_text("+0.71", 22, BLUE).move_to([4.6, -0.55 + 1.28, 0])
        formula_plus = text("H を通過： |+⟩ = (|0⟩ + |1⟩) / √2", 24, MINT).move_to(
            [-3.3, -1.65, 0]
        )

        self.play(
            FadeIn(g_h1, scale=0.85),
            Transform(bar0, bar0_plus),
            Transform(val0, val0_plus),
            Transform(bar1, bar1_plus),
            Transform(val1, val1_plus),
            Transform(state_formula, formula_plus),
            run_time=1.5,
        )
        self.finish_cue("ep1_c02")

        # Cue 3: Z gate flips |1> phase to negative -> |->
        self.say_cue("ep1_c03", CUES_EP1[2]["display"])
        bar1_minus = RoundedRectangle(
            width=1.1,
            height=1.06,
            corner_radius=0.08,
            stroke_color=RED,
            fill_color=RED,
            fill_opacity=0.88,
        ).move_to([4.6, -0.55 - 0.53, 0])
        val1_minus = code_text("-0.71", 22, RED).move_to([4.6, -0.55 - 1.28, 0])
        formula_minus = text("Z を通過： |−⟩ = (|0⟩ − |1⟩) / √2", 24, RED).move_to(
            [-3.3, -1.65, 0]
        )

        self.play(
            FadeIn(g_z, scale=0.85),
            Transform(bar1, bar1_minus),
            Transform(val1, val1_minus),
            Transform(state_formula, formula_minus),
            run_time=1.5,
        )
        self.finish_cue("ep1_c03")

        # Cue 4: Second H gate interferes -> |1> with 100%
        self.say_cue("ep1_c04", CUES_EP1[3]["display"])
        bar0_final = RoundedRectangle(
            width=1.1,
            height=0.06,
            corner_radius=0.03,
            stroke_color=MUTED,
            fill_color=MUTED,
            fill_opacity=0.6,
        ).move_to([2.4, -0.55 + 0.03, 0])
        val0_final = code_text("0 (相殺!)", 20, MUTED).move_to([2.4, -0.55 + 0.35, 0])
        bar1_final = RoundedRectangle(
            width=1.1,
            height=1.25,
            corner_radius=0.08,
            stroke_color=AMBER,
            fill_color=AMBER,
            fill_opacity=0.92,
        ).move_to([4.6, -0.55 + 0.625, 0])
        val1_final = code_text("+1.00 (100%!)", 20, AMBER).move_to(
            [4.6, -0.55 + 1.48, 0]
        )
        formula_final = text(
            "HZH |0⟩ = |1⟩ （干渉で |0⟩ が消え |1⟩ に集中！）", 21, AMBER, max_width=6.2
        ).move_to([-3.3, -1.65, 0])

        self.play(
            FadeIn(g_h2, scale=0.85),
            Transform(bar0, bar0_final),
            Transform(val0, val0_final),
            Transform(bar1, bar1_final),
            Transform(val1, val1_final),
            Transform(state_formula, formula_final),
            run_time=1.6,
        )
        self.finish_cue("ep1_c04")

        # ===================================================================
        # Chapter 2: 誰もが最初に試す「素朴な回路」の罠
        # ===================================================================
        self.clear_diagram()
        self.chapter("02  誰もが最初に試す「素朴な回路」は、なぜ失敗するのか？")

        c_panel = panel(13.4, 4.35, [0, -0.35, 0])
        c_title = text(
            "素朴な回路：下の量子ビット b を |0⟩ のままにしたら？", 23, AMBER
        ).move_to([0, 1.42, 0])

        y_a, y_b = 0.45, -1.05
        wire_a = Line(
            [-5.5, y_a, 0], [0.4, y_a, 0], stroke_color=WHITE, stroke_width=3.0
        )
        wire_b = Line(
            [-5.5, y_b, 0], [0.4, y_b, 0], stroke_color=WHITE, stroke_width=3.0
        )
        ket_a0 = make_ket_badge(
            "上 a: |0⟩",
            [-5.8, y_a, 0],
            color=BLUE,
            width=1.45,
            height=0.58,
            font_size=21,
        )
        ket_b0 = make_ket_badge(
            "下 b: |0⟩",
            [-5.8, y_b, 0],
            color=MUTED,
            width=1.45,
            height=0.58,
            font_size=21,
        )

        naive_h1 = make_gate_box("H", [-4.0, y_a, 0], color=BLUE, size=0.78)
        naive_uf = make_wide_gate_box(
            "Uf", "f(a)=a", [-2.4, -0.3, 0], color=AMBER, width=1.35, height=2.25
        )
        naive_h2 = make_gate_box("H", [-0.8, y_a, 0], color=BLUE, size=0.78)
        naive_meter = make_meter_box([0.4, y_a, 0], size=0.76)

        self.say_cue("ep1_c05", CUES_EP1[4]["display"])
        self.play(
            FadeIn(c_panel),
            FadeIn(c_title),
            Create(wire_a),
            Create(wire_b),
            FadeIn(ket_a0),
            FadeIn(ket_b0),
            FadeIn(naive_uf),
            run_time=1.3,
        )
        self.finish_cue("ep1_c05")

        self.say_cue("ep1_c06", CUES_EP1[5]["display"])
        self.play(
            FadeIn(naive_h1, scale=0.85),
            FadeIn(naive_h2, scale=0.85),
            FadeIn(naive_meter),
            run_time=1.2,
        )
        self.finish_cue("ep1_c06")

        # Show entanglement splitting into two rooms on the right side
        room0_box = RoundedRectangle(
            width=5.4,
            height=1.55,
            corner_radius=0.12,
            stroke_color=BLUE,
            stroke_width=2.0,
            fill_color=CARD_ALT,
            fill_opacity=0.95,
        ).move_to([3.65, 0.38, 0])
        room1_box = RoundedRectangle(
            width=5.4,
            height=1.55,
            corner_radius=0.12,
            stroke_color=PINK,
            stroke_width=2.0,
            fill_color=CARD_ALT,
            fill_opacity=0.95,
        ).move_to([3.65, -1.35, 0])
        room0_txt = text(
            "下が |0⟩ の部屋： a=0 の経路 → |0, 0⟩", 19, BLUE, max_width=5.0
        ).move_to([3.65, 0.62, 0])
        room1_txt = text(
            "下が |1⟩ の部屋： a=1 の経路 → |1, 1⟩", 19, PINK, max_width=5.0
        ).move_to([3.65, -1.11, 0])

        self.say_cue("ep1_c07", CUES_EP1[6]["display"])
        self.play(
            FadeIn(room0_box),
            FadeIn(room0_txt),
            FadeIn(room1_box),
            FadeIn(room1_txt),
            run_time=1.4,
        )
        self.finish_cue("ep1_c07")

        # Show why the final H cannot cancel +|10> and -|11>
        room0_after = text("最後のH後： +1/2 |00⟩  +1/2 |10⟩", 20, WHITE).move_to(
            [3.65, 0.10, 0]
        )
        room1_after = text("最後のH後： +1/2 |01⟩  −1/2 |11⟩", 20, RED).move_to(
            [3.65, -1.63, 0]
        )
        no_cancel_badge = make_ket_badge(
            "別々の部屋なので +1/2 と −1/2 が相殺できない！ → 確率 50% : 50%",
            [-2.6, -2.02, 0],
            color=RED,
            width=7.2,
            height=0.58,
            font_size=19,
        )

        self.say_cue("ep1_c08", CUES_EP1[7]["display"])
        self.play(
            FadeIn(room0_after),
            FadeIn(room1_after),
            FadeIn(no_cancel_badge),
            run_time=1.4,
        )
        self.finish_cue("ep1_c08")

        # ===================================================================
        # Chapter 3: 密度行列と部分トレースで見る「干渉の消滅」
        # ===================================================================
        self.clear_diagram()
        self.chapter("03  密度行列と部分トレースで見る「干渉の消滅」")

        hm1 = make_heatmap_2x2(
            [[0.5, 0.5], [0.5, 0.5]],
            [-4.5, -0.35, 0],
            "① 純粋な |+⟩⟨+|",
            "非対角 +0.5 → Hで 0 に干渉!",
            MINT,
        )
        hm2 = make_heatmap_2x2(
            [[0.5, -0.5], [-0.5, 0.5]],
            [0.0, -0.35, 0],
            "② 純粋な |−⟩⟨−|",
            "非対角 −0.5 → Hで 1 に干渉!",
            RED,
        )
        hm3 = make_heatmap_2x2(
            [[0.5, 0.0], [0.0, 0.5]],
            [4.5, -0.35, 0],
            "③ 素朴な回路 tr_b(|Φ+⟩⟨Φ+|)",
            "非対角 0.0 → 干渉が完全消滅!",
            AMBER,
        )

        self.say_cue("ep1_c09", CUES_EP1[8]["display"])
        self.play(FadeIn(hm1), FadeIn(hm2), run_time=1.4)
        self.finish_cue("ep1_c09")

        self.say_cue("ep1_c10", CUES_EP1[9]["display"])
        self.play(FadeIn(hm3, shift=LEFT * 0.2), run_time=1.4)
        self.finish_cue("ep1_c10")

        # ===================================================================
        # Chapter 4: 逆転の発想：固有状態 |−⟩ と位相キックバック
        # ===================================================================
        self.clear_diagram()
        self.chapter("04  逆転の発想：固有状態 |−⟩ と位相キックバック")

        eig_card = panel(13.2, 1.85, [0, 0.95, 0])
        eig_title = text(
            "解決のカギ：X を掛けても「形が変わらず、マイナスの符号だけが出る状態」",
            21,
            AMBER,
        ).move_to([0, 1.42, 0])
        eig_eq = text(
            "X |−⟩  =  X (|0⟩ − |1⟩)/√2  =  (|1⟩ − |0⟩)/√2  =  (−1) |−⟩ !", 25, MINT
        ).move_to([0, 0.65, 0])

        self.say_cue("ep1_c11", CUES_EP1[10]["display"])
        self.play(FadeIn(eig_card), FadeIn(eig_title), run_time=1.1)
        self.finish_cue("ep1_c11")

        self.say_cue("ep1_c12", CUES_EP1[11]["display"])
        self.play(FadeIn(eig_eq, shift=UP * 0.1), run_time=1.2)
        self.finish_cue("ep1_c12")

        # Show kickback mechanism box below
        kb_card = panel(13.2, 2.35, [0, -1.42, 0])
        kb_line1 = text("下を |−⟩_b に固定して Uf に通すと…", 21, BLUE).move_to(
            [0, -0.62, 0]
        )
        kb_line2 = text(
            "Uf ( |+⟩_a ⊗ |−⟩_b )  =  [ (−1)^f(0) |0⟩_a + (−1)^f(1) |1⟩_a ] / √2  ⊗  |−⟩_b",
            23,
            WHITE,
        ).move_to([0, -1.28, 0])
        kb_line3 = text(
            "下の |−⟩_b は両経路でまったく同じ！ → 右側に共通にくくり出せて、上で 100% 干渉できる！",
            20,
            AMBER,
        ).move_to([0, -1.98, 0])

        self.say_cue("ep1_c13", CUES_EP1[12]["display"])
        self.play(FadeIn(kb_card), FadeIn(kb_line1), FadeIn(kb_line2), run_time=1.3)
        self.finish_cue("ep1_c13")

        self.say_cue("ep1_c14", CUES_EP1[13]["display"])
        self.play(FadeIn(kb_line3), run_time=1.1)
        self.finish_cue("ep1_c14")

        # ===================================================================
        # Chapter 5: Deutschの回路の完成
        # ===================================================================
        self.clear_diagram()
        self.chapter("05  完成した Deutsch の回路：1回の質問で100%判定！")

        d_card = panel(13.4, 4.35, [0, -0.35, 0])
        d_title = text(
            "完成した Deutsch 回路：下の最初に X → H を足して |−⟩ を作るだけ！",
            23,
            MINT,
        ).move_to([0, 1.42, 0])

        ya, yb = 0.42, -1.12
        wa = Line([-5.2, ya, 0], [0.2, ya, 0], stroke_color=WHITE, stroke_width=3.0)
        wb = Line([-5.2, yb, 0], [0.2, yb, 0], stroke_color=WHITE, stroke_width=3.0)
        ka = make_ket_badge(
            "上 a: |0⟩",
            [-5.65, ya, 0],
            color=BLUE,
            width=1.35,
            height=0.56,
            font_size=20,
        )
        kb = make_ket_badge(
            "下 b: |0⟩",
            [-5.65, yb, 0],
            color=MINT,
            width=1.35,
            height=0.56,
            font_size=20,
        )

        gx_b = make_gate_box("X", [-4.3, yb, 0], color=MINT, size=0.74, font_size=24)
        gh_a1 = make_gate_box("H", [-3.2, ya, 0], color=BLUE, size=0.74, font_size=24)
        gh_b1 = make_gate_box("H", [-3.2, yb, 0], color=MINT, size=0.74, font_size=24)
        g_uf = make_wide_gate_box(
            "Uf", "1回だけ!", [-1.8, -0.35, 0], color=AMBER, width=1.35, height=2.25
        )
        gh_a2 = make_gate_box("H", [-0.4, ya, 0], color=BLUE, size=0.74, font_size=24)
        meter_a = make_meter_box([0.55, ya, 0], size=0.74)

        res_const = RoundedRectangle(
            width=4.8,
            height=1.45,
            corner_radius=0.12,
            stroke_color=BLUE,
            stroke_width=2.2,
            fill_color=CARD_ALT,
            fill_opacity=0.95,
        ).move_to([3.95, 0.35, 0])
        res_bal = RoundedRectangle(
            width=4.8,
            height=1.45,
            corner_radius=0.12,
            stroke_color=RED,
            stroke_width=2.2,
            fill_color=CARD_ALT,
            fill_opacity=0.95,
        ).move_to([3.95, -1.35, 0])
        txt_const = text(
            "f(0) = f(1)（同じ・定数）\n→ 上は ±|+⟩ → Hで 0 が確率 100%！", 19, BLUE
        ).move_to([3.95, 0.35, 0])
        txt_bal = text(
            "f(0) ≠ f(1)（違う・均衡）\n→ 上は ±|−⟩ → Hで 1 が確率 100%！", 19, RED
        ).move_to([3.95, -1.35, 0])

        self.say_cue("ep1_c15", CUES_EP1[14]["display"])
        self.play(
            FadeIn(d_card),
            FadeIn(d_title),
            Create(wa),
            Create(wb),
            FadeIn(ka),
            FadeIn(kb),
            FadeIn(gx_b),
            FadeIn(gh_a1),
            FadeIn(gh_b1),
            FadeIn(g_uf),
            FadeIn(gh_a2),
            FadeIn(meter_a),
            FadeIn(res_const),
            FadeIn(txt_const),
            FadeIn(res_bal),
            FadeIn(txt_bal),
            run_time=1.8,
        )
        self.finish_cue("ep1_c15", extra_pad=0.8)


if __name__ == "__main__":
    run_checks()
    print("Episode 1 mathematical checks passed!")
