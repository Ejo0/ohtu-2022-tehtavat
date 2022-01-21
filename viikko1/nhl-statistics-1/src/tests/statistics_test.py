import unittest
from statistics import Statistics
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


class TestStatistics(unittest.TestCase):
    def setUp(self) -> None:
        self.stats = Statistics(PlayerReaderStub())
    
    def test_search_returns_correct_player(self):
        player = self.stats.search("Yzer")
        self.assertEqual(player.name, "Yzerman")
    
    def test_search_with_wrong_name_returns_none(self):
        player = self.stats.search("Makar")
        self.assertIsNone(player)
    
    def test_team_returns_all_players_from_team(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].team, "EDM")
    
    def test_top_scorers_order_is_correct(self):
        top_scorers = self.stats.top_scorers(3)
        self.assertEqual(top_scorers[2].name, "Yzerman")
