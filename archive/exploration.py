import dcs
from prettytable import PrettyTable
import csv


def airport_slots():
    csv_rows = []
    field_names = ["Terrain", "Airport", "Total", "Large", "Helo", "Is Civilian?"]

    slots_table = PrettyTable()
    slots_table.field_names = field_names
    slots_table.sortby = "Total"
    slots_table.reversesort = True

    terrains = [dcs.terrain.Syria(), dcs.terrain.Caucasus(), dcs.terrain.Falklands(), dcs.terrain.MarianaIslands(), dcs.terrain.Nevada(), dcs.terrain.Normandy(), dcs.terrain.PersianGulf(), dcs.terrain.TheChannel()]
    for t in terrains:
        # if t.name != "Syria":
        #     continue
        for x in t.airports.values():
            large = len(x.free_parking_slots(dcs.planes.C_130))
            helo = sum(s.helicopter for s in x.parking_slots)
            total = len(x.parking_slots)
            slots_table.add_row([t.name, x.name, total, large, helo, x.civilian])
            csv_rows.append([t.name, x.name, total, large, helo, x.civilian])

    print(slots_table)

    with open("airport-slots.csv", "w", newline='') as outfile:
        w = csv.writer(outfile)
        w.writerow(field_names)
        w.writerows(csv_rows)

def playable_aircraft():
    field_names = ["Airframe", "Max Speed (km/h)", "Max Fuel"]

    table = PrettyTable()
    table.field_names = field_names
    table.sortby = "Max Speed (km/h)"
    table.reversesort = True

    for p in dcs.planes.plane_map.values():
        if(p.flyable):
            table.add_row([p.id, round(p.max_speed), round(p.fuel_max)])

    print(table)

def parking_slot_names(airport: dcs.terrain.Airport):
    table = PrettyTable()
    table.field_names = ["Name", "ID", "Helo"]
    table.sortby = "Name"

    for p in airport.parking_slots:
        table.add_row([p.slot_name, p.crossroad_idx, p.helicopter,])

    print(table)

def livery_ids(a):
    table = PrettyTable()
    table.field_names = ["Name"]
    table.sortby = "Name"

    for p in a.Liveries:
        print(p)
        table.add_row([p])

    print(table)

def radios():
    csv_rows = []
    field_names = ["Airframe", "Radio", "Channel", "Frequency"]

    table = PrettyTable()
    table.field_names = field_names
    table.sortby = "Airframe"

    for p in dcs.planes.plane_map.values():
        if(p.flyable):
            if p.panel_radio:
                for radioid, channels in p.panel_radio.items():
                    for c,f in sorted(channels["channels"].items()):
                        table.add_row([p.id, radioid, c, f])
                        csv_rows.append([p.id, radioid, c, f])
            else:
                table.add_row([p.id, None, None, p.radio_frequency])
                csv_rows.append([p.id, None, None, p.radio_frequency])
                    

    for p in dcs.helicopters.helicopter_map.values():
        if(p.flyable):
            if p.panel_radio:
                for radioid, channels in p.panel_radio.items():
                    for c,f in sorted(channels["channels"].items()):
                        table.add_row([p.id, radioid, c, f])
                        csv_rows.append([p.id, radioid, c, f])
            else:
                table.add_row([p.id, None, None, p.radio_frequency])
                csv_rows.append([p.id, None, None, p.radio_frequency])
    
    print(table)

    # with open("radios.csv", "w", newline='') as outfile:
    #     w = csv.writer(outfile)
    #     w.writerow(field_names)
    #     w.writerows(csv_rows)

#parking_slot_names(dcs.terrain.Normandy().airports["Needs Oar Point"])
#parking_slot_names(dcs.terrain.Syria().airports["Paphos"])
#parking_slot_names(dcs.terrain.Syria().airports["Larnaca"])
#livery_ids(dcs.helicopters.AH_64D_BLK_II)

#airport_slots()
#playable_aircraft()

#parking_slot_names(dcs.terrain.Caucasus().airports["Batumi"])

#radios()

#parking_slot_names(dcs.terrain.Normandy().airports["Needs Oar Point"])
#parking_slot_names(dcs.terrain.PersianGulf().airports["Al Dhafra AFB"])
parking_slot_names(dcs.terrain.GermanyColdWar().airports["Ramstein"])


#print(dcs.mapping.Point.from_latlng(dcs.mapping.LatLng(50.66526, -2.63873), dcs.terrain.Normandy()))