import sqlite3
# from teamDetails import TeamStatistics


class Database:
    @staticmethod
    def get_team_statistics_from_database():
        try:
            connection = sqlite3.connect('team_stats.db')
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM team_statistics')
            data = cursor.fetchall()
            return data
        except sqlite3.Error as e:
            print("Error fetching data from the database:", e)
            return []

    @staticmethod
    def insert_team_statistics(team_stats):
        try:
            connection = sqlite3.connect('team_stats.db')
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO team_statistics (team_name, team_number, team_code, score)
                VALUES (?, ?, ?, ?)
            ''', team_stats.to_tuple())
            connection.commit()
        except sqlite3.Error as e:
            print("Error inserting data into the database:", e)

    @staticmethod
    def create_database():
        try:
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
        except sqlite3.Error as e:
            print("Error creating the database table:", e)


# Call create_database() once when you want to create the database table
Database.create_database()
