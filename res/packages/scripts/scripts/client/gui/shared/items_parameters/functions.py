# 2017.02.03 21:52:37 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/shared/items_parameters/functions.py
from operator import itemgetter
from items import utils, tankmen

def getVehicleFactors(vehicle):
    factors = utils.makeDefaultVehicleAttributeFactors()
    vehicleDescr = vehicle.descriptor
    eqs = [ eq.descriptor for eq in vehicle.eqs if eq is not None ]
    crewCompactDescrs = extractCrewDescrs(vehicle)
    utils.updateAttrFactorsWithSplit(vehicleDescr, crewCompactDescrs, eqs, factors)
    return factors


def extractCrewDescrs(vehicle, replaceNone = True):
    crewCompactDescrs = []
    emptySlots = []
    otherVehicleSlots = []
    vehicleDescr = vehicle.descriptor
    for idx, tankman in sorted(vehicle.crew, key=itemgetter(0)):
        if tankman is not None:
            if hasattr(tankman, 'strCompactDescr'):
                tankmanDescr = tankman.strCompactDescr
                if tankman.efficiencyRoleLevel < tankman.roleLevel:
                    otherVehicleSlots.append(idx)
            else:
                tankmanDescr = tankman
        elif not replaceNone:
            tankmanDescr = None
            emptySlots.append(idx)
        else:
            role = vehicleDescr.type.crewRoles[idx][0]
            tankmanDescr = createFakeTankmanDescr(role, vehicleDescr.type)
        crewCompactDescrs.append(tankmanDescr)

    if replaceNone:
        return crewCompactDescrs
    else:
        return (crewCompactDescrs, emptySlots, otherVehicleSlots)
        return


def createFakeTankmanDescr(role, vehicleType, roleLevel = 100):
    nationID, vehicleTypeID = vehicleType.id
    passport = tankmen.generatePassport(nationID)
    return tankmen.generateCompactDescr(passport, vehicleTypeID, role, roleLevel)


def getBasicShell(vehDescr):
    """
        basic is shell which goes first in XML describing particular gun
    """
    return vehDescr.gun['shots'][0]['shell']
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\shared\items_parameters\functions.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:52:37 St�edn� Evropa (b�n� �as)
