from missions.CyprusInvasion.mission import CyprusInvasion
from missions.DangerZone.mission import DangerZone
from missions.GeorgianOffensive.mission import GeorgianOffensive
from missions.AndeanAbyss.mission import AndeanAbyss

missions = [CyprusInvasion(), DangerZone(), GeorgianOffensive(), AndeanAbyss()]
for m in missions:
    m.build(True, False, True)
