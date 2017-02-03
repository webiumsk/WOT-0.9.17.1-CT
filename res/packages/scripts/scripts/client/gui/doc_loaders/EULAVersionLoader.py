# 2017.02.03 21:48:09 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/doc_loaders/EULAVersionLoader.py
import ResMgr
from helpers import VERSION_FILE_PATH
__author__ = 'd_savitski'
VERSION_TAG = 'showLicense'

class EULAVersionLoader(object):

    def __init__(self):
        super(EULAVersionLoader, self).__init__()
        self.__xmlVersion = 0
        self.loadXMLVersion()

    @property
    def xmlVersion(self):
        return self.__xmlVersion

    def loadXMLVersion(self):
        xmlFile = ResMgr.openSection(VERSION_FILE_PATH)
        if not xmlFile:
            raise Exception('EULAVersionLoader.loadXMLVersion %s file is missing' % VERSION_FILE_PATH)
        xmlVersion = xmlFile.readString(VERSION_TAG)
        if not xmlVersion:
            raise Exception('Subsection EULAVersionLoader.loadXMLVersion EULAVersion tag <%(ver)s> is missing or empty in %(path)s' % {'ver': VERSION_TAG,
             'path': VERSION_FILE_PATH})
        self.__xmlVersion = int(xmlVersion)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\doc_loaders\EULAVersionLoader.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:48:09 St�edn� Evropa (b�n� �as)
