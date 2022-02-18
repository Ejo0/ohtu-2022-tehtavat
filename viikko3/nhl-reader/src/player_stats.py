class PlayerStats:

    def __init__(self, reader) -> None:
        self.reader = reader
    
    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()

        return sorted(filter(lambda p: p.nationality == nationality, players),
                      key=lambda p: p.points, reverse=True)
