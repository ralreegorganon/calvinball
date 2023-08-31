from missions.CyprusInvasion.mission import CyprusInvasion
from missions.DangerZone.mission import DangerZone
from missions.GeorgianOffensive.mission import GeorgianOffensive

m = CyprusInvasion()
m.build(True, False)

m = DangerZone()
m.build(True, False)

m = GeorgianOffensive()
m.build(True, False)