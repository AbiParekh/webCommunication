# main.py
# Author: Abhishek Parekh
from api import API


def main():
    api_call = API()

    team_stats_list = api_call.get_team_statistics()

    # Print team statistics fetched from the API
    for team_stats in team_stats_list:
        print(team_stats)
        print(team_stats.keys())
        print(team(team_stats_list))
        print(f"Team Name: {team_stats.team_name}, Team Code: {team_stats.team_code}, Score: {team_stats.score}")


if __name__ == '__main__':
    main()
