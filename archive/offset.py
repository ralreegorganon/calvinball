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
#positions = [{"heading":10,"x":-25863.571765621,"y":-292217.32354961},{"heading":333,"x":-25861.256932766,"y":-292187.2885479},{"heading":324,"x":-25853.4374652,"y":-292161.28881824},{"heading":322,"x":-25839.362423582,"y":-292134.31165514}]
positions = [{"heading": 314, "x": -25824.327728835, "y": -292122.82881144}, {"heading": 305, "x": -25804.185984264, "y": -292107.27380078}, {"heading": 299, "x": -25784.749804378, "y": -292096.26890616}, {"heading": 289, "x": -25763.083701189, "y": -292087.69466107}]

farps = {
     "FARP-1": {
        "clearScenery": "all",
        "component": "farp",
        "label": "FARP Puhdys",
        "radius": 137.16,
        "ship_groups": [],
        "static_groups": [
            "Static Invisible FARP-4",
            "Static Container 20ft-3",
            "Static FARP Tent-7",
            "Static Invisible FARP-2",
            "Static Invisible FARP-3",
            "Static Watch tower armed-3",
            "Static Windsock-1",
            "MASH Tent 1-1",
            "Static Container 20ft-2",
            "Static Container 20ft-4",
            "MASH Tent 1",
            "Static FARP Tent-8",
            "Static FARP Tent-6",
            "Static Invisible FARP-1",
            "Static FARP Tent-5"
        ],
        "vehicle_groups": [
            "FARP MASH 1-6",
            "FARP Support 1-3",
            "FARP Support 1-2",
            "FARP Support 1-1"
        ],
        "x": -525188.78516044,
        "y": -879104.51568112
    }
}

for farpname, farp in farps.items():
    new_point = { "x": farp["x"], "y": farp["y"] }
    new_positions = offset_positions(original_point, positions, new_point)
    print(farpname)
    print(json.dumps(new_positions, separators=(',', ':')))