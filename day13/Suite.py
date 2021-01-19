import unittest
from utest import TestCalc
from HTMLTestRunner import HTMLTestRunner
suite = unittest.TestSuite()
suite.addTest(TestCalc("testAdd"))
suite.addTest(TestCalc("testIncre"))
suite.addTest(TestCalc("testMulti"))
suite.addTest(TestCalc("testDivid"))

f = open("计算机的测试报告.html","w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream = f,
    verbosity = 1,
    title = "计算机测试报告"
)
runner.run(suite)