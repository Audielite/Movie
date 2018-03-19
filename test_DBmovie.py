import unittest
from DBmovie import shows
from DBmovie import pick

class ShowsTestCase(unittest.TestCase):
    def test_shows_playing(self):
        self.assertIsInstance(response["results"][1]["title"])

class PickTestCase(unittest.TestCase):
    def test_shows_playing(self):
        self.assertTrue('yes')



if __name__ == '__main__':
    unittest.main()
