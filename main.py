# main.py
# Author: Abhishek Parekh
import json

from api import API


def main():
    api_call = API()  # create an instance of the API class
    team_stats_list = api_call.get_team_statistics()  # api call to get the stats

    # Print team statistics from the api call
    for team_stats in team_stats_list:
        print(f"Team Name: {team_stats.team_name}")
        print(f"Team Code: {team_stats.team_code}")
        print(f"Score: {team_stats.score}")
        print()

    # load the JSON files foe each team
    for team_number in range(1, 33):
        with open(f"team_stats_{team_number}.json", "r") as json_file:
            team_data = json.load(json_file)

        print(f"Team Number: {team_number}")

        if 'matchUpStats' in team_data:
            for match_stats in team_data['matchUpStats']:
                vis_stats = match_stats.get('visStats', {})
                home_stats = match_stats.get('homeStats', {})

                if 'teamName' in vis_stats:
                    print(f"Team Name (Visitor): {vis_stats['teamName']}")
                    print(f"Team Code (Visitor): {vis_stats['teamCode']}")
                    print(f"Score (Visitor): {vis_stats['score']}")
                    print()

                if 'teamName' in home_stats:
                    print(f"Team Name (Home): {home_stats['teamName']}")
                    print(f"Team Code (Home): {home_stats['teamCode']}")
                    print(f"Score (Home): {home_stats['score']}")
                    print()
        else:
            print("No data found for this team")
            print()


if __name__ == '__main__':
    main()
