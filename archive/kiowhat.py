import argparse
import json
import os
import math
from pathlib import Path

def load_json(file_path):
    with open(file_path) as json_file:
        return json.load(json_file)

def add_waypoint_and_notebook_entry(counter, x, z, label, waypoints, notebook):
    waypoint = {
        "datum": 47,
        "name": f"{counter}W",
        "x": x,
        "y": 0.0,
        "z": z
    }
    waypoints.append(waypoint)
    notebook_entry = {
        "text": f"{counter}W - {label.upper()}"
    }
    notebook.append(notebook_entry)
    return counter + 1

def add_controlpoint(counter, x, z, controlpoints):
    controlpoint = {
        "datum": 47,
        "name": f"{counter}C",
        "x": x,
        "y": 0.0,
        "z": z
    }
    controlpoints.append(controlpoint)
    return counter + 1

def calculate_distance(x1, z1, x2, z2):
    return math.sqrt((x2 - x1) ** 2 + (z2 - z1) ** 2)

def process_objective(objective_key, objectives, airbases, farps, objective_current_airbase_or_farp, output_folder, strand_index, objective_index):
    objective = objectives[objective_key]
    waypoints, notebook, controlpoints = [], [], []
    waypoint_counter, controlpoint_counter = 1, 1

    current_airbase_or_farp = objective_current_airbase_or_farp.get(objective_key)
    if current_airbase_or_farp:
        if current_airbase_or_farp in airbases:
            airbase = airbases[current_airbase_or_farp]
            waypoint_counter = add_waypoint_and_notebook_entry(waypoint_counter, airbase['x'], airbase['y'], airbase['label'], waypoints, notebook)
            reference_x, reference_z = airbase['x'], airbase['y']
        elif current_airbase_or_farp in farps:
            farp = farps[current_airbase_or_farp]
            waypoint_counter = add_waypoint_and_notebook_entry(waypoint_counter, farp['x'], farp['y'], farp['label'], waypoints, notebook)
            reference_x, reference_z = farp['x'], farp['y']

    nodes = sorted(objective['nodes'].values(), key=lambda node: calculate_distance(reference_x, reference_z, node['x'], node['y']))
    for node in nodes:
        waypoint_counter = add_waypoint_and_notebook_entry(waypoint_counter, node['x'], node['y'], node['label'], waypoints, notebook)

    for vertex in objective.get('vertices', []):
        controlpoint_counter = add_controlpoint(controlpoint_counter, vertex['x'], vertex['y'], controlpoints)

    cyc_route_points = [{"index": i, "type": 0} for i in range(len(waypoints))]
    cyc_route_points.append({"index": 0, "type": 0})
    cyc_route = {"name": "CYC", "points": cyc_route_points}

    tab_route_points = [{"index": 0, "type": 0}]
    for i in range(1, len(waypoints)):
        tab_route_points.extend([{"index": i, "type": 0}, {"index": 0, "type": 0}])
    tab_route = {"name": "TAB", "points": tab_route_points}

    per_route_points = [{"index": i, "type": 2} for i in range(len(controlpoints))]
    if controlpoints:
        per_route_points.append({"index": 0, "type": 2})
    per_route = {"name": "PER", "points": per_route_points}

    battlefieldgraphics_points = [{"index": i, "type": 2} for i in range(len(controlpoints))]
    if controlpoints:
        battlefieldgraphics_points.append({"index": 0, "type": 2})
    battlefieldgraphics = [{"name": "OBJ", "points": battlefieldgraphics_points, "type": 2}]

    prepoints = [{"index": i, "type": 0} for i in range(1, len(waypoints))]

    mission_name = f"S{strand_index+1}-O{objective_index+1}"
    output_filename = f"Mission3 - {objective.get('label', 'Unknown')}.json"
    output_filepath = os.path.join(output_folder, output_filename)
    filename = Path(output_folder)
    filename.mkdir(parents=True, exist_ok=True)

    output_json = json.dumps({
        "missionName": mission_name,
        "waypoints": waypoints,
        "notebook": notebook,
        "controlpoints": controlpoints,
        "routes": [cyc_route, tab_route, per_route],
        "battlefieldgraphics": battlefieldgraphics,
        "prepoints": prepoints
    }, indent=4)
    with open(output_filepath, 'w') as output_file:
        output_file.write(output_json)

    print(f"Output written to {output_filepath}")

def main(args):
    objectives_data = load_json(args.objectives_file)
    objectives = objectives_data['objectives']
    strands = objectives_data['strands']
    airbases = load_json(args.airbases_file)
    farps = load_json(args.farps_file)

    objective_current_airbase_or_farp = {}
    for strand_index, (strand, objective_list) in enumerate(strands.items()):
        current_airbase_or_farp = None
        for objective_index, objective_key in enumerate(objective_list):
            objective = objectives[objective_key]
            airbases_unlocked = objective.get('airbases', [])
            farps_unlocked = objective.get('farps', [])

            if airbases_unlocked:
                current_airbase_or_farp = airbases_unlocked[-1]
            elif farps_unlocked:
                current_airbase_or_farp = farps_unlocked[-1]

            objective_current_airbase_or_farp[objective_key] = current_airbase_or_farp

    fixup = None
    for strand, objs in strands.items():
        if fixup is None and objective_current_airbase_or_farp[objs[0]] is not None:
            fixup = objective_current_airbase_or_farp[objs[0]]
    for strand, objs in strands.items():
        if objective_current_airbase_or_farp[objs[0]] is None:
            objective_current_airbase_or_farp[objs[0]] = fixup

    if args.objective_key:
        for strand_index, (strand, objective_list) in enumerate(strands.items()):
            if args.objective_key in objective_list:
                objective_index = objective_list.index(args.objective_key)
                process_objective(args.objective_key, objectives, airbases, farps, objective_current_airbase_or_farp, args.output_folder, strand_index, objective_index)
                break
    else:
        for strand_index, (strand, objective_list) in enumerate(strands.items()):
            for objective_index, objective_key in enumerate(objective_list):
                process_objective(objective_key, objectives, airbases, farps, objective_current_airbase_or_farp, args.output_folder, strand_index, objective_index)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate waypoints and notebook entries for objectives from objectives JSON.')
    parser.add_argument('objectives_file', type=str, help='Path to the input JSON file containing objectives.')
    parser.add_argument('airbases_file', type=str, help='Path to the input JSON file containing airbases.')
    parser.add_argument('farps_file', type=str, help='Path to the input JSON file containing FARPs.')
    parser.add_argument('output_folder', type=str, help='Path to the output folder where the JSON files will be saved.')
    parser.add_argument('--objective_key', type=str, help='The key of the objective to process. If not provided, all objectives will be processed.')
    args = parser.parse_args()
    main(args)
