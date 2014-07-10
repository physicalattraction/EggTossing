'''
Created on 22 jun. 2014

@author: Erwin Rossen

Version 1: 1 egg, <= T tosses.

Version 2: ~1 lg N eggs and ~1 lg N tosses.

Version 3: ~ lg T eggs and ~2 lg T tosses.

Version 4: 2 eggs and ~2 sqrt(N) tosses.

Version 5: 2 eggs and <= c*sqrt(T) tosses for some fixed constant c. 
'''

from Building import Building

class Strategy(object):
    
    def __init__(self, building):
        assert(isinstance(building, Building))
        self.building = building
        
    def determine_T(self):
        pass

class Strategy_1(Strategy):
    '''    1 egg, <=T tosses.    '''

    def determine_T(self):
        egg_broken = False
        floor_to_throw_from = 0
        while ( (not egg_broken) and (floor_to_throw_from < self.building.N) ):
            floor_to_throw_from += 1
            egg_broken = self.building.drop_from_floor(floor_to_throw_from)
        return (floor_to_throw_from, 
                self.building.nr_tosses, 
                self.building.nr_broken_eggs)    
        
class Strategy_2(Strategy):
    '''    ~1 lg N eggs and ~1 lg N tosses    '''

    def determine_T(self):
        T_low = 0
        T_high = self.building.N
        
        while (T_low != T_high):
            T_mid = ((T_low)+(T_high)) / 2
            egg_breaks = self.building.drop_from_floor(T_mid)
            if egg_breaks:
                T_high = T_mid
            else:
                T_low = T_mid + 1
                    
        return (T_low, 
                self.building.nr_tosses, 
                self.building.nr_broken_eggs)
        
class Strategy_3(Strategy):
    '''    ~lg T eggs and ~2 lg T tosses    '''

    def determine_T(self):
        raise NotImplementedError()
        
class Strategy_4(Strategy):
    '''    2 eggs and ~2 sqrt(N) tosses    '''

    def determine_T(self):
        raise NotImplementedError()
        
class Strategy_5(Strategy):
    '''    2 eggs and <= c*sqrt(T) tosses for some fixed constant c    '''

    def determine_T(self):
        raise NotImplementedError()
        