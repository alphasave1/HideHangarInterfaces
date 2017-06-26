# HideHangarInterfaces
Cording at WoT-DebugServer-Master(Replserver)
## 特徴
 - ガレージ画面が表示されている状態で何らかのキーを押すと、インターフェースが非表示になる
 - もう一度キーを押すと非表示のインターフェースが表示に戻る

## 非表示になる(はずの)インターフェース
 - tankCarousel  
 :`tankCarousel = hangar.components['tankCarousel']`
 - crew  
 :`crew = hangar.components['crew']`
 - header  
 :`header = hangar.components['header']`
 - tmenXpPanel  
 :`tmenXpPanel = hangar.components['tmenXpPanel']`
 - params  
 :`params = hangar.components['params']`
 - ammunitionPanel  
 :`ammunitionPanel = hangar.components['ammunitionPanel']`
 - researchPanel  
 :`researchPanel = hangar.components['researchPanel']`
 - switchModePanel  
 :`switchModePanel = hangar.components['switchModePanel']`
 - questsControl  
 :`questsControl = hangar.components['questsControl']`
 
 表示、非表示を行うキーの設定  
 :Mキー
