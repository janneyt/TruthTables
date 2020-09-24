import unittest
from truthTables import *


class testLogic(unittest.TestCase):

    def testAndTF(self):
        self.assertEqual(logicAnd(True, False), ':p  :q  :p and q\n:T  :F  :F\n')

    def testAndTT(self):
        self.assertEqual(logicAnd(True, True), ':p  :q  :p and q\n:T  :T  :T\n')

    def testAndFT(self):
        self.assertEqual(logicAnd(False, True), ':p  :q  :p and q\n:F  :T  :F\n')

    def testAndFF(self):
        self.assertEqual(logicAnd(False, False), ':p  :q  :p and q\n:F  :F  :F\n')

    def testEvaluateAndTF(self):
        self.assertEqual(evaluateAnd(True, False), False)

    def testEvaluateAndTT(self):
        self.assertEqual(evaluateAnd(True, True), True)

    def testEvaluateAndFF(self):
        self.assertEqual(evaluateAnd(False, False), False)

    def testEvaluateAndFT(self):
        self.assertEqual(evaluateAnd(False, True), False)
