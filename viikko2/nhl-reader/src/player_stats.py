class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        result = []
        for player in players:
            if player.nationality == nationality:
                result.append(player)
        
        result.sort(key=lambda x: x.goals+x.assists)
        return result