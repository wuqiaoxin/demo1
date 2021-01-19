import unittest
from calc import Calculator
c=Calculator()
class TestCalc(unittest.TestCase):
    def testAdd(self):
        a = 9
        b = 10
        s = 19
        sum = c.Add(a,b)
        self.assertEquals(s,sum)

    def testAdd1(self):
        a = -9
        b = 10
        s = 1
        sum = c.Add(a,b)
        self.assertEquals(s,sum)

    def testAdd2(self):
        a = 9
        b = -10
        s = -1
        sum = c.Add(a,b)
        self.assertEquals(s,sum)

    def testAdd3(self):
        a = -9
        b = -10
        s = -19
        sum = c.Add(a,b)
        self.assertEquals(s,sum)

