import unittest
from calc import Calculator
c= Calculator()
class TestCalc3(unittest.TestCase):
    def testDivid(self):
        a = 9
        b = 3
        s = 3
        sum = c.Divid(a,b)
        self.assertAlmostEquals(s,sum)

    def testDivid1(self):
        a = 9
        b = -3
        s = -3
        sum = c.Divid(a,b)
        self.assertAlmostEquals(s,sum)

    def testDivid2(self):
        a = -9
        b = 3
        s = -3
        sum = c.Divid(a,b)
        self.assertAlmostEquals(s,sum)

    def testDivid3(self):
        a = -9
        b = -3
        s = 3
        sum = c.Divid(a,b)
        self.assertAlmostEquals(s,sum)



