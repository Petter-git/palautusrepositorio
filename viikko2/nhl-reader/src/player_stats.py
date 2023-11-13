from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, playerreader: PlayerReader):
        self.playerreader = playerreader
            
    def top_scorers_by_nationality (self, country: str):
        players_from_country =  []
        for player in self.playerreader.get_players():
            if player.nationality == country:
                players_from_country.append(player)
        return players_from_country


    def top_scorers (self):
        return self.playerreader.get_players()