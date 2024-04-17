from My_calc import calc
from My_calc import calc_dif
import unittest


class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc(1, 1,'+'), 2)
    def test_min(self):
        self.assertEqual(calc(77, 7,'-'), 70)
    def test_del(self):
        self.assertEqual(calc(9, 3,'/'), 3)
    def test_mul(self):
        self.assertEqual(calc(40, 10,'*'), 400)
    def test_power(self):
        self.assertEqual(calc(2, 2,"**"), 4)
    def test_square(self):
        self.assertEqual(calc_dif(4,"^(1/2)"), 2)
    def test_fact(self):
        self.assertEqual(calc_dif(3,"!"), 6)
    def test_add_2(self):
        self.assertNotEqual(calc(1, 1,'+'), 11)
    def test_min_2(self):
        self.assertNotEqual(calc(1, 1,'-'), ' ')
    def test_mul_2(self):
        self.assertNotEqual(calc(1, 0,'*'), 1)
    def test_div_zero(self):
        self.assertNotEqual(calc(1, 0,'/'), 0)
    def test_power_2(self):
        self.assertNotEqual(calc(1, 1,'**'), 0)
    def test_square_negative(self):
        self.assertNotEqual(calc_dif(-4,"^(1/2)"), 0)
    def test_fact_zero(self):
        self.assertNotEqual(calc_dif(0,"!"), 0)



if __name__ == '__main__':
    unittest.main()
