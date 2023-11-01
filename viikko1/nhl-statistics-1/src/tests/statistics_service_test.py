import unittest
from statistics_service import StatisticsService
from player import Player
from sortby import SortBy

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
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_konstruktori_toimii_oikein(self):
        players = [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]
        self.assertEqual(self.stats._player_reader.get_players()[0].name, players[0].name)

    def test_search_kun_nimi_loytyy(self):
        self.assertEqual(self.stats.search("Semenko").name, "Semenko")

    def test_search_kun_nimi_ei_loydy(self):
        self.assertIsNone(self.stats.search("testname"))

    def test_team_toimii_oikein(self):
        self.assertEqual(len(self.stats.team("EDM")), 3)

    def test_top_sort_by_points_toimii_oikein(self):
        self.assertEqual(self.stats.top(2)[0].name, "Gretzky")

    def test_top_sort_by_goals_toimii_oikein(self):
        self.assertEqual(self.stats.top(2, SortBy.GOALS)[0].name, "Lemieux")

    def test_top_sort_by_assists_toimii_oikein(self):
        self.assertEqual(self.stats.top(2, SortBy.ASSISTS)[0].name, "Gretzky")

    def test_top_vaara_arvo(self):
        with self.assertRaises(ValueError):
            self.stats.top(2, 2)
