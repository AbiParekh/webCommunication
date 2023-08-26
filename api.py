# API Client class
import requests
from teamDetails import TeamStatistics
import sqlite3


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

        print("Request URL:", url)
        print("Response Status Code:", response.status_code)
        print("Response Text:", response.text)  # Print the response content

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

    def insert_team_statistics(self, team_stats):
        connection = sqlite3.connect('team_stats.db')
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO team_statistics (team_name, team_number, team_code, score)
            VALUES (?, ?, ?, ?)
        ''', team_stats.to_tuple())
        connection.commit()
        connection.close()

    def get_team_statistics_from_database(self):
        connection = sqlite3.connect('team_stats.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM team_statistics')
        data = cursor.fetchall()
        connection.close()
        return data

    def create_database(self):
        connection = sqlite3.connect('team_stats.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS team_statistics (
            id INTEGER PRIMARY KEY,
            team_name TEXT,
            team_number INTEGER,
            team_code TEXT,
            score INTEGER
        )''')
        connection.commit()
        connection.close()

