# Calvinball

## Quickstart

### Setup
1. Install a modern python 3 (I'm using 3.10)
2. Clone the repository
3. Make a virtual environment `python -m venv venv`
4. Activate the virtual environment `./venv/Scripts/Activate`
5. Install the dependencies `pip install -r ./requirements.txt`
6. Ensure `<DCS Install Folder>\Scripts\MissionScripting.lua` is desanitized before running

### Edit the missions
1. Run `python ./generate.py`
2. Open the generated mission in the ME (will be in folder named after the mission in `Saved Games\DCS.openbeta\Missions` )
3. Make edits and save mission
4. Dump mission contents to temp json using `python ./dump.py --mission CyprusInvasion`
5. Copy contents from `temp/*.json` to the appropriate mission json files, json format them, and review changes.
   
### Run the missions
1. For local testing, generate with `python ./generate.py --no-edit --no-package --debug`
2. For server, generate with `python ./generate.py --no-edit --package --debug`
3. The mission state is stored in csv files in the mission folder in `Saved Games\DCS.openbeta\Missions`
