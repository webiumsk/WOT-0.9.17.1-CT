# 2017.02.03 21:55:33 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/items/utils.py
import copy
from operator import sub
from constants import IS_CLIENT, VEHICLE_TTC_ASPECTS
from items import tankmen
from items.qualifiers import QUALIFIER_TYPE
from items.tankmen import MAX_SKILL_LEVEL, MIN_ROLE_LEVEL
from items.vehicles import VEHICLE_ATTRIBUTE_FACTORS, CAMOUFLAGE_KIND_INDICES
from VehicleDescrCrew import VehicleDescrCrew
from VehicleQualifiersApplier import VehicleQualifiersApplier
from debug_utils import *

def _makeDefaultVehicleFactors(sample):
    """It's a simple analog of copy.deepcopy to make copy of default factors,
    but too faster than copy.deepcopy.
    :param sample: dict containing sample that should be copy.
    :return: dict containing copy of sample.
    """
    default = {}
    for key, value in sample.iteritems():
        if value is None:
            default[key] = value
        elif isinstance(value, (float,
         int,
         long,
         str)):
            default[key] = value
        elif isinstance(value, (list, tuple)):
            default[key] = value[:]
        else:
            LOG_ERROR('Default value of vehicle attribute can not be resolved', key, value)

    return default


def makeDefaultVehicleAttributeFactors():
    """Make copy of VEHICLE_ATTRIBUTE_FACTORS."""
    return _makeDefaultVehicleFactors(VEHICLE_ATTRIBUTE_FACTORS)


def isclose(a, b, rel_tol = 1e-09, abs_tol = 0.0):
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def generateDefaultCrew(vehicleType, level):
    raise 0 <= level <= tankmen.MAX_SKILL_LEVEL or AssertionError
    nationID, vehicleTypeID = vehicleType.id
    skills = ()
    passport = (nationID,
     False,
     False,
     0,
     0,
     0)
    res = []
    for roles in vehicleType.crewRoles:
        cd = tankmen.generateCompactDescr(passport, vehicleTypeID, roles[0], level, skills, level)
        res.append(tankmen.stripNonBattle(cd))

    return tuple(res)


def _generateTankman(vehicleDescr, roles, level):
    nationID, vehicleTypeID = vehicleDescr.type.id
    passport = (nationID,
     False,
     False,
     0,
     0,
     0)
    skills = ()
    return tankmen.stripNonBattle(tankmen.generateCompactDescr(passport, vehicleTypeID, roles[0], level, skills, level))


def _replaceMissingTankmenWithDefaultOnes(vehicleDescr, crewCompactDescrs, level = MAX_SKILL_LEVEL):
    result = []
    for tankmanCompactDescr, roles in zip(crewCompactDescrs, vehicleDescr.type.crewRoles):
        if tankmanCompactDescr is None:
            result.append(_generateTankman(vehicleDescr, roles, level))
        else:
            result.append(tankmanCompactDescr)

    return result


def getRadioDistance(vehicleDescr, factors):
    return vehicleDescr.radio['distance'] * max(factors['radio/distance'], 0.0)


def getCircularVisionRadius(vehicleDescr, factors):
    return vehicleDescr.turret['circularVisionRadius'] * vehicleDescr.miscAttrs['circularVisionRadiusFactor'] * max(factors['circularVisionRadius'], 0.0)


def getReloadTime(vehicleDescr, factors):
    return vehicleDescr.gun['reloadTime'] * vehicleDescr.miscAttrs['gunReloadTimeFactor'] * max(factors['gun/reloadTime'], 0.0)


def getTurretRotationSpeed(vehicleDescr, factors):
    return vehicleDescr.turret['rotationSpeed'] * max(factors['turret/rotationSpeed'], 0.0)


def getGunRotationSpeed(vehicleDescr, factors):
    return vehicleDescr.gun['rotationSpeed'] * max(factors['gun/rotationSpeed'], 0.0)


def getGunAimingTime(vehicleDescr, factors):
    return vehicleDescr.gun['aimingTime'] * vehicleDescr.miscAttrs['gunAimingTimeFactor'] * max(factors['gun/aimingTime'], 0.0)


def getChassisRotationSpeed(vehicleDescr, factors):
    return vehicleDescr.chassis['rotationSpeed'] * max(factors['vehicle/rotationSpeed'], 0.0)


def getInvisibility(factors, baseInvisibility, isMoving):
    return (baseInvisibility[0 if isMoving else 1] + factors['invisibility'][0]) * factors['invisibility'][1]


def getEnginePower(vehicleDescr, factor):
    return vehicleDescr.physics['enginePower'] * factor


if IS_CLIENT:
    CLIENT_VEHICLE_ATTRIBUTE_FACTORS = {'camouflage': 1.0,
     'shotDispersion': 1.0}
    CLIENT_VEHICLE_ATTRIBUTE_FACTORS.update(VEHICLE_ATTRIBUTE_FACTORS)

    def makeDefaultClientVehicleAttributeFactors():
        """Make copy of CLIENT_VEHICLE_ATTRIBUTE_FACTORS."""
        return _makeDefaultVehicleFactors(CLIENT_VEHICLE_ATTRIBUTE_FACTORS)


    def _isFactor(a):
        return isinstance(a, (int, long, float))


    def _comparableFactors(original, changed):
        if all((isinstance(x, list) for x in (original, changed))):
            return all((_isFactor(a) and _isFactor(b) for a, b in zip(original, changed)))
        else:
            return _isFactor(original) and _isFactor(changed)


    def _compareFactors(original, changed):
        result = {}
        for factor in original.iterkeys():
            if not _comparableFactors(original[factor], changed[factor]):
                continue
            if all((isinstance(x, list) for x in (original[factor], changed[factor]))):
                if not all(map(isclose, original[factor], changed[factor])):
                    result[factor] = map(sub, original[factor], changed[factor])
            elif not isclose(original[factor], changed[factor]):
                result[factor] = original.get(factor, CLIENT_VEHICLE_ATTRIBUTE_FACTORS[factor]) - changed[factor]

        return result


    def getClientShotDispersion(vehicleDescr, shotDispersionFactor):
        return vehicleDescr.gun['shotDispersionAngle'] * shotDispersionFactor


    def getClientInvisibility(vehicleDescr, camouflageFactor, factors):
        camouflageKind = 0
        for camouflageIndex, camouflageName in CAMOUFLAGE_KIND_INDICES.iteritems():
            if vehicleDescr.camouflages[camouflageIndex][0] is not None:
                camouflageKind = camouflageIndex
                break

        baseInvisibility = vehicleDescr.computeBaseInvisibility(camouflageFactor, camouflageKind)
        invisibilityFactors = factors['invisibility']
        factors['invisibility'] = invisibilityFactors[VEHICLE_TTC_ASPECTS.DEFAULT]
        moving = getInvisibility(factors, baseInvisibility, True)
        factors['invisibility'] = invisibilityFactors[VEHICLE_TTC_ASPECTS.WHEN_STILL]
        still = getInvisibility(factors, baseInvisibility, False)
        factors['invisibility'] = invisibilityFactors
        return (moving, still)


    def updateAttrFactorsWithSplit(vehicleDescr, crewCompactDescrs, eqs, factors):
        extras = {}
        extraAspects = {VEHICLE_TTC_ASPECTS.WHEN_STILL: ('invisibility',)}
        updateVehicleAttrFactors(vehicleDescr, crewCompactDescrs, eqs, factors, VEHICLE_TTC_ASPECTS.DEFAULT)
        for aspect in extraAspects.keys():
            currFactors = copy.deepcopy(factors)
            updateVehicleAttrFactors(vehicleDescr, crewCompactDescrs, eqs, currFactors, aspect)
            for coefficient in extraAspects[aspect]:
                extras.setdefault(coefficient, {})[aspect] = currFactors[coefficient]

        for coefficientName, coefficientValue in extras.iteritems():
            coefficientValue[VEHICLE_TTC_ASPECTS.DEFAULT] = factors[coefficientName]
            factors[coefficientName] = coefficientValue


    def getCrewAffectedFactors(vehicleDescr, crewCompactDescrs):
        defaultCrewCompactDescrs = _replaceMissingTankmenWithDefaultOnes(vehicleDescr, crewCompactDescrs)
        defaultFactors = makeDefaultClientVehicleAttributeFactors()
        updateAttrFactorsWithSplit(vehicleDescr, defaultCrewCompactDescrs, [], defaultFactors)
        result = {}
        for i, (tankmanCompactDescr, roles) in enumerate(zip(crewCompactDescrs, vehicleDescr.type.crewRoles)):
            backupedtankmanCompactDescr = defaultCrewCompactDescrs[i]
            defaultCrewCompactDescrs[i] = _generateTankman(vehicleDescr, roles, MIN_ROLE_LEVEL if tankmanCompactDescr is None else MAX_SKILL_LEVEL)
            tankmanAffectedFactors = makeDefaultClientVehicleAttributeFactors()
            updateAttrFactorsWithSplit(vehicleDescr, defaultCrewCompactDescrs, [], tankmanAffectedFactors)
            changedFactors = _compareFactors(tankmanAffectedFactors, defaultFactors)
            if changedFactors:
                result[i] = changedFactors
            defaultCrewCompactDescrs[i] = backupedtankmanCompactDescr

        return result


    def _sumCrewLevelIncrease(eqs):
        return sum(filter(None, [ getattr(eq, 'crewLevelIncrease', None) for eq in eqs ]))


    def updateVehicleAttrFactors(vehicleDescr, crewCompactDescrs, eqs, factors, aspect):
        factors['crewLevelIncrease'] = _sumCrewLevelIncrease(eqs)
        for eq in eqs:
            if eq is not None:
                eq.updateVehicleAttrFactors(factors)

        for device in vehicleDescr.optionalDevices:
            if device is not None:
                device.updateVehicleAttrFactors(vehicleDescr, factors, aspect)

        mainSkillBonuses = VehicleQualifiersApplier({}, vehicleDescr)[QUALIFIER_TYPE.MAIN_SKILL]
        vehicleDescrCrew = VehicleDescrCrew(vehicleDescr, crewCompactDescrs, mainSkillBonuses)
        vehicleDescrCrew.onCollectFactors(factors)
        factors['camouflage'] = vehicleDescrCrew.camouflageFactor
        shotDispersionFactors = [1.0, 0.0]
        vehicleDescrCrew.onCollectShotDispersionFactors(shotDispersionFactors)
        factors['shotDispersion'] = shotDispersionFactors
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\common\items\utils.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:55:34 St�edn� Evropa (b�n� �as)
