import unittest

from WinStates import * 
from CloudUser import *

class WinStatesTest(unittest.TestCase):
	
        def test_gold(self):
            ''' test if user has all priorities of gold cases '''
            user = CloudUser('test')
            case_type='gold'
            cases = ['B1','B2','B3','B4'] 
            print(user.get_user_cases())
            user.set_user_cases(cases)
            self.assertEqual(check_straight(case_type,user.get_user_cases()),True) 

        def test_silver(self):
            ''' test if user has all priorities of silver cases '''
            user = CloudUser('test2')
            case_type='silver'
            cases = ['Y1','Y2','Y3','Y4'] 
            user.set_user_cases(cases)
            self.assertEqual(check_straight(case_type,user.get_user_cases()),True) 

        def test_platinum(self):
            ''' test if user has all priorities of platinum cases '''
            user = CloudUser('test')
            case_type='platinum'
            cases = ['G1','G2','G3','G4'] 
            user.set_user_cases(cases)
            self.assertEqual(check_straight(case_type,user.get_user_cases()),True) 
            

        def test_eight_cases(self):
            ''' test if user has 8 cases '''
            user = CloudUser('test',8)
	    self.assertTrue(check_num(user.get_case_count(),8))

        def test_ten_cases(self):
            user = CloudUser('test',10)
	    self.assertTrue(check_num(user.get_case_count(),10))

if __name__ == '__main__':
	unittest.main()
	
