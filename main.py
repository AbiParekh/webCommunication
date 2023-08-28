from api import APIClient, create_database, get_team_statistics_from_database, insert_team_statistics


def main():
    api_client = APIClient()
    create_database()

    team_stats_list = api_client.get_team_statistics()

    # Insert fetched team statistics into the database
    for team_stats in team_stats_list:
        insert_team_statistics(team_stats)

    # Fetch team statistics from the database and print them
    database_data = get_team_statistics_from_database()
    for row in database_data:
        print(row)


'''    for team_stats in team_stats_list:
        print(f"Team Name: {team_stats.team_name}, Team Number: {team_stats.team_number}")
        print(f"Team Code: {team_stats.team_code}, Score: {team_stats.score}")
        print("------------------------------------")

        api_client.insert_team_statistics(team_stats)

    # Retrieve data from the database
    saved_data = api_client.get_team_statistics_from_database()
    print("\nData retrieved from the database:")
    for row in saved_data:
        print(row)'''

if __name__ == '__main__':
    main()
