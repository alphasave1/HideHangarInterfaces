import game
import Keys
from debug_utils import LOG_CURRENT_EXCEPTION
from gui.app_loader import g_appLoader
from gui.Scaleform.daapi.view.lobby.hangar.Hangar import Hangar
from gui.Scaleform.framework import ViewTypes

hangar = None

def toggleHangarUI():
    lobby = g_appLoader.getApp()
    hangar = lobby.containerManager.getView(ViewTypes.LOBBY_SUB)
    hangar.flashObject.visible = not hangar.flashObject.visible

def handleKeyEvent(event):
    ret = wg_handleKeyEvent(event)
    try:
        if event.isKeyDown() and not event.isRepeatedEvent():
            if event.key == Keys.KEY_F11:
                toggleHangarUI()
    except:
        LOG_CURRENT_EXCEPTION()
    return ret

# オリジナルのキーイベント処理関数を乗っ取る
wg_handleKeyEvent = game.handleKeyEvent
game.handleKeyEvent = handleKeyEvent
