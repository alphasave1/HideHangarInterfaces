import game
import Keys
from debug_utils import LOG_CURRENT_EXCEPTION '''��O�����ӏ��o��'''
from gui.Scaleform.daapi.view.lobby.hangar.Hangar import Hangar '''Hangar��Import'''

hangar=None

def CTRLInterfaces(): '''hangar.components���ɑ��݂���ϐ��̏���'''
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
def handleKeyEvent(event): '''�L�[�C�x���g�Ăяo��'''
	ret = wg_handleKeyEvent(event)
	try:
	    if event.isKeyDown() and not event.isRepeatedEvent():
		if event.key == Keys.KEY_M:
		    CTRLInterfaces()
	except: '''�������G���[���o����'''
	    LOG_CURRENT_EXCEPTION() '''���O���o��'''
	return ret

#�I���W�i���L�[�C�x���g����
wg_handleKeyEvent = game.handleKeyEvent
game.handleKeyEvent = handleKeyEvent
