import unittest

import sum

class TestSum(unittest.TestCase):
	def test_sum(self):
		self.assertEqual(3, sum.sum(1, 2)) 
