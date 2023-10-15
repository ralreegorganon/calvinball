# import dcs
# from prettytable import PrettyTable

# m = dcs.Mission(terrain=dcs.terrain.Falklands())
# m.load_file("C:/Users/jj/Saved Games/DCS.openbeta/Missions/The_Long_Afternoon_War_template_v4.miz")

# common_layer = m.drawings.get_layer(dcs.drawing.drawings.StandardLayer.Common)
# b = dcs.mapping.Point(m.coalition["blue"].bullseye["x"], m.coalition["blue"].bullseye["y"], m.terrain)

# for a in m.terrain.airports.values():
#     common_layer.add_text_box(a.position, f"{round(b.heading_between_point(a.position)):03d} / {round(a.position.distance_to_point(b)/1852)}", dcs.drawing.Rgba(0, 0, 128, 255), dcs.drawing.Rgba(255, 255, 255, 128), 24, border_thickness=4)

# common_layer.add_circle(b, 1852*25, dcs.drawing.Rgba(0, 0, 0, 255), dcs.drawing.Rgba(0, 0, 0, 0), 2, dcs.drawing.LineStyle.Solid)
# common_layer.add_circle(b, 1852*50, dcs.drawing.Rgba(0, 0, 0, 255), dcs.drawing.Rgba(0, 0, 0, 0), 4, dcs.drawing.LineStyle.Solid)
# common_layer.add_circle(b, 1852*75, dcs.drawing.Rgba(0, 0, 0, 255), dcs.drawing.Rgba(0, 0, 0, 0), 2, dcs.drawing.LineStyle.Solid)
# common_layer.add_circle(b, 1852*100, dcs.drawing.Rgba(0, 0, 0, 255), dcs.drawing.Rgba(0, 0, 0, 0), 8, dcs.drawing.LineStyle.Solid)
# common_layer.add_circle(b, 1852*150, dcs.drawing.Rgba(0, 0, 0, 255), dcs.drawing.Rgba(0, 0, 0, 0), 4, dcs.drawing.LineStyle.Solid)
# common_layer.add_circle(b, 1852*200, dcs.drawing.Rgba(0, 0, 0, 255), dcs.drawing.Rgba(0, 0, 0, 0), 8, dcs.drawing.LineStyle.Solid)

# for angle in range(0, 360, 45):
#     p = b.point_from_heading(angle, 1852*200) 
#     common_layer.add_line_segment(b, p - b, dcs.drawing.Rgba(0, 0, 0, 255), 12, dcs.drawing.LineStyle.Dot)
#     common_layer.add_text_box(p, f"{angle}", dcs.drawing.Rgba(0, 0, 128, 255), dcs.drawing.Rgba(255, 255, 255, 128), 24, border_thickness=4)

# m.save("C:/Users/jj/Saved Games/DCS.openbeta/Missions/The_Long_Afternoon_War_template_v4_altered.miz")


# import dcs
# from geographiclib.geodesic import Geodesic
# from prettytable import PrettyTable


# def dcs_point_from_heading(dcs_point, heading, distance):
#     geod = Geodesic.WGS84
#     point = dcs_point.latlng()
#     g = geod.Direct(point.lat, point.lng, heading, distance)
#     return dcs.mapping.Point.from_latlng(dcs.mapping.LatLng(g["lat2"], g["lon2"]), dcs_point._terrain)

# def heading_and_distance_between_points(dcs_point1, dcs_point2):
#     geod = Geodesic.WGS84
#     point1 = dcs_point1.latlng()
#     point2 = dcs_point2.latlng()
#     g = geod.Inverse(point1.lat, point1.lng, point2.lat, point2.lng)
#     return ((g["azi1"]+360) % 360, g["s12"])

# m = dcs.Mission(terrain=dcs.terrain.Falklands())
# m.load_file("C:/Users/jj/Saved Games/DCS.openbeta/Missions/TempTest.miz")

# common_layer = m.drawings.get_layer(dcs.drawing.drawings.StandardLayer.Common)
# b = dcs.mapping.Point(m.coalition["blue"].bullseye["x"], m.coalition["blue"].bullseye["y"], m.terrain)

# geod = Geodesic.WGS84

# for a in m.terrain.airports.values():
#     x = heading_and_distance_between_points(b, a.position)
#     common_layer.add_text_box(a.position, f"DCS: {round(b.heading_between_point(a.position)):03d} / {round(a.position.distance_to_point(b)/1852)}\nGEO: {round(x[0]):03d} / {round(x[1]/1852)}", dcs.drawing.Rgba(0, 0, 128, 255), dcs.drawing.Rgba(255, 255, 255, 128), 24, border_thickness=4)

# common_layer.add_circle(b, 1852*25, dcs.drawing.Rgba(0, 0, 0, 255), dcs.drawing.Rgba(0, 0, 0, 0), 2, dcs.drawing.LineStyle.Solid)
# common_layer.add_circle(b, 1852*50, dcs.drawing.Rgba(0, 0, 0, 255), dcs.drawing.Rgba(0, 0, 0, 0), 4, dcs.drawing.LineStyle.Solid)
# common_layer.add_circle(b, 1852*75, dcs.drawing.Rgba(0, 0, 0, 255), dcs.drawing.Rgba(0, 0, 0, 0), 2, dcs.drawing.LineStyle.Solid)
# common_layer.add_circle(b, 1852*100, dcs.drawing.Rgba(0, 0, 0, 255), dcs.drawing.Rgba(0, 0, 0, 0), 8, dcs.drawing.LineStyle.Solid)
# common_layer.add_circle(b, 1852*150, dcs.drawing.Rgba(0, 0, 0, 255), dcs.drawing.Rgba(0, 0, 0, 0), 4, dcs.drawing.LineStyle.Solid)
# common_layer.add_circle(b, 1852*200, dcs.drawing.Rgba(0, 0, 0, 255), dcs.drawing.Rgba(0, 0, 0, 0), 8, dcs.drawing.LineStyle.Solid)

# for angle in range(0, 360, 45):
#     p = dcs_point_from_heading(b, angle, 1852*200) 
#     common_layer.add_line_segment(b, p - b, dcs.drawing.Rgba(0, 0, 0, 255), 12, dcs.drawing.LineStyle.Dot)
#     common_layer.add_text_box(p, f"{angle}", dcs.drawing.Rgba(0, 0, 128, 255), dcs.drawing.Rgba(255, 255, 255, 128), 24, border_thickness=4)

#     pz = b.point_from_heading(angle, 1852*200) 
#     common_layer.add_line_segment(b, pz - b, dcs.drawing.Rgba(255, 255, 255, 255), 12, dcs.drawing.LineStyle.Dot)

# m.save("C:/Users/jj/Saved Games/DCS.openbeta/Missions/The_Long_Afternoon_War_template_v4_altered.miz")



# t = PrettyTable()
# t.field_names = ["Airport", "Bullseye", "Distance"]
# t.sortby = "Distance"

# m = dcs.Mission(terrain=dcs.terrain.Falklands())
# m.load_file("C:/Users/jj/Saved Games/DCS.openbeta/Missions/The_Long_Afternoon_War_template_v4.miz")
# b = dcs.mapping.Point(m.coalition["blue"].bullseye["x"], m.coalition["blue"].bullseye["y"], m.terrain)
# for a in m.terrain.airports.values():
#     t.add_row([a.name, f"{round(a.position.heading_between_point(b))} / {round(a.position.distance_to_point(b)/1852)}", round(a.position.distance_to_point(b)/1852)])

# print(t)


import dcs
from prettytable import PrettyTable

m = dcs.Mission(terrain=dcs.terrain.Falklands())
m.load_file("C:/Users/jj/Saved Games/DCS.openbeta/Missions/TempTest.miz")

common_layer = m.drawings.get_layer(dcs.drawing.drawings.StandardLayer.Common)
b = dcs.mapping.Point(m.coalition["blue"].bullseye["x"], m.coalition["blue"].bullseye["y"], m.terrain)

for a in m.terrain.airports.values():
    common_layer.add_text_box(a.position, f"{round(b.heading_between_point(a.position)):03d} / {round(a.position.distance_to_point(b)/1852)}", dcs.drawing.Rgba(0, 0, 128, 255), dcs.drawing.Rgba(255, 255, 255, 128), 24, border_thickness=4)

rings = [25, 50, 75, 100, 150, 200]
radial = 10

for distance in rings:
    thick = 1
    if distance % 100 == 0:
        thick = 8
    elif distance % 50 == 0:
        thick = 4
    elif distance % 25 == 0:
        thick = 2
    
    common_layer.add_circle(b, 1852*distance, dcs.drawing.Rgba(0, 0, 0, 255), dcs.drawing.Rgba(0, 0, 0, 0), thick, dcs.drawing.LineStyle.Solid)

for angle in range(0, 360, radial):
    p = b.point_from_heading(angle, 1852*rings[-1]) 
    common_layer.add_line_segment(b, p - b, dcs.drawing.Rgba(0, 0, 0, 255), 12, dcs.drawing.LineStyle.Dot)
    common_layer.add_text_box(p, f"{angle}", dcs.drawing.Rgba(0, 0, 128, 255), dcs.drawing.Rgba(255, 255, 255, 128), 24, border_thickness=4)

m.save("C:/Users/jj/Saved Games/DCS.openbeta/Missions/TempTest_altered.miz")