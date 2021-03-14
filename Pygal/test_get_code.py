import unittest
from get_code_3 import get_country_code

class Test_Country_Code(unittest.TestCase):
	
	def setUp(self):
		self.code = get_country_code("Iceland")
		
	def test_code(self):
		self.assertIn(self.code, 'is')

unittest.main()
