import game
import Keys
from debug_utils import LOG_CURRENT_EXCEPTION '''例外発生箇所出力'''
from gui.Scaleform.daapi.view.lobby.hangar.Hangar import Hangar '''HangarをImport'''

hangar = None

#hangarオブジェクトへの参照を退避
def switchCarousels(self):
	global hangar
	hangar = self
	print 'switchCarousels'
	wg_switchCarousels(self)

def CTRLInterfaces(): '''hangar.components内に存在する変数の処理'''
    tankCarousel = hangar.components['tankCarousel']
    if tankCarousel:
        tankCarousel.flashObject.visible = not tankCarousel.flashObject.visible
    crew = hangar.components['crew']
    if crew:
	crew.flashObject.visible = not crew.flashObject.visible
    header = hangar.components['header']
    if header:
	header.flashObject.visible = not header.flashObject.visible
    tmenXpPanel = hangar.components['tmenXpPanel']
    if tmenXpPanel:
	tmenXpPanel.flashObject.visible = not tmenXpPanel.flashObject.visible
    params = hangar.components['params']
    if params:
	params.flashObject.visible = not params.flashObject.visible
    ammunitionPanel = hangar.components['ammunitionPanel']
    if ammunitionPanel:
	ammunitionPanel.flashObject.visible = not ammunitionPanel.flashObject.visible
    researchPanel = hangar.components['researchPanel']
    if researchPanel:
	researchPanel.flashObject.visible = not researchPanel.flashObject.visible
    switchModePanel = hangar.components['switchModePanel']
    if switchModePanel:
	switchModePanel.flashObject.visible = not switchModepanel.flashObject.visible
    questsControl = hangar.components['questsControl']
    if questsControl:
	questsControl.flashObject.visible = not quests.flashObject.visible
def handleKeyEvent(event): '''キーイベント呼び出し'''
	ret = wg_handleKeyEvent(event)
	try:
	    if event.isKeyDown() and not event.isRepeatedEvent():
		if event.key == Keys.KEY_M:
		    CTRLInterfaces()
	except: '''もしもエラーが出たら'''
	    LOG_CURRENT_EXCEPTION() '''ログを出力'''
	return ret

#hangarのcarousel切り替え
wg_switchCarousels = Hangar._Hangar__switchCarousels
Hangar._Hangar__switchCarousels = switchCarousels

#オリジナルキーイベント処理
wg_handleKeyEvent = game.handleKeyEvent
game.handleKeyEvent = handleKeyEvent
