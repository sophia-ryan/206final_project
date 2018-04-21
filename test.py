import unittest
from app import *

DBNAME = 'restaurant.db'

class TestDatabase(unittest.TestCase):

    def test_episode_table(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql = 'SELECT EpisodeName FROM Episode'
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertIn(('Burgers and Dogs',), result_list)
        self.assertIn(('A Festival of Flavor',), result_list)
        self.assertIn(('Signature Sandwiches',), result_list)
        self.assertIn(('A Taste of Everywhere',), result_list)
        self.assertIn(('Breakfast',), result_list)
        self.assertIn(('Seriously Saucy',), result_list)
        self.assertEqual(len(result_list), 202)

        sql = 'SELECT SeasonNumber FROM Episode WHERE EpisodeName = "Aces of Authenticity"'
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertEqual(len(result_list), 1)

        conn.close()

    def test_restaurant_table(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql = 'SELECT Name FROM Restaurants'
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertIn(('POK POK',), result_list)
        self.assertIn(('ATAULA',), result_list)
        self.assertIn(('CAFE BRAZIL',), result_list)
        self.assertIn(('BANG!',), result_list)
        self.assertIn(('TIP TOP CAFE',), result_list)
        self.assertIn(('ATAULA',), result_list)

        sql = 'SELECT * FROM Restaurants WHERE Name = "STANDARD TAP"'
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertEqual(len(result_list), 1)

        conn.close()

unittest.main()

# class SQLTestCase()
