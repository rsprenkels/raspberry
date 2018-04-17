import unittest
from ronsmodule import *

class Test(unittest.TestCase):

    def setUp(self):
        self.sj = SplitJoiner()

    def test_1(self):
        self.assertEqual(self.sj.work('bart robin'), 'bart-robin', 'wrong') 

    def testSimple(self):
        self.assertEqual(self.sj.work('bart'), 'bart', 'excpected bart') 

    def test1(self):
        self.assertEqual(self.sj.work(''), '', 'expected empty result') 

if __name__ == "__main__":
    unittest.main()
