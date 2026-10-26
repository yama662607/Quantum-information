"""Episode 2: 隠れたパリティを1回の問い合わせで特定（Bernstein–Vazirani）"""

from __future__ import annotations

import numpy as np
from manim import (
    RIGHT,
    Create,
    DashedLine,
    FadeIn,
    Line,
    RoundedRectangle,
    Transform,
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
    code_text,
    panel,
    text,
)
from quantum_videos.voiced_engine import (
    VoicedTeachingScene,
    make_cnot_symbol,
    make_gate_box,
    make_ket_badge,
)


def run_checks() -> None:
    H = np.array([[1, 1], [1, -1]], dtype=float) / np.sqrt(2)
    Z = np.array([[1, 0], [0, -1]], dtype=float)
    ket0 = np.array([1.0, 0.0])
    ket1 = np.array([0.0, 1.0])
    ket_plus = H @ ket0
    ket_minus = H @ ket1

    # 1. CNOT (|+> x |->) = |-> x |-> = (Z|+>) x |->
    CNOT = np.array(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
        ],
        dtype=float,
    )
    lhs = CNOT @ np.kron(ket_plus, ket_minus)
    rhs = np.kron(Z @ ket_plus, ket_minus)
    assert np.allclose(lhs, rhs)
    assert np.allclose(lhs, np.kron(ket_minus, ket_minus))

    # 2. BV for n=3, s=101: after oracle, top state is |->|+>|->, after H^3 it is |101>
    top_after_oracle = np.kron(np.kron(ket_minus, ket_plus), ket_minus)
    H3 = np.kron(np.kron(H, H), H)
    out_state = H3 @ top_after_oracle
    expected = np.zeros(8)
    expected[int("101", 2)] = 1.0
    assert np.allclose(out_state, expected)


CUES_EP2 = [
    {
        "id": "ep2_c01",
        "display": "Deutschの回路では「2回を1回」に減らしました。\nでは、これを n 本の量子ビットに広げたら、どれだけ劇的に速くなるでしょうか？",
        "tts": "ドイッチュの回路では、二回を一回に減らしました。では、これをエヌ本の量子ビットに広げたら、どれだけ劇的に速くなるでしょうか？",
    },
    {
        "id": "ep2_c02",
        "display": "本題に入る前に、たった1つの準備パズルを解いておきましょう。\n下のターゲットを |−⟩ に固定した CNOT ゲートは、上に何をするでしょうか？",
        "tts": "本題に入る前に、たった一つの準備パズルを解いておきましょう。下のターゲットをマイナス状態に固定したシーノットゲートは、上の量子ビットに何をするでしょうか？",
    },
    {
        "id": "ep2_c03",
        "display": "上が |0⟩ なら何も起きず、上が |1⟩ なら下に X が掛かって −1 が飛び出します。\nつまり、上の量子ビットに Z ゲートを掛けたのと同じになります！",
        "tts": "上がゼロなら何も起きず、上がイチなら下にエックスが掛かってマイナス一が飛び出します。つまり、上の量子ビットにゼットゲートを掛けたのと、まったく同じになります！",
    },
    {
        "id": "ep2_c04",
        "display": "だから、上が |+⟩ のときにこの CNOT を通すと、\n下は |−⟩ のまま変わらず、上だけが |+⟩ から |−⟩ に反転します！",
        "tts": "だから、上がプラス状態のときにこのシーノットを通すと、下はマイナス状態のまま変わらず、上だけがプラスからマイナスに反転します！",
    },
    {
        "id": "ep2_c05",
        "display": "s=101 のパリティ関数 f_s(x)=s・x mod 2 を考えます。入力 100, 010, 001 への答えは 1, 0, 1 です。",
        "tts": "箱には、秘密のビット列が隠されています。入力との積の和を計算し、二で割った余りを返します。これがパリティ関数です。図の例では、一番上と一番下の桁が選ばれています。",
    },
    {
        "id": "ep2_c06",
        "display": "古典コンピュータでは、1回の質問で1ビットしか返ってこないため、\n100、010、001 と1桁ずつ調べるのに必ず n 回の質問が必要です。",
        "tts": "古典的には、一つの桁だけを一にした入力で、その桁の秘密を調べます。一回に一ビットずつ、全てを確実に知るには、桁数と同じ回数の質問が必要です。",
    },
    {
        "id": "ep2_c07",
        "display": "ところが箱の中身を回路で見ると、秘密の鍵 s の桁が 1 である\na2 と a0 の線からだけ、下の b へ CNOT が繋がっています。",
        "tts": "ところが、箱の中身を回路で見ると、秘密の鍵エスの桁がイチである、エーツーとエーゼロの線からだけ、下のビーへシーノットが繋がっています。",
    },
    {
        "id": "ep2_c08",
        "display": "そこで上の3本をすべて |+⟩、下の b を |−⟩ にして箱を1回だけ通すと…\nCNOT がある a2 と a0 だけが |−⟩ に反転し、a1 は |+⟩ のまま残ります！",
        "tts": "そこで、上の三本をすべてプラス状態、下のビーをマイナス状態にして、箱を一回だけ通すと、シーノットがあるエーツーとエーゼロだけがマイナスに反転し、エーワンはプラスのまま残ります！",
    },
    {
        "id": "ep2_c09",
        "display": "あとは最後に上の3本すべてに H を掛けるだけです！\n|−⟩ は |1⟩ に、|+⟩ は |0⟩ になり、1回の測定で秘密の鍵 101 がそのまま出ます！",
        "tts": "最後に、上の三本の線に、エイチゲートをかけます。マイナス状態は一に、プラス状態はゼロに変わります。図の例では、上から順に、一、ゼロ、一が出ます。",
    },
    {
        "id": "ep2_c10",
        "display": "コヒーレントなパリティ・オラクルなら、量子は問い合わせ 1 回。n+1 量子ビットと O(n) 個の周辺ゲートも必要です。",
        "tts": "コヒーレントなパリティオラクルを使えるとき、量子は問い合わせ一回で済みます。ただし、エヌ足す一個の量子ビットと、エヌに比例する数の周辺ゲートも必要です。",
    },
    {
        "id": "ep2_c11",
        "display": "これが Bernstein–Vazirani のアルゴリズムです。\n次は、この「位相の転写」が創薬の分子エネルギー計算でどう活躍するかを見ていきましょう！",
        "tts": "これがベルンシュタイン・ヴァジラニのアルゴリズムです。次は、この位相の転写が、創薬の分子エネルギー計算でどう活躍するかを見ていきましょう！",
    },
]


class Ep2SecretKeyBV(VoicedTeachingScene):
    def construct(self):
        run_checks()
        self.start_lesson(
            "第2回 セクション2",
            "隠れたパリティ：古典 n 回、量子 1 回（BVアルゴリズム）",
        )

        # ===================================================================
        # Chapter 1: 伏線パズル：下を |−⟩ にした CNOT の正体
        # ===================================================================
        self.chapter("01  伏線パズル：下を |−⟩ にした CNOT は、上の Z ゲートと同じ！")

        p_left = panel(6.4, 4.2, [-3.5, -0.35, 0])
        p_right = panel(6.4, 4.2, [3.5, -0.35, 0])
        t_left = text(
            "回路：下を |−⟩ に固定した CNOT", 22, BLUE, max_width=5.8
        ).move_to([-3.5, 1.32, 0])
        t_right = text(
            "実際に起きること：上だけ符号反転（Zと同じ！）", 20, AMBER, max_width=5.8
        ).move_to([3.5, 1.32, 0])

        wa = Line(
            [-5.2, 0.35, 0], [-1.6, 0.35, 0], stroke_color=WHITE, stroke_width=3.0
        )
        wb = Line(
            [-5.2, -1.05, 0], [-1.6, -1.05, 0], stroke_color=WHITE, stroke_width=3.0
        )
        in_a = make_ket_badge(
            "上 a: |+⟩",
            [-5.6, 0.35, 0],
            color=BLUE,
            width=1.4,
            height=0.58,
            font_size=21,
        )
        in_b = make_ket_badge(
            "下 b: |−⟩",
            [-5.6, -1.05, 0],
            color=MINT,
            width=1.4,
            height=0.58,
            font_size=21,
        )
        cnot1 = make_cnot_symbol(-3.4, 0.35, -1.05, color=AMBER)

        self.say_cue("ep2_c01", CUES_EP2[0]["display"])
        self.play(
            FadeIn(p_left),
            FadeIn(p_right),
            FadeIn(t_left),
            FadeIn(t_right),
            run_time=1.1,
        )
        self.finish_cue("ep2_c01")

        self.say_cue("ep2_c02", CUES_EP2[1]["display"])
        self.play(
            Create(wa),
            Create(wb),
            FadeIn(in_a),
            FadeIn(in_b),
            FadeIn(cnot1),
            run_time=1.3,
        )
        self.finish_cue("ep2_c02")

        eq1 = text("・上が |0⟩ → 下は何もしない → +|0⟩ ⊗ |−⟩", 20, WHITE).move_to(
            [3.5, 0.52, 0]
        )
        eq2 = text("・上が |1⟩ → 下に X が掛かる → −|1⟩ ⊗ |−⟩", 20, RED).move_to(
            [3.5, -0.15, 0]
        )
        eq3 = text("⇒ 上の量子ビットに Z を掛けたのと同じ！", 22, AMBER).move_to(
            [3.5, -0.88, 0]
        )

        self.say_cue("ep2_c03", CUES_EP2[2]["display"])
        self.play(FadeIn(eq1), FadeIn(eq2), FadeIn(eq3), run_time=1.3)
        self.finish_cue("ep2_c03")

        out_a = make_ket_badge(
            "|−⟩ に反転!",
            [-1.3, 0.35, 0],
            color=RED,
            width=1.65,
            height=0.58,
            font_size=20,
        )
        out_b = make_ket_badge(
            "|−⟩ のまま",
            [-1.3, -1.05, 0],
            color=MINT,
            width=1.65,
            height=0.58,
            font_size=20,
        )
        eq4 = make_ket_badge(
            "CNOT (|+⟩ ⊗ |−⟩)  =  |−⟩ ⊗ |−⟩",
            [3.5, -1.72, 0],
            color=MINT,
            width=5.4,
            height=0.62,
            font_size=21,
        )

        self.say_cue("ep2_c04", CUES_EP2[3]["display"])
        self.play(
            FadeIn(out_a, scale=0.9),
            FadeIn(out_b, scale=0.9),
            FadeIn(eq4),
            run_time=1.3,
        )
        self.finish_cue("ep2_c04")

        # ===================================================================
        # Chapter 2 & 3: 秘密の鍵 s = 101 の回路と「一斉魚拓」
        # ===================================================================
        self.clear_diagram()
        self.chapter("02  秘密の鍵 s = 101 を1回で転写する Bernstein–Vazirani 回路")

        bv_card = panel(13.4, 4.4, [0, -0.35, 0])
        bv_title = text(
            "秘密の鍵 s = 101：s_i = 1 の線（a2 と a0）からだけ CNOT が刺さっている",
            21,
            AMBER,
        ).move_to([0, 1.45, 0])

        ys = [0.78, 0.05, -0.68, -1.55]
        w_names = ["a2 (s2=1)", "a1 (s1=0)", "a0 (s0=1)", "下 b"]
        w_colors = [BLUE, BLUE, BLUE, MINT]
        wires = VGroup()
        in_badges = VGroup()

        for y, nm, col in zip(ys, w_names, w_colors):
            wires.add(
                Line([-4.5, y, 0], [4.2, y, 0], stroke_color=WHITE, stroke_width=2.6)
            )
            init_txt = f"{nm}: |+⟩" if nm != "下 b" else "下 b: |−⟩"
            in_badges.add(
                make_ket_badge(
                    init_txt,
                    [-5.35, y, 0],
                    color=col,
                    width=1.75,
                    height=0.52,
                    font_size=18,
                )
            )

        self.say_cue("ep2_c05", CUES_EP2[4]["display"])
        self.play(
            FadeIn(bv_card),
            FadeIn(bv_title),
            Create(wires),
            FadeIn(in_badges),
            run_time=1.4,
        )
        self.finish_cue("ep2_c05")

        classical_note = make_ket_badge(
            "f(x)=s・x mod 2：100→1 / 010→0 / 001→1",
            [0.0, -2.18, 0],
            color=MUTED,
            width=6.2,
            height=0.48,
            font_size=18,
        )
        self.say_cue("ep2_c06", CUES_EP2[5]["display"])
        self.play(FadeIn(classical_note), run_time=1.0)
        self.finish_cue("ep2_c06")

        # Oracle box + CNOTs from a2 (ys[0]) and a0 (ys[2]) to b (ys[3])
        oracle_frame = DashedLine([-2.8, 1.15, 0], [-2.8, -1.9, 0], stroke_color=AMBER)
        oracle_frame2 = DashedLine([0.2, 1.15, 0], [0.2, -1.9, 0], stroke_color=AMBER)
        cnot_a2 = make_cnot_symbol(-1.8, ys[0], ys[3], color=AMBER)
        cnot_a0 = make_cnot_symbol(-0.7, ys[2], ys[3], color=AMBER)

        self.say_cue("ep2_c07", CUES_EP2[6]["display"])
        self.play(
            Create(oracle_frame),
            Create(oracle_frame2),
            FadeIn(cnot_a2),
            FadeIn(cnot_a0),
            run_time=1.4,
        )
        self.finish_cue("ep2_c07")

        # Mid badges after 1 pass of Uf: a2 -> |->, a1 -> |+>, a0 -> |->
        mid_a2 = make_ket_badge(
            "|−⟩ (反転!)",
            [1.15, ys[0], 0],
            color=RED,
            width=1.55,
            height=0.50,
            font_size=18,
        )
        mid_a1 = make_ket_badge(
            "|+⟩ (そのまま)",
            [1.15, ys[1], 0],
            color=BLUE,
            width=1.55,
            height=0.50,
            font_size=18,
        )
        mid_a0 = make_ket_badge(
            "|−⟩ (反転!)",
            [1.15, ys[2], 0],
            color=RED,
            width=1.55,
            height=0.50,
            font_size=18,
        )

        self.say_cue("ep2_c08", CUES_EP2[7]["display"])
        self.play(
            FadeIn(mid_a2, scale=0.9),
            FadeIn(mid_a1, scale=0.9),
            FadeIn(mid_a0, scale=0.9),
            run_time=1.4,
        )
        self.finish_cue("ep2_c08")

        # Final H gates on top 3 wires -> output |1⟩, |0⟩, |1⟩
        h_gates = VGroup(
            make_gate_box("H", [2.65, ys[0], 0], color=BLUE, size=0.62, font_size=22),
            make_gate_box("H", [2.65, ys[1], 0], color=BLUE, size=0.62, font_size=22),
            make_gate_box("H", [2.65, ys[2], 0], color=BLUE, size=0.62, font_size=22),
        )
        out_badges = VGroup(
            make_ket_badge(
                "s2 = 1 !",
                [4.95, ys[0], 0],
                color=AMBER,
                width=1.45,
                height=0.52,
                font_size=20,
            ),
            make_ket_badge(
                "s1 = 0 !",
                [4.95, ys[1], 0],
                color=MINT,
                width=1.45,
                height=0.52,
                font_size=20,
            ),
            make_ket_badge(
                "s0 = 1 !",
                [4.95, ys[2], 0],
                color=AMBER,
                width=1.45,
                height=0.52,
                font_size=20,
            ),
        )
        quantum_win = make_ket_badge(
            "量子：たった 1 回の通過で s = 101 が確率 100% で出現！",
            [0.0, -2.18, 0],
            color=AMBER,
            width=7.2,
            height=0.52,
            font_size=19,
        )

        self.say_cue("ep2_c09", CUES_EP2[8]["display"])
        self.play(
            FadeIn(h_gates),
            FadeIn(out_badges, shift=RIGHT * 0.15),
            Transform(classical_note, quantum_win),
            run_time=1.5,
        )
        self.finish_cue("ep2_c09")

        # ===================================================================
        # Chapter 3: 100万桁のスケーリングと波の集中
        # ===================================================================
        self.clear_diagram()
        self.chapter("03  古典 n 回 vs 量子 1 回：魚拓のように全桁を一括転写する")

        s_left = panel(6.3, 4.2, [-3.5, -0.35, 0])
        s_right = panel(6.3, 4.2, [3.5, -0.35, 0])
        st_l = text(
            "古典：1本ずつ棒で突いて調べる (n 回)", 20, MUTED, max_width=5.8
        ).move_to([-3.5, 1.32, 0])
        st_r = text(
            "量子：H^⊗n の干渉で正解 |s⟩ だけに 100% 集中！", 19, AMBER, max_width=5.8
        ).move_to([3.5, 1.32, 0])

        comp_1 = text(
            "・10 桁の鍵： 古典 10 回  vs  量子 1 回", 19, WHITE, max_width=5.7
        ).move_to([-3.5, 0.45, 0])
        comp_2 = text(
            "・1,000 桁の鍵： 古典 1,000 回  vs  量子 1 回", 19, WHITE, max_width=5.7
        ).move_to([-3.5, -0.25, 0])
        comp_3 = text(
            "・量子：n+1 ビット ＋ O(n) 周辺ゲート", 19, MINT, max_width=5.7
        ).move_to([-3.5, -0.95, 0])
        comp_4 = text(
            "すべての s_i が別々のビットの位相 (−1)^s_i に乗るため",
            16,
            BLUE,
            max_width=5.7,
        ).move_to([-3.5, -1.75, 0])

        # Right panel: 8 candidate bars for n=3, all 0 except s=101 at 100%
        axis_r = Line(
            [0.9, -1.55, 0], [6.1, -1.55, 0], stroke_color=GRID, stroke_width=2.0
        )
        bars_r = VGroup()
        bit_labels = ["000", "001", "010", "011", "100", "101", "110", "111"]
        for idx, b_str in enumerate(bit_labels):
            bx = 1.22 + idx * 0.65
            is_ans = b_str == "101"
            bh = 1.85 if is_ans else 0.05
            bcol = AMBER if is_ans else MUTED
            rect = RoundedRectangle(
                width=0.42,
                height=bh,
                corner_radius=0.04,
                stroke_color=bcol,
                fill_color=bcol,
                fill_opacity=0.92,
            ).move_to([bx, -1.55 + bh / 2, 0])
            lbl = code_text(b_str, 14, AMBER if is_ans else MUTED).move_to(
                [bx, -1.85, 0]
            )
            bars_r.add(rect, lbl)
            if is_ans:
                peak_lbl = text("正解 s=101 (100%!)", 17, AMBER, max_width=2.2).move_to(
                    [bx, 0.62, 0]
                )
                bars_r.add(peak_lbl)

        self.say_cue("ep2_c10", CUES_EP2[9]["display"])
        self.play(
            FadeIn(s_left),
            FadeIn(s_right),
            FadeIn(st_l),
            FadeIn(st_r),
            FadeIn(comp_1),
            FadeIn(comp_2),
            FadeIn(comp_3),
            FadeIn(comp_4),
            Create(axis_r),
            FadeIn(bars_r),
            run_time=1.6,
        )
        self.finish_cue("ep2_c10")

        self.say_cue("ep2_c11", CUES_EP2[10]["display"])
        self.finish_cue("ep2_c11", extra_pad=0.8)


if __name__ == "__main__":
    run_checks()
    print("Episode 2 mathematical checks passed!")
