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

    def testAndString(self):
        self.assertEqual(logicAnd("Hi", "World"), ERROR)

    def testAndInteger(self):
        self.assertEqual(logicAnd(1,2), ERROR)

    def testEvaluateAndTF(self):
        self.assertEqual(evaluateAnd(True, False), False)

    def testEvaluateAndTT(self):
        self.assertEqual(evaluateAnd(True, True), True)

    def testEvaluateAndFF(self):
        self.assertEqual(evaluateAnd(False, False), False)

    def testEvaluateAndFT(self):
        self.assertEqual(evaluateAnd(False, True), False)

    def testEvaluateString(self):
        self.assertEqual(evaluateAnd("False", "True"), ERROR)

    def testEvaluateAndInteger(self):
        self.assertEqual(evaluateAnd(1,0), ERROR)

    def testEvaluateOrTT(self):
        self.assertEqual(evaluateOr(True, True), ':p  :q  :p or q\n:T  :T  :T\n')

    def testEvaluateOrString(self):
        self.assertEqual(evaluateOr("True", "False"), ERROR)

    def testEvaluateOrInteger(self):
        self.assertEqual(evaluateOr(1, 0), ERROR)

    def testEvaluateFF(self):
        self.assertEqual(evaluateOr(False, False), False)

    def testEvaluateFT(self):
        self.assertEqual(evaluateOr(False, True), True)

    def testEvaluateOrTF(self):
        self.assertEqual(evaluateOr(True, False), True)
