import unittest
from truthTables import *


class testLogic(unittest.TestCase):
    def testInput(self):
        self.assertEqual(initInput("a and b"), ANDTABLE)

    def testInputInteger(self):
        self.assertEqual(initInput(1), getInput(INITERROR))

    def testInputInteger(self):
        self.assertEqual(initInput("a^b"), getInput(INITERROR))

    def testInputInteger(self):
        self.assertEqual(initInput("Hello world"), getInput(INITERROR))

    def testInputInteger(self):
        self.assertEqual(initInput(True), getInput(INITERROR))

    def testInputInteger(self):
        self.assertEqual(initInput("a adn b"), getInput(INITERROR))

    def testInputInteger(self):
        self.assertEqual(initInput(INITERROR), getInput(INITERROR))

    def testAndTF(self):
        self.assertEqual(logicAnd(True, False), ':p  :q  :p and q\n:T  :F  :F\n')

    def testAndTT(self):
        self.assertEqual(logicAnd(True, True), ':p  :q  :p and q\n:T  :T  :T\n')

    def testAndFT(self):
        self.assertEqual(logicAnd(False, True), ':p  :q  :p and q\n:F  :T  :F\n')

    def testAndFF(self):
        self.assertEqual(logicAnd(False, False), ':p  :q  :p and q\n:F  :F  :F\n')

    def testAndString(self):
        self.assertEqual(logicAnd("Hi", "World"), getInput(ERROR))

    def testAndInteger(self):
        self.assertEqual(logicAnd(1,2), getInput(ERROR))

    def testrepresentAndTF(self):
        self.assertEqual(representAnd(True, False), False)

    def testrepresentAndTT(self):
        self.assertEqual(representAnd(True, True), True)

    def testrepresentAndFF(self):
        self.assertEqual(representAnd(False, False), False)

    def testrepresentAndFT(self):
        self.assertEqual(representAnd(False, True), False)

    def testrepresentString(self):
        self.assertEqual(representAnd("False", "True"), getInput(ERROR))

    def testrepresentAndInteger(self):
        self.assertEqual(representAnd(1,0), getInput(ERROR))

    def testrepresentOrTT(self):
        self.assertEqual(representOr(True, True), True)

    def testrepresentOrString(self):
        self.assertEqual(representOr("True", "False"), getInput(ERROR))

    def testrepresentOrInteger(self):
        self.assertEqual(representOr(1, 0), getInput(ERROR))

    def testrepresentFF(self):
        self.assertEqual(representOr(False, False), False)

    def testrepresentFT(self):
        self.assertEqual(representOr(False, True), True)

    def testrepresentOrTF(self):
        self.assertEqual(representOr(True, False), True)

    def testrepresentConditional(self):
        self.assertEqual(representConditional("if p, then q"), CONDTABLE)

    def testrepresentConditionalMalformed(self):
        self.assertEqual(representConditional("f p, then q"), getInput(CONDERROR))

    def testrepresentConditionalCommaMiss(self):
        self.assertEqual(representConditional("if p then q"), getInput(COMMAERROR))

    def testRepresentConditionalInteger(self):
        self.assertEqual(representConditional(1), getInput(CONDERROR))

    def testRepresentConditionalBoolean(self):
        self.assertEqual(representConditional(True), getInput(CONDERROR))

    def testRepresentConditionalContradiction(self):
        self.assertEqual(representConditional("if p, then ~p"), getInput(CONTRACOND))

    def testRepresentConditionalTautology(self):
        self.assertEqual(representConditional("if p, then p"), getInput(CONTRATAUT))

    def testRepresentConditionalMultiple(self):
        self.assertEqual(representConditional("if p, then (if q, then r)"), MULTICONTRATABLE)

    def testRepresentConditionalMultiMalformedPara(self):
        self.assertEqual(representConditional("if p, then if q then r"), getInput(PARAERROR))

    def testRepresentConditionalMultiMalformedPlacePara(self):
        self.assertEqual(representConditional("if p, (then if q, then r)"), getInput(PARAERROR))

    def testRepresentConditionalMultMalformedComma(self):
        self.assertEqual(representConditional("if p, then (if q then r)"), getInput(COMMAERROR))

    def testBreakConditionIntoLor(self):
        self.assertEqual(evaluateConditional("if p, then q"), "~p or q")

    def testBreakConditionIntoLorMulti(self):
        self.assertEqual(evaluateConditional("if p, then (if q, then r)"), "~p or (~q or r)")

    def testBreakConditionalIntLorMalformed(self):
        self.assertEqual(evaluateConditional("if p then q"), getInput(COMMAERROR))

    def testParentheses(self):
        self.assertEqual(evaluateParentheses("(if p, then q)"), True)

    def testParenthesesMalformed(self):
        self.assertEqual(evaluateParentheses("if p, then q)"), getInput(PARAERROR))

    def testParenthesesMalformedAll(self):
        self.assertEqual(evaluateParentheses("if p, then q"), getInput(PARAERROR))

    def testParenthesesBadConditional(self):
        self.assertEqual(evaluateParentheses("(if p then q)"), getInput(COMMAERROR))

    def testParenthesesMulti(self):
        self.assertEqual(evaluateParentheses("(if p, then (if q, then r))"), True)

    def testParenthesesMultiMalformed(self):
        self.assertEqual(evaluateParentheses("(if p, then if q, then r)"), getInput(PARAERROR))

    def testParenthesesMultiComma(self):
        self.assertEqual(evaluateParentheses("(if p, then (if q then r))"), getInput(COMMAERROR))

    def testParenthesesTooMany(self):
        self.assertEqual(evaluateParentheses("((if p, then (if q, then r)))"), evaluateParentheses("(if p, then (if q, then r))"))

    def testParenthesesInvalidConditional(self):
        self.assertEqual(evaluateParentheses("(if p, then if q, (then r))"), getInput(PARAERROR))

    def testParenthesesInvalidHypothesis(self):
        self.assertEqual(evaluateParentheses("((if p), then (if q, then r))"), getInput(PARAERROR))

    def testParenthesesParaBeforeThen(self):
        self.assertEqual(evaluateParentheses("(if p, (then, if q, then r))"), getInput(PARAERROR))

    def testParenthesesBlank(self):
        self.assertEqual(evaluateParentheses("()"), getInput(BLANKERROR))

    def testParenthesesMisspelledIf(self):
        self.assertEqual(evaluateParentheses("(ef p, then q)"), getInput(SPELLERROR))

    def testParenthesesMisspelledThen(self):
        self.assertEqual(evaluateParentheses("(if p, thenq)"), getInput(SPELLERROR))

    def testParenthesesExtraCommas(self):
        self.assertEqual(evaluateParentheses("(if p, then, q)"), getInput(COMMAERROR))

    def testParenthesesExtraCommasEverywhere(self):
        self.assertEqual(evaluateParentheses("(if p,, then q)"), getInput(COMMAERROR))

    def testParenthesesWrongCharacters(self):
        self.assertEqual(evaluateParentheses("(if p,. then q)"), getInput(SPELLERROR))

    def testParenthesesMissingSpaces(self):
        self.assertEqual(evaluateParentheses("(if p,then q)"), getInput(SPACEERROR))

    def testParenthesesExtraSpaces(self):
        self.assertEqual(evaluateParentheses("(if p,  then q)"), getInput(SPACEERROR))

    def testParenthesesUseOfKeyword(self):
        self.assertEqual(evaluateParentheses("(if p, then then)"), getInput(KEYERROR))

    def testParenthesesKeywordOnly(self):
        self.assertEqual(evaluateParentheses("(if p, then )"), getInput(KEYERROR))
