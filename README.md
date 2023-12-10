# ATCODER
## 使い方
------------------------
このレポジトリの使い方を説明します！

- Step1. レポジトリをクローンしましょう!

~~~
git clone https://github.com/kaikai529/atcoder_python.git
~~~

※ gitをインストールしてない人はしてください. <br>
<url>https://qiita.com/WebSysRider/items/3d9ea47f4af8c0dd4ed0

- Step2. Visual Studio Code　を開く

※　VScodeをインストールしてください
<url> https://code.visualstudio.com/Download

- Step3. 新しいフォルダーとテンプレートを作成する

まず，my_answerのフォルダーに入ります． <br>
以下のコマンドを打ち込むと下の出力を得ます．<br>
ここにコンテストの名前を入力しましょう！
~~~
python make_folder.py

(画面)　
Input contest name:

(入力後)
Input contest name: abc120
~~~

## レートについて

- レート 1-399：灰色
- レート 400-799：茶色
- <strong> レート 800-1199：緑色 </strong> <-- 目標
- レート 1200-1599：水色
- レート 1600-1999：青色
- レート 2000-2399：黄色
- レート 2400-2799：橙色
- レート 2800-3199：赤色


## template.pyについて

自分好みのテンプレートを作成しましょう！！！

| contest name | A | B | C | D | E | F | memo |
|:------------:|:-:|--:|:--|:-:|:-:|:-:|:----:|
|abc043        |o|o|o|△| - | - | |
|abc044        |o|o|o|?| - | - | |
|abc045        |o|o|o|o| - | - | |
|abc046        |o|o|o|o| - | - | |
|abc047        |o|o|o|?| - | - | |
|abc048        |o|o|o|?| - | - | |
|abc049        |o|o|o|△| - | - | D:グラフ連結 |
|abc050        |o|o|o|?| - | - | |
|abc051        |o|o|o|△| - | - | D:ワーシャルフロイド法 |
|abc052        |o|o|o|o| - | - | |
|abc053        |o|o|o|o| - | - | |
|abc054        |o|o|o|o| - | - |C:グラフ全探索,D:動的計画法|
|abc055        |o|o|o|o| - | - | |
|abc056        |o|o|△|?| - | - | |
|abc057        |o|o|o|x| - | - | |
|abc058        |o|o|o|x| - | - | |
|abc059        |o|o|x|-| - | - | |
|abc060        |o|o|o|x| - | - |D:ナップザック問題 |
|abc061        |o|o|o|x| - | - |D:ベルマンフォード法 |
|abc062        |o|o|x|-| - | - | |
|abc063        |o|o|o|x| - | - | |
|abc064        |o|-|-|-| - | - | |
|abc065        |o|o|o|-| - | - | |
|abc066        |o|o|o|-| - | - |C:deque |
|abc067        |o|o|o|-| - | - |C:累積和 |
|abc068        |o|o|o|-| - | - |C:グラフ理論 |
|abc069        |o|o|o|-| - | - |D(補足):色でブロックを作る |
|abc070        |o|o|o|o| - | - |D:木構造の探索 |
|abc071        |o|o|o|o| - | - | |
|abc072        |o|o|o|o| - | - | |
|abc073        |o|o|o|-| - | - | |
|abc074        |o|o|-|-| - | - | |
|abc075        |o|o|o|-| - | - |C:グラフ理論 |
|abc076        |o|o|o|-| - | - | |
|abc077        |o|o|o|-| - | - |C:bisect |
|abc078        |o|o|o|-| - | - | |
|abc079        |o|o|o|o| - | - |D:ワーシャルフロイド法 |
|abc080        |o|o|o|-| - | - |C:Bit探索 |
|abc078        |o|o|o|-| - | - | |
|abc079        |o|o|o|o| - | - |D:ワーシャルフロイド法 |
|abc080        |o|o|o|-| - | - |C:Bit探索 |
|abc081        |o|o|o|-| - | - | |
|abc082        |o|o|o|-| - | - | |
|abc083        |o|o|o|-| - | - | |
|abc084        |o|o|o|o| - | - | |
|abc085        |o|o|o|o| - | - | |
|abc086        |o|o|o|-| - | - | |
|abc087        |o|o|o|-| - | - |C:累積和 |
|abc088        |o|o|o|o| - | - |D:幅優先探索 |
|abc089        |o|o|o|-| - | - | |
|abc089        |o|o|o|-| - | - | |
|abc090        |o|o|o|o| - | - | |
|abc091        |o|o|-|-| - | - | |
|abc092        |o|o|o|-| - | - | |
|abc093        |o|o|o|-| - | - | |
|abc094        |o|o|o|o| - | - | |
|abc095        |o|o|o|-| - | - | |
|abc096        |o|o|o|-| - | - | |
|abc097        |o|o|o|-| - | - |C:k<=5を用いる |
|abc098        |o|o|o|-| - | - | |
|abc099        |o|o|o|-| - | - |C:動的計画法 |
|abc100        |o|o|o|-| - | - | |
|abc101        |o|o|o|-| - | - | |
|abc102        |o|o|△|-| - | - | |
|abc103        |o|o|o|-| - | - | |
|abc104        |o|o|-|-| - | - | |
|abc105        |o|o|-|-| - | - |B:深さ優先探索 |
|abc106        |o|o|o|-| - | - |C:思考問題 |
|abc107        |o|o|o|-| - | - | |
|abc108        |o|o|△|-| - | - |C:数学的問題 |
|abc109        |o|o|o|△| - | - |D:数学的問題 |
|abc110        |o|o|o|-| - | - | |
|abc111        |o|o|o|-| - | - | |
|abc112        |o|o|△|o| - | - | |
|abc113        |o|o|o|-| - | - | |
|abc114        |o|o|o|-| - | - | |
|abc115        |o|o|o|o| - | - |D:計算量+再帰関数 |
|abc116        |o|o|o|-| - | - |C:領域分割 |
|abc117        |o|o|o|-| - | - | |
|abc118        |o|o|△|-| - | - |C:思考問題 |
|abc119        |o|o|-|-| - | - |A:datetime |
|abc120        |o|o|o|-| - | - |C:Queue |
|abc121        |o|o|o|-| - | - | |
|abc122        |o|o|o|-| - | - | |
|abc122        |o|o|o|-| - | - | |
|abc122        |o|o|o|△| - | - |D:尺取法 |
|-        |-|-|-|-| - | - | |
|abc130        |o|o|o|-| - | - | |
|abc131        |o|o|△|-| - | - | |
|abc132        |o|o|o|-| - | - | |
|abc133        |o|o|o|-| - | - | |
|abc134        |o|o|o|-| - | - | |
|abc135        |o|o|o|-| - | - | |
|abc175        |o|o|o|-| - | - | |
|abc176        |o|o|o|-| - | - | |
|abc178        |o|o|o|-| - | - | |
|abc179        |o|o|o|-| - | - | |
|abc180        |o|o|o|o| - | - | |
|abc181        |o|o|o|o| - | - | |
|abc182        |o|o|o|o| - | - |D:累積和 |
|abc183        |o|o|o|o| - | - |D:累積和 |
|abc184        |o|o|o|?| - | - | |
|abc185        |o|o|o|o| - | - | |
|abc186        |o|o|o|?| - | - | |
|abc187        |o|o|o|o| - | - | |
|abc188        |o|o|o|o| - | - |D:いもす法 |
|abc189        |o|o|o|o| - | - | |
|abc190        |o|o|o|o| - | - | |
|abc191        |o|o|o|o| - | - | |
|abc192        |o|o|o|o| - | - | |
|abc193        |o|o|o|?| - | - | |
|abc194        |o|o|o|?| - | - | |
|abc195        |o|o|o|o| - | - | |
|abc196        |o|o|o|?| - | - | |
|abc197        |o|o|o|?| - | - | |
|-             |-|-|-|-| - | - | |
|abc200        |o|o|o|?| - | - | |
|abc201        |o|o|o|?| - | - | |
|abc202        |o|o|o|o| - | - | |
|abc203        |o|o|o|-| - | - | |
|abc204        |o|o|o|△| - | - |C:グラフ，D:DP法 |
|abc205        |o|o|o|△| - | - |D:数学的問題 |
|abc206        |o|o|o|-| - | - | |
|abc207        |o|o|o|-| - | - | |
|abc208        |o|o|o|-| - | - | |
|abc209        |o|o|o|o| - | - |D:二部グラフ |
|-             |-|-|-|-| - | - | |
|abc230        |o|-|-|-| - | - | |
|abc231        |o|-|-|-| - | - | |
|abc232        |o|-|-|-| - | - | |
|abc233        |o|-|-|-| - | - | |
|abc234        |o|-|-|-| - | - | |
|abc235        |o|-|-|-| - | - | |
|abc236        |o|-|-|-| - | - | |
|abc237        |o|-|-|-| - | - | |
|abc238        |o|-|-|-| - | - | |
|abc239        |o|-|-|-| - | - | |
|abc240        |o|-|-|-| - | - | |
|abc241        |o|-|-|-| - | - | |
|abc242        |o|-|-|-| - | - | |
|abc243        |o|-|-|-| - | - | |
|abc244        |o|-|-|-| - | - | |
|abc245        |o|-|-|-| - | - | |
|abc246        |o|-|-|-| - | - | |
|abc247        |o|-|-|-| - | - | |
|abc248        |o|o|?|x| - | - | |
|abc249        |o|o|o|o| - | - |D:Pypy only |
|abc250        |o|o|o|x| - | - | |
|abc251        |o|o|o|△| - | - | |
|abc252        |o|o|o|△| - | - | |
|abc253        |o|o|o|-| - | - |C:heapq |
|abc254        |o|o|-|-| - | - | |
|abc255        |o|o|o|△| - | - | |
|abc256        |o|o|-|-| - | - | |
|abc257        |o|o|o|-| - | - | |
|abc258        |o|o|o|?| - | - | |
|abc259        |o|o|o|?| - | - | |
|abc260        |o|o|o|?| - | - | |
|abc261        |o|o|o|?| - | - | |
|abc262        |o|o|o|?| - | - | |
|abc263        |o|o|o|?| - | - | |
|abc264        |o|o|o|o| - | - | |
|abc265        |o|o|o|-| - | - | |
|abc266        |o|o|o|△| - | - | |
|abc267        |o|o|o|-| - | - | |
|abc268        |o|o|-|-| - | - | |
|abc269        |o|o|o|o| - | - |D:深さ優先探索（グループ分け）|
|abc276        |o|o|o|o| - | - | |
|abc277        |o|o|o|-| - | - |C:深さ優先探索,  |
|abc278        |o|o|o|o| - | - |D:計算量, E:二次元累積和 |
|abc279        |o|o|o|o| - | - | |
|abc281        |o|o|o|o| - | - |D:動的計画法 |
|abc282        |o|o|o|△| - | - |D:二部グラフの判定 |
|abc286        |o|o|-|-| - | - | |
|abc287        |o|o|-|-| - | - | |
|abc288        |o|o|△|x| - | - |C:グラフ理論 |
|abc289        |o|o|o|-| - | - |C:bit探索 |
|abc290        |o|o|△|-| - | - | |
|abc291        |o|o|o|-| - | - | |
|abc292        |o|o|o|-| - | - |C:調和数列の計算量 |
|abc293        |o|o|o|-| - | - | |
|abc294        |o|o|o|-| - | - | |
|abc295        |o|o|o|-| - | - | |
|abc296        |o|o|o|-| - | - | |
|abc297        |o|o|o|-| - | - | |
|abc298        |o|o|△|-| - | - |C:計算量 |
|abc299        |o|o|o|-| - | - | |
|abc300        |o|o|o|-| - | - | |
|abc301        |o|o|△|-| - | - | |
|abc302        |o|o|o|-| - | - |C:全探索 |
|abc303        |o|o|o|-| - | - |C:set，辞書型の理解 |
|abc304        |o|o|o|-| - | - |C:探索 |
|abc305        |o|o|o|-| - | - | |
|abc306        |o|o|o|-| - | - | |
|abc307        |o|-|-|-| - | - | |
|abc308        |o|o|△|-| - | - |C:浮動小数点の扱い |
|abc309        |o|o|-|-| - | - | |
|abc310        |o|o|o|-| - | - | |
|abc311        |o|o|o|-| - | - | |
|abc312        |o|o|o|-| - | - | |
|abc313        |o|o|o|-| - | - | |
|abc314        |o|o|o|-| - | - | |
|abc315        |o|o|o|-| - | - | |
|abc316        |o|o|-|-| - | - | |
|abc317        |o|o|o|-| - | - |C:再起 |
|abc318        |o|o|o|-| - | - | |
|abc319        |o|o|-|-| - | - | |
|abc320        |o|o|-|-| - | - | |
|abc321        |o|o|o|-| - | - | |
|abc322        |o|o|o|-| - | - | |
|abc323        |o|o|-|-| - | - | |
|abc324        |o|o|o|-| - | - | |
|abc325        |o|o|o|-| - | - | |
|abc326        |o|o|o|-| - | - | |
|abc327        |o|o|o|o| - | - |D:二部グラフ |
o ・・・ 解ける <br>
△ ・・・ 一発でできなかったが，理解できる・実装ができる <br>
x ・・・理解できる・実装できない <br>
? ・・・ 数学的に分からない

## 参考文献
- ワーシャルフロイド法
https://qiita.com/rp523/items/8fba3882c4a6ea203757