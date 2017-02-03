# 2017.02.03 21:47:18 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/EditUtils.py
import BigWorld, GUI, Math, ResMgr

def setup():
    BigWorld.camera(BigWorld.CursorCamera())
    BigWorld.setCursor(GUI.mcursor())
    GUI.mcursor().visible = True


def clearAll():
    while len(GUI.roots()):
        GUI.delRoot(GUI.roots()[0])


def clone(component):
    ResMgr.purge('gui/temp_clone.gui', True)
    component.save('gui/temp_clone.gui')
    return GUI.load('gui/temp_clone.gui')


weatherWindow = None

def weather():
    global weatherWindow
    setup()
    weatherWindow = GUI.load('gui/weather_window.gui')
    GUI.addRoot(weatherWindow)
    return weatherWindow


def saveWeather():
    if weatherWindow:
        weatherWindow.save('gui/weather_window.gui')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\bwobsolete_helpers\PyGUI\EditUtils.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:47:18 St�edn� Evropa (b�n� �as)
