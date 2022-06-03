import unittest

from something import add

class TestSum(unittest.TestCase):
    def test_add(self):

        a = 10 
        b = 20 
        self.assertEqual(add(a,b),30)
if __name__ == "__main__":
    unittest.main()
