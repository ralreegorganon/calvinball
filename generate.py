import argparse

from missions.CyprusInvasion.mission import CyprusInvasion
from missions.DangerZone.mission import DangerZone
from missions.GeorgianOffensive.mission import GeorgianOffensive
from missions.AndeanAbyss.mission import AndeanAbyss
from missions.RockTheCasbah.mission import RockTheCasbah
from missions.AcesHigh.mission import AcesHigh

parser = argparse.ArgumentParser()
parser.add_argument("--edit", action=argparse.BooleanOptionalAction, default=True, help="Generate for editing in the ME")
parser.add_argument("--package", action=argparse.BooleanOptionalAction, default=False, help="Package scripts in mission")
parser.add_argument("--debug", action=argparse.BooleanOptionalAction, default=True, help="Enable debug menu")
args = parser.parse_args()

missions = [CyprusInvasion(), DangerZone(), GeorgianOffensive(), AndeanAbyss(), RockTheCasbah(), AcesHigh()]
for m in missions:
    m.build(args.edit, args.package, args.debug)
