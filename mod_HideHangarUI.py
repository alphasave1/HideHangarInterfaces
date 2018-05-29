import game
import Keys
import GUI
from debug_utils import LOG_CURRENT_EXCEPTION
from gui.app_loader import g_appLoader
from gui.Scaleform.daapi.view.lobby.hangar.Hangar import Hangar
from gui.Scaleform.framework import ViewTypes

class MOD:
    AUTHOR = 'Chirimen , alphasave1'
    NAME = 'HideHangarUI'
    VERSION = '1.0'
    DESCRIPTION = 'If You Push F11 Key, Hangar UI Will Hide. Else If You Push F12 Key,All Ui Will Hide.'
    SUPPORT_URL = 'http://www.twitter.com/alphasave1'

hangar = None
def init():
    __optimizer = GUI.WGUIOptimizer()
    __optimizer.setEnable(False)

def toggleHangarUI():
    lobby = g_appLoader.getApp()
    hangar = lobby.containerManager.getView(ViewTypes.LOBBY_SUB)
    hangar.flashObject.visible = not hangar.flashObject.visible

def toggleAllUI():
    _lobby = g_appLoader.getDefLobbyApp()
    _lobby.flashObject.visible = not _lobby.flashObject.visible

def handleKeyEvent(event):
    ret = wg_handleKeyEvent(event)
    try:
        if event.isKeyDown() and not event.isRepeatedEvent():
            if event.key == Keys.KEY_F11:
                toggleHangarUI()
            if event.key == Keys.KEY_F12:
                toggleAllUI()
    except:
        LOG_CURRENT_EXCEPTION()
    return ret

wg_handleKeyEvent = game.handleKeyEvent
game.handleKeyEvent = handleKeyEvent
