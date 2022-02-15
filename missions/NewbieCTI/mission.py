import dcs
import calvinball

class NewbieCTI(calvinball.mission.Mission):
    def __init__(self) -> None:
        t = dcs.terrain.Caucasus()
        miz_name = "NewbieCTI"
        ctld = NewbieCTICtld()
        clients = NewbieCTIClients()
        red_airwings = NewbieCTIRedAirwings()
        blue_airwings = NewbieCTIBlueAirwings()

        super().__init__(t, miz_name, ctld, clients, red_airwings, blue_airwings)

class NewbieCTICtld(calvinball.ctld.Ctld):
    def build(self, m: dcs.Mission):
        super().build(m)

class NewbieCTIClients(calvinball.clients.Clients):
    def define(self, m: dcs.Mission, edit: bool):
        m.groundControl.blue_game_masters = 1
        return []

class NewbieCTIRedAirwings(calvinball.redairwing.RedAirwings):
    def define(self, m: dcs.Mission):
        return {}

class NewbieCTIBlueAirwings(calvinball.blueairwing.BlueAirwings):
    def define(self, m: dcs.Mission):
        return {}