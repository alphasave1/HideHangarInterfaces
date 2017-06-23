import game
import Keys
from debug_utils import LOG_CURRENT_EXCEPTION '''例外発生箇所出力'''
from gui.Scaleform.daapi.view.lobby.hangar.Hangar import Hangar '''HangarをImport'''
from gui.mods.HideHangarInterfaces import hangar

hangar = None

#hangarオブジェクトへの参照を退避
def switchCarousels(self):
	global hangar
	hangar = self
	print 'switchCarousels'
	wg_switchCarousels(self)

def switchheader(self):
	global hangar
	hangar = self
	print 'switchheader'
	wg_switchheader(self)

def switchcrew(self):
	global hangar
	hangar = self
	print 'switchcrew'
	wg_switchcrew(self)

def switchparams(self):
	global hangar
	hangar = self
	print 'switchparams'
	wg_switchparams(self)

def switchresearch(self):
	global hangar
	hangar = self
	print 'switchresearch'
	wg_switchresearch(self)

def switchammunition(self):
	global hangar
	hangar = self
	print 'switchammunition'
	wg_switchammunition(self)

def switchtmenXp(self):
	global hangar
	hangar = self
	print 'switchtmenXp'
	wg_switchtmenXp(self)

def switchquests(self):
	global hangar
	hangar = self
	print 'switchquests'
	wg_switchquests(self)

def switchswitchMode(self):
	global hangar
	hangar = self
	print 'switchswitchMode'
	wg_switchswitchMode(self)

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

#hangarのheader切り替え
wg_switchheader = Hangar._Hangar__updateHeader
Hangar._Hangar__updateHeader = switchheader

#hangarのcrew切り替え '''動くか怪しい'''
wg_switchcrew = Hangar._Hangar__updateCrew
Hangar._Hangar__updateCrew = switchcrew

#hangarのparams切り替え '''動くか怪しい'''
wg_switchparams = Hangar._Hangar__updateParams
Hangar._Hangar__updateParams = switchparams

#hangarのresearch切り替え '''動くか怪しい'''
wg_switchresearch = Hangar._Hangar__updateVehicleInResearchPanel
Hangar._Hangar__updateVehicleInResearchPanel = switchresearch

#hangarのammunition切り替え '''動くか怪しい'''
wg_switchammunition = Hangar._Hangar__updateVehicleInResearchPanel
Hangar._Hangar__updateVehicleInResearchPanel = switchammunition

#hangarのtmenXp切り替え '''tmenXpPanelの値は見つからなかったので省略'''
wg_switchtmenXp = switchtmenXp

#hangarのquests切り替え '''questsControlの値は見つからなかったので省略'''
wg_switchquests = switchquests

#hangarのswitchMode切り替え '''switchModePanelの値は見つからなかったので省略'''
wg_switchswitchMode = switchswitchMode

#オリジナルキーイベント処理
wg_handleKeyEvent = game.handleKeyEvent
game.handleKeyEvent = handleKeyEvent
