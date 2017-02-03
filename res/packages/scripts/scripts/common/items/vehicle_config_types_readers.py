# 2017.02.03 21:55:39 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/items/vehicle_config_types_readers.py
from items import _xml
import vehicle_config_types

def readLodDist(xmlCtx, section, subsectionName):
    from items.vehicles import g_cache
    name = _xml.readNonEmptyString(xmlCtx, section, subsectionName)
    dist = g_cache.commonConfig['lodLevels'].get(name)
    if dist is None:
        _xml.raiseWrongXml(xmlCtx, subsectionName, "unknown lod level '%s'" % name)
    return dist


def readLodSettings(xmlCtx, section):
    return vehicle_config_types.LodSettings(readLodDist(xmlCtx, section, 'lodSettings/maxLodDistance'), _xml.readIntOrNone(xmlCtx, section, 'lodSettings/maxPriority'))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\common\items\vehicle_config_types_readers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:55:39 Støední Evropa (bìžný èas)
