![Static Badge](https://img.shields.io/badge/ojigi-v1.0-blue)

# OJIGI
「ペコちゃん」のシステムです。  
相手との年収の差額からあなたがするべきお辞儀の角度を教えてくれます。  
[たのしいmicro:bitコンテスト2023](https://makezine.jp/blog/2023/06/microbitcontest2023.html)の成果物。

▼プロジェクト動画([YouTube](https://www.youtube.com/watch?v=Rlp9lnXqhYo))▼  
[![](https://img.youtube.com/vi/Rlp9lnXqhYo/0.jpg)](https://www.youtube.com/watch?v=Rlp9lnXqhYo)

## システム概要  
ネクタイピンとしてmicrobitを実装
- 年収が低い方がより深いお辞儀をする
   - 年収差で必要なお辞儀の角度が変わる
   - 年収さが大ければより大きなお辞儀が必要
- 必要な角度に達したらボードのLEDで通知
   - 5*5のLEDを5マスのゲージとして使用
   - 必要な角度までお辞儀をすればゲージが満タン(全点灯)に

### 時間があれば取り組む
以下はコンテストの締切に間に合わない場合、コンテストとは関係なく取り組む
- より速いお辞儀だとボーナスポイント
- 欧米ver.の握手版も開発

## 環境
```
python
```