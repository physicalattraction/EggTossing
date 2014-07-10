'''
Created on 22 jun. 2014

@author: Erwin Rossen
'''

class Building(object):
    '''
    The problem definition: set up an N-story building and define
    T, the floor from which the egg will break.
    '''

    def __init__(self, N, T):
        '''
        Constructor
        '''
        # Set N
        if (N <= 0):
            self.N = 1
        else:
            self.N = N
            
        # Set T
        if (T <= 0):
            self.T = 1
        elif (T>N):
            self.T = N
        else:
            self.T = T
            
        self.nr_tosses = 0
        self.nr_broken_eggs = 0
        
    def drop_from_floor(self, floor):
        self.nr_tosses += 1
        if floor < self.T:
            return False
        else:
            self.nr_broken_eggs += 1
            return True