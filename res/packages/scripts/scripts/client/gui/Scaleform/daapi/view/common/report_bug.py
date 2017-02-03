# 2017.02.03 21:49:18 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/common/report_bug.py
from account_helpers import getAccountDatabaseID
from adisp import process
from avatar_helpers import getAvatarDatabaseID
from gui import GUI_SETTINGS, DialogsInterface
from gui import makeHtmlString
from gui.Scaleform.daapi.view.dialogs import DIALOG_BUTTON_ID
from gui.Scaleform.daapi.view.meta.ReportBugPanelMeta import ReportBugPanelMeta
from gui.Scaleform.locale.MENU import MENU
from helpers import i18n, dependency
from skeletons.gui.game_control import IExternalLinksController

class ReportBugPanel(ReportBugPanelMeta):

    def reportBug(self):
        reportBugOpenConfirm(getAccountDatabaseID() or getAvatarDatabaseID())

    def _populate(self):
        super(ReportBugPanel, self)._populate()
        links = GUI_SETTINGS.reportBugLinks
        if links:
            reportBugLink = makeHyperLink('ingameMenu', MENU.INGAME_MENU_LINKS_REPORT_BUG)
            self.as_setHyperLinkS(reportBugLink)


def getForumURL(accountId):
    links = GUI_SETTINGS.reportBugLinks
    url = None
    for region in links:
        min = long(links[region]['min'])
        max = long(links[region]['max'])
        if min <= long(accountId) <= max:
            url = links[region]['url']
            break

    return url


def makeHyperLink(linkType, textId):
    text = i18n.makeString(textId)
    attrs = {'linkType': linkType,
     'text': text}
    linkHtml = makeHtmlString('html_templates:lobby/system_messages', 'link', attrs)
    return linkHtml


@process
def reportBugOpenConfirm(accountId):
    isOk = yield DialogsInterface.showI18nConfirmDialog('reportBug', focusedID=DIALOG_BUTTON_ID.SUBMIT)
    if isOk:
        links = dependency.instance(IExternalLinksController)
        links.open(getForumURL(accountId))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\common\report_bug.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:49:19 St�edn� Evropa (b�n� �as)
