import unittest
from cal import cal




class MyTestCase(unittest.TestCase):

    def test_something(self):
        Cal = cal()
        self.assertEqual(True, False)

    def test_results_property_cal(self):
        Cal = cal()
        self.assertEqual(cal.result, 0)

    def test_add_method_cal(self):
        Cal = cal()
        self.assertEqual(cal.add(2 , 2) , 4)
        self.assertEqual(cal.result , 4)

    def test_sub_method_cal(self):
        Cal = cal()
        self.assertEqual(cal.sub(2 , 2) , 4)
        self.assertEqual(cal.result , 4)


if __name__ == '__main__':
    unittest.main()
