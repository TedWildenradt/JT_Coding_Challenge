import unittest
from main import Soccer

class TestSoccer(unittest.TestCase):

    def setUp(self):
      self.soccer = Soccer()
      # self.file_object = open('sample_input.txt','r')


    def testParseTeamAndScore(self):
        """
        Test that it parses line into team and score
        """
        data = "San Jose Earthquakes 3"
        result = self.soccer.parseTeamAndScore(data)
        self.assertEqual(result, ["San Jose Earthquakes", "3"])

    def testParseTeamAndScore2(self):
        """
        Test that it parses line into team and score
        """
        data = " Santa Cruz Slugs 3"
        result = self.soccer.parseTeamAndScore(data)
        self.assertEqual(result, ["Santa Cruz Slugs", "3"])

    def testDeterminePoints(self):
        """
        Test that it determines points correctly
        """
        team1 = ["San Jose Earthquakes", "3"]
        team2 = ["Santa Cruz Slugs", "3"]
        self.soccer.determinePoints(team1,team2)
        self.assertEqual(self.soccer.teams["Santa Cruz Slugs"], 1)
        self.assertEqual(self.soccer.teams["San Jose Earthquakes"], 1)

    def testDeterminePoints(self):
        """
        Test that it determines points correctly
        """
        team1 = ["Capitola Seahorses", "1"]
        team2 = ["Aptos FC", "0"]
        self.soccer.determinePoints(team1,team2)
        self.assertEqual(self.soccer.teams["Capitola Seahorses"], 3)
        self.assertEqual(self.soccer.teams["Aptos FC"], 0)


if __name__ == '__main__':
    unittest.main()