import unittest
from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase): 
    def test1(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertIsNotNone(englishToFrench(""))

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertIsNotNone(frenchToEnglish(""))

unittest.main()       