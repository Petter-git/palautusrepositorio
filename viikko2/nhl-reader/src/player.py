class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict ['team']
        self.goals = dict ['goals']
        self.assists = dict ['assists']
        self.nationality = dict ['nationality']
        self.total = self.goals + self.assists
    

    def __str__(self):
        return f"{self.name:20} {self.team:7} {self.goals:3} + {self.assists:3} = {self.total}"

# Tee Player-luokkaan attribuutit kaikille JSON-datassa oleville kentille, joita ohjelmasi tarvitsee. 
# Ohjelmasi voi toimia esimerkiksi niin, että se tulostaisi pelaajat seuraavalla tavalla: poetry run python3 src/index.py