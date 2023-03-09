import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):

    def setUp(self):
        self.home_win = {"home_score": 3, "away_score": 2}
        self.away_win =  {"home_score": 0, "away_score": 2}
        self.draw = {"home_score": 1, "away_score": 1}
        self.final_scores = [self.home_win, self.away_win, self.draw]

    def test_get_home_win_when_home_score_higher(self):
        self.assertEquals("Home win", get_result(self.home_win))

    def test_get_away_win_when_away_score_higher(self):
        self.assertEquals("Away win", get_result(self.away_win))

    def test_get_draw_when_scores_the_same(self):
        self.assertEquals("Draw", get_result(self.draw))

    def test_get_results_for_list_of_scores(self):
        self.assertEquals(["Home win", "Away win", "Draw"], get_results(self.final_scores))


if __name__ == "__main__":
    unittest.main()
