import json

def offset_positions(original_point, positions, new_point):
    # Calculate offsets
    offsets = [
        {
            "heading": pos["heading"],
            "x_offset": pos["x"] - original_point["x"],
            "y_offset": pos["y"] - original_point["y"]
        }
        for pos in positions
    ]

    # Apply offsets to the new point
    new_positions = [
        {
            "heading": offset["heading"],
            "x": new_point["x"] + offset["x_offset"],
            "y": new_point["y"] + offset["y_offset"]
        }
        for offset in offsets
    ]

    return new_positions

# Example usage
original_point = { "x": -25737.909511595, "y": -292207.07941827 }
positions = [
    {"heading": 10, "x": -25863.571765621, "y": -292217.32354961},
    {"heading": 333, "x": -25861.256932766, "y": -292187.2885479},
    {"heading": 324, "x": -25853.4374652, "y": -292161.28881824},
    {"heading": 322, "x": -25839.362423582, "y": -292134.31165514}
]

farps = {
    "FARP-1": {
        "clearScenery": "",
        "component": "farp",
        "label": "FARP Pissouri",
        "radius": 137.16,
        "ship_groups": [],
        "static_groups": [
            "MASH Tent 1",
            "MASH Tent 1-1",
            "Static Container 20ft-2",
            "Static Container 20ft-3",
            "Static Container 20ft-4",
            "Static FARP Tent-5",
            "Static FARP Tent-6",
            "Static FARP Tent-7",
            "Static FARP Tent-8",
            "Static Invisible FARP-1",
            "Static Invisible FARP-2",
            "Static Invisible FARP-3",
            "Static Invisible FARP-4",
            "Static Watch tower armed-3",
            "Static Windsock-1"
        ],
        "vehicle_groups": [
            "FARP MASH 1-2",
            "FARP Support 1-1",
            "FARP Support 1-2",
            "FARP Support 1-3"
        ],
        "x": -25737.909511595,
        "y": -292207.07941827
    },
    "FARP-2": {
        "clearScenery": "",
        "component": "farp",
        "label": "FARP Pyrgos",
        "radius": 137.16,
        "ship_groups": [],
        "static_groups": [
            "MASH Tent 1-2",
            "MASH Tent 1-3",
            "Static Container 20ft-5",
            "Static Container 20ft-6",
            "Static Container 20ft-7",
            "Static FARP Tent-10",
            "Static FARP Tent-11",
            "Static FARP Tent-12",
            "Static FARP Tent-9",
            "Static Invisible FARP-5",
            "Static Invisible FARP-6",
            "Static Invisible FARP-7",
            "Static Windsock-2",
            "Static Watch tower armed-4",
            "Static Invisible FARP-8"
        ],
        "vehicle_groups": [
            "FARP MASH 1-1",
            "FARP Support 1-4",
            "FARP Support 1-5",
            "FARP Support 1-6"
        ],
        "x": -23200.163973475,
        "y": -249853.70558637
    },
    "FARP-3": {
        "clearScenery": "",
        "component": "farp",
        "label": "FARP Stavrovouni",
        "radius": 137.16,
        "ship_groups": [],
        "static_groups": [
            "MASH Tent 1-4",
            "MASH Tent 1-5",
            "Static Container 20ft-10",
            "Static Container 20ft-8",
            "Static Container 20ft-9",
            "Static FARP Tent-13",
            "Static FARP Tent-14",
            "Static FARP Tent-15",
            "Static FARP Tent-16",
            "Static Invisible FARP-10",
            "Static Invisible FARP-11",
            "Static Invisible FARP-12",
            "Static Invisible FARP-9",
            "Static Windsock-3",
            "Static Watch tower armed-5"
        ],
        "vehicle_groups": [
            "FARP MASH 1-6",
            "FARP Support 1-7",
            "FARP Support 1-8",
            "FARP Support 1-9"
        ],
        "x": -3336.6090235222,
        "y": -224855.22756355
    },
    "FARP-4": {
        "clearScenery": "",
        "component": "farp",
        "label": "FARP Xylofagou",
        "radius": 137.16,
        "ship_groups": [],
        "static_groups": [
            "MASH Tent 1-6",
            "MASH Tent 1-7",
            "Static Container 20ft-11",
            "Static Container 20ft-12",
            "Static Container 20ft-13",
            "Static FARP Tent-19",
            "Static FARP Tent-20",
            "Static FARP Tent-21",
            "Static FARP Tent-22",
            "Static Invisible FARP-13",
            "Static Invisible FARP-14",
            "Static Invisible FARP-15",
            "Static Invisible FARP-16",
            "Static Watch tower armed-6",
            "Static Windsock-4"
        ],
        "vehicle_groups": [
            "FARP MASH 1-19",
            "FARP Support 1-10",
            "FARP Support 1-11",
            "FARP Support 1-12"
        ],
        "x": -375.02760177519,
        "y": -185831.77743075
    },
    "FARP-5": {
        "clearScenery": "all",
        "component": "farp",
        "label": "FARP Pano Akourdaleia",
        "radius": 137.16,
        "ship_groups": [],
        "static_groups": [
            "MASH Tent 1-8",
            "MASH Tent 1-9",
            "Static Container 20ft-14",
            "Static Container 20ft-15",
            "Static Container 20ft-16",
            "Static FARP Tent-30",
            "Static FARP Tent-31",
            "Static FARP Tent-32",
            "Static FARP Tent-33",
            "Static Invisible FARP-17",
            "Static Invisible FARP-18",
            "Static Invisible FARP-19",
            "Static Invisible FARP-20",
            "Static Watch tower armed-7",
            "Static Windsock-5"
        ],
        "vehicle_groups": [
            "FARP MASH 1-20",
            "FARP Support 1-13",
            "FARP Support 1-14",
            "FARP Support 1-15"
        ],
        "x": 6326.3432897668,
        "y": -316178.25561954
    }
}

for farpname, farp in farps.items():
    new_point = { "x": farp["x"], "y": farp["y"] }
    new_positions = offset_positions(original_point, positions, new_point)
    print(farpname)
    print(json.dumps(new_positions, separators=(',', ':')))