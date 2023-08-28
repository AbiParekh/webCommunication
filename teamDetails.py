# team stats class
# Import into api.py

class TeamStatistics:
    def __init__(self, team_name, team_number, team_code, score):
        self.team_name = team_name
        self.team_number = team_number
        self.team_code = team_code
        self.score = score

    def add_to_tuple(self):
        return self.team_name, self.team_number, self.team_code, self.score


