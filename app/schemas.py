from enum import StrEnum


class WeaponType(StrEnum):
    bow = 'bow'
    catalyst = 'catalyst'
    claymore = 'claymore'
    polearm = 'polearm'
    sword = 'sword'


class Element(StrEnum):
    anemo = 'anemo'
    cryo = 'cryo'
    dendro = 'dendro'
    electro = 'electro'
    geo = 'geo'
    hydro = 'hydro'
    pyro = 'pyro'
