'''
Created on Apr 12, 2018

@author: rsprenkels
'''
import unittest


class Test(unittest.TestCase):
    

    def setUp(self):
        self.sj = SplitJoiner()

    def tearDown(self):
        pass

    def testName(self):
        self.assertEqual(
            self.sj.work('work on this'), 'work-on-this', 'wrong') 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()