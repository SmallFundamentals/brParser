import unittest
import core

class TestCoreFunctions(unittest.TestCase):
	def test_get_last_initial(self):
		self.assertEqual(core.get_last_initial("Tim Duncan"), "D")

if __name__ == '__main__':
    unittest.main()