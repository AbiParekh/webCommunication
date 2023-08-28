# API class
import requests
from teamDetails import TeamStatistics


class API:
    def __init__(self):
        self.base_url = "https://sports.snoozle.net/search/nfl/searchHandler?"
        self.file_type = "inline"
        self.stat_type = "teamStats"
        self.season = 2020
        self.t_name = 26
        self.http_client = requests.Session()

    def get_team_statistics(self):
        url = f"{self.base_url}fileType={self.file_type}&statType={self.stat_type}&season={self.season}" \
              f"&teamName={self.t_name}"
        response = self.http_client.get(url)

        print("Request URL:", url)
        print("Response Status Code:", response.status_code)
        print("Response Text:", response.content)  # Print the response content

        response_json = response.json()

        print("Response JSON:", response_json)

        team_stats_list = []

        if 'matchUpStats' in response_json:
            match_up_stats = response_json['matchUpStats']

            for match_stats in match_up_stats:
                vis_stats = match_stats.get('visStats', {})
                home_stats = match_stats.get('homeStats', {})

                if 'teamName' in vis_stats:
                    team_stats_list.append(
                        TeamStatistics(
                            vis_stats['teamName'],
                            vis_stats.get('teamCode', ''),
                            vis_stats.get('teamCode', ''),  # Assuming this is correct
                            vis_stats.get('score', 0)
                        )
                    )

                if 'teamName' in home_stats:
                    team_stats_list.append(
                        TeamStatistics(
                            home_stats['teamName'],
                            home_stats.get('teamCode', ''),
                            home_stats.get('teamCode', ''),  # Assuming this is correct
                            home_stats.get('score', 0)
                        )
                    )

        return team_stats_list
