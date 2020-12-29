import json

import requests

DEV_URL = "http://localhost:8080/local/bootstrap/load/team"


def main():
    with open("ftc/ftc_config.json") as f:
        config = json.load(f)

    with requests.get(config["team_data_url"]) as req:
        data = req.json()

    for idx, (team_number, team_data) in enumerate(data.items(), 1):
        team_data["team_number"] = team_number

        r = requests.post(DEV_URL, data={"team_data": json.dumps(team_data)})
        r.raise_for_status()
        print(f"Posted team {team_number} ({idx} / {len(data)})")


if __name__ == "__main__":
    main()
