'''
Created on 22 jun. 2014

@author: Erwin Rossen
'''
import unittest
from Building import Building

class Test(unittest.TestCase):


    def testInit(self):
        N = 60
        T = 52
        building = Building(N=N, T=T)
        self.assertEqual(building.N, 60)
        self.assertEqual(building.T, 52)
        
        N = -1
        T = 0
        building = Building(N=N, T=T)
        self.assertEqual(building.N, 1)
        self.assertEqual(building.T, 1)
        
        N = 0
        T = 0
        building = Building(N=N, T=T)
        self.assertEqual(building.N, 1)
        self.assertEqual(building.T, 1)
        
        N = 10
        T = -1
        building = Building(N=N, T=T)
        self.assertEqual(building.T, 1)
        
        N = 10
        T = 0
        building = Building(N=N, T=T)
        self.assertEqual(building.T, 1)
        
        N = 10
        T = 10
        building = Building(N=N, T=T)
        self.assertEqual(building.T, 10)
        
        N = 10
        T = 11
        building = Building(N=N, T=T)
        self.assertEqual(building.T, 10)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()