class Player:

    def __init__(self, player_dict: dict):
        self.name = player_dict.get("name", None)
        self.nationality = player_dict.get("nationality", None)
        self.assists = player_dict.get("assists", None)
        self.goals = player_dict.get("goals", None)
        self.penalties = player_dict.get("penalties", None)
        self.team = player_dict.get("team", None)
        self.games = player_dict.get("games", None)
        try:
            self.points = self.goals + self.assists
        except:
            self.points = 0

    def __str__(self):
        return f"{self.name:20}{self.team} {self.goals:2} + {self.assists:2} = {self.points:3}"
