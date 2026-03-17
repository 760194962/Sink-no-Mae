# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define n = Character(None, kind=nvl, what_cps=30)


# 游戏在此开始。
label before_main_menu:
    jump start
label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene bg_kaiwa
    with fade
    pause 0.5
    play music "audio/echoTōryanse.mp3"
    # 此处显示各行对话。
    n "{cps=30}食堂で二人が座っている。{/cps}"
    n "{cps=30}「今日の飯、{/cps}"
    pause 0.2
    extend "{cps=30}悪くなかっただろ？」 {/cps}"
    extend "{cps=30}大沢ぴいは、親友の符江佬（フーゴンロウ）・胡嬌霆（フーギュテイン）に問いかけた。{/cps}"
    
    window hide
    # 等待玩家第二次点击（用于查看背景）
    pause
    # 玩家点击后恢复对话框并继续下一句
    window show

    n "{cps=30}......{/cps}"
    n "{cps=30}大沢ぴいは居心地わるかった，{/cps}"
    extend"{cps=30}向かいの胡嬌霆はおそらく察している。{/cps}"
    n "{cps=30}胡嬌霆は動揺していた，{/cps}"
    extend "{cps=30}向かいの大沢ぴいもおそらく気づいている。{/cps}"
    n "{cps=30}ふたりとも、オトナなんだから。{/cps}"

    scene bg_shokudou
    with fade
    n "{cps=30}「まあな」 {/cps}"
    extend "{cps=30}胡はそっけなく、しかし苛立ちを隠さずに答えた。{/cps}"
    extend "{cps=30}首の斜め上にある顔を、指でつついた。{/cps}"
    nvl clear
    n "{cps=30}「親知らず、飯食うのは大丈夫なの？」 {/cps}"
    n "{cps=30}大沢ぴいは他人を気遣うのが好きだ。{/cps}"
    n "{cps=30}「......こっち、腫れてるように見えるのか？」{/cps}"
    extend "{cps=30} 胡は指をわざと力を込めて突いた。{/cps}"
    n "{cps=30}胡は今日は他人の気遣いを拒むのだ。{/cps}"
    n "{cps=30}「ないな。」{/cps}"
    n "{cps=30}「......」{/cps}"
    n "{cps=30}「............」{/cps}"
    n "{cps=30}雰囲気が冷たくなった。{/cps}"
    n "{cps=30}「食べ終わった、行こう。」二人は皿を持ち上げた。{/cps}" 
    extend "{cps=30}  //kaiwaEnd{/cps}" 
    n "{cps=30}十秒後、{/cps}"
    stop music fadeout 1.0
    play music "audio/clocksfx.mp3"
    extend "{cps=30}二つの皿がざぶんと洗い場に落ちた。{/cps}"
    
    scene black
    with fade

    # 清除 NVL 缓冲，下一句将作为全新一页显示
    nvl clear
    centered "{cps=30}{i}見てしまった。{i}{/cps}"

    play music "audio/悪夢への彷徨.mp3"
    scene bg_exit
    with fade
    n "{cps=30}大沢ぴいが食堂のホールを曲がると、冴えない身なりのチャイナ男が、{/cps}"
    extend "{cps=30}通路の洗面台に腰をかがめて突っ伏しているのが目に入った。 {/cps}"

    scene bg_sink
    n "{cps=30}チャイナ男は、{/cps}"
    extend "{cps=30}まるで水を飲むかのように、{/cps}"
    extend "{cps=30}蛇口から出る水を口に含んでいた。{/cps}"
    
    n "{cps=30}大沢ぴいは反対側の蛇口へ歩み寄り、ハンドルをひねる。{/cps}"
    extend "{cps=30}壊れることのない日常、その断片を使わせてもらおうとしたのだ......{/cps}"
    
    scene black
    with fade
    centered "{cps=30}だが、{/cps}"
    stop music fadeout 1.0
    extend "{cps=2}水は出なかった{/cps}"
    
    play music "audio/シュレディンガー.mp3"
    nvl clear
    scene bg_sink
    with fade

    n "{cps=30}もう一方の蛇口に目を向け、{/cps}"
    extend "{cps=30}先ほどのチャイナ男の{color=#f00}殘留思念{/color}があった。{/cps}"
    scene black
    centered "{cps=30}{color=#f00}「オレは忙しいんだ、デートなんだ」{/color}{/cps}"
    nvl clear
    scene bg_sink
    with fade

    n "{cps=30}さっき見えたのに、{/cps}"
    extend "{cps=30}わずか五秒前、その男が{/cps}"
    extend "{cps=10}日常的な水{/cps}"
    extend "{cps=30}で濡れた手で、跳ねた髪を撫でつけた動きが脳裏をよぎる。{/cps}"

    # 在这里也想清除之前的 NVL 内容、单独显示下一句时，再调用 nvl clear
    nvl clear
    scene black
    with fade
    centered "{cps=30}NICHIJOUという名のメインストーリーに疲れ果てた大沢ぴいは{/cps}"
    centered "{cps=30}そろそろ「次へ」のボタンを押してしまいたいと願うんだ{/cps}"
    scene bg_sink
    with fade
    n "{cps=30}材質が違うのか、あるいはレンダリングの失敗か。{/cps}"
    n "{cps=30}目の前の蛇口は、脳内のアセットライブラリにある姿とは異なっている。{/cps}"
    n "{cps=30}鏡面反射するはずの蛇口の表面に、自分の顔を映し出すことはできなかった。 {/cps}"

    n "{cps=30}「蛇口は二つ。一つは水が出ない。ならもう一方は……{/cps}"
    extend "{cps=30}ニマイナスイチイコール一……」{/cps}"
    extend "{cps=30}頭はまだ算数の問題を処理している最中だというのに、体はすでに横へずれて隣の蛇口の前に立っていた。{/cps}"
    n "{cps=30}迷いなくハンドルを回す。{/cps}"

    play music "audio/watersfx.mp3"
    extend "{cps=30}昼食の汚れを鮮やかに、そしていさぎよく洗い流した。{/cps}"

    nvl clear
    stop music fadeout 3.0
    
    scene bg_exit
    with fade
    n "{cps=30}大沢ぴいは満足げに踵を返し、洗面台を後にした。{/cps}"

    scene black
    with fade

    play music "audio/shinon.mp3"
    centered "{cps=30}また、{/cps}"
    extend "{cps=10}日常の軌道{/cps}"
    extend "{cps=30}に戻ったと感じている。{/cps}"
    centered "{cps=5}One NICHIJOU after another.{/cps}"
    stop music fadeout 2.0

    scene black
    with fade
    pause 0.5
    python:
        renpy.quit()