import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_topscorers(self):
        top_scorers = self.stats.top(3)
        topname = top_scorers[0].name

        self.assertAlmostEqual(topname, "Gretzky")

    def test_players_of_team(self):
        players = self.stats.team("PIT")
        self.assertEqual(1, len(players))

    def test_search(self):
        pelaaja = self.stats.search("Gretzky")
        self.assertEqual(pelaaja.name, "Gretzky")
    
    def test_search_none(self):
        pelaaja = self.stats.search("Matti")
        self.assertEqual(pelaaja, None)