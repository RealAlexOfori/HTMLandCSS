import unittest
from src.functions import *

class TestFunctions(unittest.TestCase):

    # @unittest.skip("comment out this line to run the test")
    def test_greet_catalan(self):
        result = greet_catalan("Mar")
        self.assertEqual("Hola, Mar", result)


    # @unittest.skip("comment out this line to run the test")
    def test_greet_mandarin(self):
        result = greet_mandarin("Sky")
        self.assertEqual("Ni hao, Sky", result)


    # @unittest.skip("comment out this line to run the test")
    def test_count_eggs(self):
        chickens = [
            { "name": "Margaret", "age": 2, "eggs": 0 },
            { "name": "Hetty", "age": 1, "eggs": 2 },
            { "name": "Henrietta", "age": 3, "eggs": 1 },
            { "name": "Audrey", "age": 2, "eggs": 0 },
            { "name": "Mabel", "age": 5, "eggs": 1 },
        ]
        result = count_eggs(chickens)
        self.assertEqual(4, result)


    # @unittest.skip("comment out this line to run the test")
    def test_find_chicken_by_name(self):
        mars_chickens = [
            { "name": "The Knowledge", "age": 5, "eggs": 3 },
            { "name": "Spaghetti", "age": 4, "eggs": 0 },
            { "name": "Bob", "age": 2, "eggs": 2 },
            { "name": "Egg", "age": 2, "eggs": 1 },
            { "name": "Keith", "age": 1, "eggs": 0 },
        ]
        found_chicken = find_chicken_by_name(mars_chickens, "Spaghetti")
        self.assertEqual({ "name": "Spaghetti", "age": 4, "eggs": 0 }, found_chicken)

    
    # @unittest.skip("comment out this line to run the test")
    def test_find_chicken_by_name__not_found(self):
        skys_chickens = [
            { "name": "Pea", "age": 2, "eggs": 1 },
            { "name": "Perry", "age": 1, "eggs": 5 },
            { "name": "JiJi", "age": 3, "eggs": 1 },
            { "name": "Pie", "age": 2, "eggs": 2 },
            { "name": "Mario", "age": 5, "eggs": 8 },
        ]

        found_chicken = find_chicken_by_name(skys_chickens, "Nugget")
        self.assertEqual(None, found_chicken)