import unittest
from cal import cal




class MyTestCase(unittest.TestCase):

    def test_something(self):
        Cal = cal()
        self.assertEqual(True, False)

    def test_results_property_cal(selfself):
        cal = cal()
        self.assertEqual(cal.result, 4)

if __name__ == '__main__':
    unittest.main()
