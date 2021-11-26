import unittest

from scores import calculate_scores


class TestScoring(unittest.TestCase):

    def test_calculate_scores(self):
        team_scores = ['Lions 3, Snakes 3',
                       'Tarantulas 1, FC Awesome 0',
                       'Kaizer Chiefs 3, Lions 1',
                       'Lions 1, Tarantulas 1']
        scores = calculate_scores(team_scores)
        self.assertEqual(scores['FC Awesome'], 0)
        self.assertEqual(scores['Kaizer Chiefs'], 3)
        self.assertEqual(scores['Lions'], 2)


if __name__ == '__main__':
    unittest.main()
