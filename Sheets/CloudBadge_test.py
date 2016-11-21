import unittest
from CloudBadge import *

class CloudBadgeTest(unittest.TestCase):


	def test_date_sort(self):
		"""Check the correct format for the current date """
	
		self.assertEqual(get_tab_date() ,"11/20")
	
	def test_straight_check(self):
		straight_list = ['B2','B1','B4','B3']
		self.assertEqual(check_straight(straight_list),True)
		
		
if __name__ == '__main__':
	unittest.main()
	
