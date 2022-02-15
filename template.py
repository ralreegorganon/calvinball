from missions.CyprusInvasion.mission import CyprusInvasion
from calvinball.utility import build_sam_templates
import dcs

c = CyprusInvasion()


m = dcs.mission.Mission()
m.load_file(c.miz_export_path)
build_sam_templates(m)
m.save()