import requests


class TeamStatistics:
    def __init__(self, team_name, team_number, team_code, score):
        self.team_name = team_name
        self.team_number = team_number
        self.team_code = team_code
        self.score = score


class APIClient:
    def __init__(self):
        self.base_url = "https://sports.snoozle.net/search/nfl/searchHandler?"
        self.file_type = "inline"
        self.stat_type = "teamStats"
        self.season = 2020
        self.http_client = requests.Session()

    def get_team_statistics(self):
        url = f"{self.base_url}fileType={self.file_type}&season={self.season}&statType={self.stat_type}"
        response = self.http_client.get(url)
        print(response.status_code)
        print(response.text)  # Print the response content
        response_json = response.json()

        team_stats_list = []

        if 'matchUpStats' in response_json:
            match_up_stats = response_json['matchUpStats']

            for match_stats in match_up_stats:
                vis_stats = match_stats['visStats']
                home_stats = match_stats['homeStats']

                team_stats_list.append(
                    TeamStatistics(
                        vis_stats['teamName'],
                        vis_stats['teamCode'],
                        vis_stats['teamCode'],  # Assuming this is correct
                        vis_stats['score']
                    )
                )

                team_stats_list.append(
                    TeamStatistics(
                        home_stats['teamName'],
                        home_stats['teamCode'],
                        home_stats['teamCode'],  # Assuming this is correct
                        home_stats['score']
                    )
                )

        return team_stats_list


def main():
    api_client = APIClient()
    team_stats_list = api_client.get_team_statistics()

    for team_stats in team_stats_list:
        print(f"Team Name: {team_stats.team_name}, Team Number: {team_stats.team_number}")
        print(f"Team Code: {team_stats.team_code}, Score: {team_stats.score}")
        print("------------------------------------")


if __name__ == '__main__':
    main()
