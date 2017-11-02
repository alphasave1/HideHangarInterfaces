# HideHangarInterfaces
Cording at WoT-DebugServer-Master(Replserver)
## 特徴
 - ガレージ画面が表示されている状態で何らかのキーを押すと、インターフェースが非表示になる
 - もう一度キーを押すと非表示のインターフェースが表示に戻る

<b>mod_testhide_ver_3_1.py が最新のファイルです</b>

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
 :F11キー

## 考えていた案
1.
lobby自体を呼び出し、flashObjectのvisible=Falseもしくはalpha=0とする  
しかし、visible=Falseだと、カーソルもOFFになってしまい、車両閲覧操作が不可能になる  
また、alpha=0で非表示にしたとしてもオブジェクトとしては残っており、クリックなどで他のパーツが機能してしまうため、ユーザーの意図しない操作がされてしまう可能性あり  
結果、没  
2.
lobbyの表示状態をBattleLoadingにする  
しかし、カーソルでの車両閲覧操作ができない  
結果、没  
3.
hangar.components内にあるtmenXpPanel,header,tankCarousel,crew,params,ammunitionPanel,researchPanel,questsControl,switchModePanelのflashObjectのvisible=Falseもしくはalpha=0とする  
しかし、visible=Falseにした後visible=Trueに戻すと、tankCarouselの選択機能が効かなくなる  
また、alpha=0としても、ユーザーの意図しない操作(例えば、適当にhangar下部をクリックした際に車両表示が変わってしまう、など)がされてしまう可能性あり  
結果、没  
4.
hangarのflashObjectのvisible=Falseもしくはalpha=0とする
非常に良い、バグも現時点では見られない  
結果、これを採用  
因みに、lobbyHeader,messengerBarの非表示に関してはmessengerBarは問題なく表示、非表示を行えるが、lobbyHeaderはflashObjectのvisible=Falseもしくはalpha=0としても、表示を戻した際にほぼ全てのボタン操作が効かなくなる  
