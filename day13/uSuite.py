import unittest
import os
from utest import TestCalc
from u1test import TestCalc1
from u2test import TestCalc2
from u3test import TestCalc3
from HTMLTestRunner import HTMLTestRunner
suite = unittest.TestSuite()
tests = unittest.defaultTestLoader.discover(os.getcwd(),"*test.py")
suite.addTest(tests)

f = open("计算机的测试报告汇总.html","w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
     stream = f,
     verbosity = 1,
     title = "计算机的测试报告汇总"
)

runner.run(suite)



