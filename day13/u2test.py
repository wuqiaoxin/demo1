import unittest
from calc import Calculator
c= Calculator()
class TestCalc2(unittest.TestCase):
    def testMulti(self):
        a = 1
        b = 10
        s = 10
        sum = c.Multi(a,b)
        self.assertEquals(s,sum)

    def testMulti1(self):
        a = -1
        b = 10
        s = -10
        sum = c.Multi(a,b)
        self.assertEquals(s,sum)

    def testMulti2(self):
        a = 1
        b = -10
        s = -10
        sum = c.Multi(a,b)
        self.assertEquals(s,sum)

    def testMulti3(self):
        a = -1
        b = -10
        s = 10
        sum = c.Multi(a,b)
        self.assertEquals(s,sum)

    def testMulti4(self):
        a = -1
        b = 0
        s = 0
        sum = c.Multi(a,b)
        self.assertEquals(s,sum)

