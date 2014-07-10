'''
Created on 22 jun. 2014

@author: Erwin Rossen
'''
import unittest
import math
from Building import Building
from Strategy import *

class Test(unittest.TestCase):
    
    def setUp(self):
        M = 15
        self.buildings = []
        self.buildings.append(Building(N = 2**M-1, T = 1))
        self.buildings.append(Building(N = 2**M  , T = 1))
        self.buildings.append(Building(N = 2**M+1, T = 1))

        self.buildings.append(Building(N = 2**M-1, T = 2**M-2))
        self.buildings.append(Building(N = 2**M  , T = 2**M-1))
        self.buildings.append(Building(N = 2**M+1, T = 2**M  ))
        self.buildings.append(Building(N = 2**M+2, T = 2**M+1))
                
        self.buildings.append(Building(N = 2**M-1, T = 2**M-1))
        self.buildings.append(Building(N = 2**M  , T = 2**M  ))
        self.buildings.append(Building(N = 2**M+1, T = 2**M+1))

    def tearDown(self):
        pass
    
    def testInit(self):
        '''The Strategy can only be initialized with a proper Building'''
        with self.assertRaises(AssertionError):
            Strategy_1(1.0)
        with self.assertRaises(AssertionError):
            Strategy_2(1.0)
  
    def testStrategy_1(self):
        '''
        The strategy should return the proper T,
        with 1 egg, <=T tosses
        '''
        for building in self.buildings:
            toss_strategy = Strategy_1(building)
            (determined_T, nr_tosses, nr_broken_eggs) = toss_strategy.determine_T()
            
            expected_T = building.T
            expected_tosses = building.T
            expected_eggs = 1
            
            print('N = {0}, T = {1}'.format(building.N, building.T))
            
            self.assertEqual(determined_T, expected_T)
            self.assertLessEqual(nr_tosses, expected_tosses,
                                 'N = {0}, T = {1}'.format(building.N, building.T))
            self.assertLessEqual(nr_broken_eggs, expected_eggs,
                                 'N = {0}, T = {1}'.format(building.N, building.T))
        
    def testStrategy_2(self):
        '''
        The strategy should return the proper T,
        with ~1 lg N eggs and ~1 lg N tosses
        '''
        
        for building in self.buildings:
            toss_strategy = Strategy_2(building)
            (determined_T, nr_tosses, nr_broken_eggs) = toss_strategy.determine_T()
            
            expected_T = building.T
            expected_tosses = math.ceil(math.log(building.N)/math.log(2)) + 1
            expected_eggs = math.ceil(math.log(building.N)/math.log(2))
            
            self.assertEqual(determined_T, expected_T)
            self.assertLessEqual(nr_tosses, expected_tosses,
                                 'N = {0}, T = {1}, nr_tosses = {2}, max_nr_tosses = {3}'
                                 .format(building.N, building.T, nr_tosses, expected_tosses))
            self.assertLessEqual(nr_broken_eggs, expected_eggs,
                                 'N = {0}, T = {1}, nr_eggs = {2}, max_nr_eggs = {3}'.
                                 format(building.N, building.T, nr_broken_eggs, expected_eggs))
        pass
    
    def testStrategy_3(self):
        '''
        The strategy should return the proper T,
        with ~ lg T eggs and ~2 lg T tosses
        '''
        
        for building in self.buildings:
            toss_strategy = Strategy_3(building)
            (determined_T, nr_tosses, nr_broken_eggs) = toss_strategy.determine_T()
            
            expected_T = building.T
            expected_tosses = 2*math.ceil(math.log(building.T)/math.log(2))
            expected_eggs = math.ceil(math.log(building.T)/math.log(2))
            
            self.assertEqual(determined_T, expected_T)
            self.assertLessEqual(nr_tosses, expected_tosses,
                                 'N = {0}, T = {1}, nr_tosses = {2}, max_nr_tosses = {3}'
                                 .format(building.N, building.T, nr_tosses, expected_tosses))
            self.assertLessEqual(nr_broken_eggs, expected_eggs,
                                 'N = {0}, T = {1}, nr_eggs = {2}, max_nr_eggs = {3}'.
                                 format(building.N, building.T, nr_broken_eggs, expected_eggs))
        pass
    
    def testStrategy_4(self):
        '''
        The strategy should return the proper T,
        with 2 eggs and ~2 sqrt(N) tosses
        '''
        
        for building in self.buildings:
            toss_strategy = Strategy_4(building)
            (determined_T, nr_tosses, nr_broken_eggs) = toss_strategy.determine_T()
            
            expected_T = building.T
            expected_tosses = 2*math.ceil(math.sqrt(building.N))
            expected_eggs = 2
            
            self.assertEqual(determined_T, expected_T)
            self.assertLessEqual(nr_tosses, expected_tosses,
                                 'N = {0}, T = {1}, nr_tosses = {2}, max_nr_tosses = {3}'
                                 .format(building.N, building.T, nr_tosses, expected_tosses))
            self.assertLessEqual(nr_broken_eggs, expected_eggs,
                                 'N = {0}, T = {1}, nr_eggs = {2}, max_nr_eggs = {3}'.
                                 format(building.N, building.T, nr_broken_eggs, expected_eggs))
        pass
    
    def testStrategy_5(self):
        '''
        The strategy should return the proper T,
        with 2 eggs and <= c*sqrt(T) tosses for some fixed constant c
        '''
        
        for building in self.buildings:
            toss_strategy = Strategy_5(building)
            (determined_T, nr_tosses, nr_broken_eggs) = toss_strategy.determine_T()
            
            expected_T = building.T
            c = 1
            expected_tosses = c * math.sqrt(math.log(building.T)) + 1
            expected_eggs = 2
            
            self.assertEqual(determined_T, expected_T)
            self.assertLessEqual(nr_tosses, expected_tosses,
                                 'N = {0}, T = {1}, nr_tosses = {2}, max_nr_tosses = {3}'
                                 .format(building.N, building.T, nr_tosses, expected_tosses))
            self.assertLessEqual(nr_broken_eggs, expected_eggs,
                                 'N = {0}, T = {1}, nr_eggs = {2}, max_nr_eggs = {3}'.
                                 format(building.N, building.T, nr_broken_eggs, expected_eggs))
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStrategy']
    unittest.main()