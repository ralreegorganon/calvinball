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
        "label": "FARP Portland Bill",
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
        "x": 111531.35177591,
        "y": -157069.50280131
    },
    "FARP-2": {
        "clearScenery": "all",
        "component": "farp",
        "label": "FARP Morden Bog",
        "radius": 137.16,
        "ship_groups": [],
        "static_groups": [
            "MASH Tent 1-2",
            "MASH Tent 1-3",
            "Static Container 20ft-1",
            "Static Container 20ft-5",
            "Static Container 20ft-6",
            "Static FARP Tent-13",
            "Static FARP Tent-14",
            "Static FARP Tent-15",
            "Static FARP Tent-18",
            "Static Invisible FARP-5",
            "Static Invisible FARP-6",
            "Static Invisible FARP-7",
            "Static Invisible FARP-8",
            "Static Watch tower armed-1",
            "Static Windsock-2"
        ],
        "vehicle_groups": [
            "FARP MASH 1-1",
            "FARP Support 1-4",
            "FARP Support 1-5",
            "FARP Support 1-6"
        ],
        "x": 134151.8137747,
        "y": -133818.48342646
    },
    "FARP-3": {
        "clearScenery": "all",
        "component": "farp",
        "label": "FARP Timmy",
        "radius": 137.16,
        "ship_groups": [],
        "static_groups": [
            "MASH Tent 1-4",
            "MASH Tent 1-5",
            "Static Container 20ft-7",
            "Static Container 20ft-8",
            "Static Container 20ft-9",
            "Static FARP Tent-65",
            "Static FARP Tent-66",
            "Static FARP Tent-67",
            "Static FARP Tent-68",
            "Static Invisible FARP-10",
            "Static Invisible FARP-11",
            "Static Invisible FARP-12",
            "Static Invisible FARP-9",
            "Static Watch tower armed-2",
            "Static Windsock-3"
        ],
        "vehicle_groups": [
            "FARP MASH 1-14",
            "FARP Support 1-7",
            "FARP Support 1-8",
            "FARP Support 1-9"
        ],
        "x": 225220.7942526,
        "y": 26946.717049047
    },
    "FARP-4": {
        "clearScenery": "all",
        "component": "farp",
        "label": "FARP Bewl Water",
        "radius": 137.16,
        "ship_groups": [],
        "static_groups": [
            "MASH Tent 1-6",
            "MASH Tent 1-7",
            "Static Container 20ft-10",
            "Static Container 20ft-11",
            "Static Container 20ft-12",
            "Static FARP Tent-69",
            "Static FARP Tent-70",
            "Static FARP Tent-71",
            "Static FARP Tent-72",
            "Static Invisible FARP-13",
            "Static Invisible FARP-14",
            "Static Invisible FARP-15",
            "Static Invisible FARP-16",
            "Static Watch tower armed-4",
            "Static Windsock-4"
        ],
        "vehicle_groups": [
            "FARP MASH 1-15",
            "FARP Support 1-10",
            "FARP Support 1-11",
            "FARP Support 1-12"
        ],
        "x": 177862.23657392,
        "y": 42603.952621407
    },
    "FARP-5": {
        "clearScenery": "all",
        "component": "farp",
        "label": "FARP Bluebird",
        "radius": 137.16,
        "ship_groups": [],
        "static_groups": [
            "MASH Tent 1-15",
            "MASH Tent 1-16",
            "Static Container 20ft-34",
            "Static Container 20ft-35",
            "Static Container 20ft-36",
            "Static FARP Tent-73",
            "Static FARP Tent-74",
            "Static FARP Tent-75",
            "Static FARP Tent-76",
            "Static Invisible FARP-24",
            "Static Invisible FARP-25",
            "Static Invisible FARP-26",
            "Static Invisible FARP-27",
            "Static Watch tower armed-5",
            "Static Windsock-5"
        ],
        "vehicle_groups": [
            "FARP MASH 1-23",
            "FARP Support 1-20",
            "FARP Support 1-21",
            "FARP Support 1-22"
        ],
        "x": 182831.0465453,
        "y": 98494.640257035
    },
    "FARP-6": {
        "clearScenery": "all",
        "component": "farp",
        "label": "FARP Guines",
        "radius": 137.16,
        "ship_groups": [],
        "static_groups": [
            "MASH Tent 1-17",
            "MASH Tent 1-18",
            "Static Container 20ft-37",
            "Static Container 20ft-38",
            "Static Container 20ft-39",
            "Static FARP Tent-77",
            "Static FARP Tent-78",
            "Static FARP Tent-79",
            "Static FARP Tent-80",
            "Static Invisible FARP-28",
            "Static Invisible FARP-29",
            "Static Invisible FARP-30",
            "Static Invisible FARP-31",
            "Static Watch tower armed-6",
            "Static Windsock-6"
        ],
        "vehicle_groups": [],
        "x": 160205.5599261,
        "y": 146403.2206729
    }
}

for farpname, farp in farps.items():
    new_point = { "x": farp["x"], "y": farp["y"] }
    new_positions = offset_positions(original_point, positions, new_point)
    print(farpname)
    print(json.dumps(new_positions, separators=(',', ':')))