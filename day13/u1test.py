import unittest
from calc import Calculator
c= Calculator()
class TestCalc1(unittest.TestCase):
    def testIncre(self):
        a = 19
        b = 10
        s = 9
        sum = c.Incre(a,b)
        self.assertEquals(s,sum)

    def testIncre1(self):
        a = -19
        b = 10
        s = -29
        sum = c.Incre(a,b)
        self.assertEquals(s,sum)

    def testIncre2(self):
        a = 19
        b = -10
        s = 29
        sum = c.Incre(a,b)
        self.assertEquals(s,sum)

    def testIncre3(self):
        a = -19
        b = -10
        s = -9
        sum = c.Incre(a,b)
        self.assertEquals(s,sum)
