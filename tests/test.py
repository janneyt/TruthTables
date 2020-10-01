import unittest
from ..TruthTables import inputValidator, representTables, logicProcBool, logicBlocks, parserParen, customErrors


class testInput(unittest.TestCase):

    def testInput(self):
        self.assertEqual(inputValidator.initInput("a and b"), customErrors.ANDTABLE)

    def testInputIntegerAlone(self):
        self.assertEqual(inputValidator.initInput(1), inputValidator.getInput(customErrors.INITERROR))

    def testInputIntegerSymbols(self):
        self.assertEqual(inputValidator.initInput("a^b"), inputValidator.getInput(customErrors.INITERROR))

    def testInputString(self):
        self.assertEqual(inputValidator.initInput("Hello world"), inputValidator.getInput(customErrors.INITERROR))

    def testInputBoolean(self):
        self.assertEqual(inputValidator.initInput(True), inputValidator.getInput(customErrors.INITERROR))

    def testInputIntegerMisspelled(self):
        self.assertEqual(inputValidator.initInput("a adn b"), inputValidator.getInput(customErrors.INITERROR))

    def testInputIntegerError(self):
        self.assertEqual(inputValidator.initInput(customErrors.INITERROR), inputValidator.getInput(customErrors.INITERROR))

class testLogic(unittest.TestCase):

    def testAndTF(self):
        self.assertEqual(logicProcBool.logicAnd(True, False), ':p  :q  :p and q\n:T  :F  :F\n')

    def testAndTT(self):
        self.assertEqual(logicProcBool.logicAnd(True, True), ':p  :q  :p and q\n:T  :T  :T\n')

    def testAndFT(self):
        self.assertEqual(logicProcBool.logicAnd(False, True), ':p  :q  :p and q\n:F  :T  :F\n')

    def testAndFF(self):
        self.assertEqual(logicProcBool.logicAnd(False, False), ':p  :q  :p and q\n:F  :F  :F\n')

    def testAndString(self):
        self.assertEqual(logicProcBool.logicAnd("Hi", "World"), inputValidator.getInput(customErrors.ERROR))

    def testAndInteger(self):
        self.assertEqual(logicProcBool.logicAnd(1,2), inputValidator.getInput(customErrors.ERROR))

class testRepresentation(unittest.TestCase):

    def testrepresentAndTF(self):
        self.assertEqual(representTables.representAnd(True, False), False)

    def testrepresentAndTT(self):
        self.assertEqual(representTables.representAnd(True, True), True)

    def testrepresentAndFF(self):
        self.assertEqual(representTables.representAnd(False, False), False)

    def testrepresentAndFT(self):
        self.assertEqual(representTables.representAnd(False, True), False)

    def testrepresentString(self):
        self.assertEqual(representTables.representAnd("False", "True"), inputValidator.getInput(customErrors.ERROR))

    def testrepresentAndInteger(self):
        self.assertEqual(representTables.representAnd(1,0), inputValidator.getInput(customErrors.ERROR))

    def testrepresentOrTT(self):
        self.assertEqual(representTables.representOr(True, True), True)

    def testrepresentOrString(self):
        self.assertEqual(representTables.representOr("True", "False"), inputValidator.getInput(customErrors.ERROR))

    def testrepresentOrInteger(self):
        self.assertEqual(representTables.representOr(1, 0), inputValidator.getInput(customErrors.ERROR))

    def testrepresentFF(self):
        self.assertEqual(representTables.representOr(False, False), False)

    def testrepresentFT(self):
        self.assertEqual(representTables.representOr(False, True), True)

    def testrepresentOrTF(self):
        self.assertEqual(representTables.representOr(True, False), True)

    def testrepresentConditional(self):
        self.assertEqual(representTables.representConditional("if p, then q"), customErrors.CONDTABLE)

    def testrepresentConditionalMalformed(self):
        self.assertEqual(representTables.representConditional("f p, then q"), inputValidator.getInput(customErrors.CONDERROR))

    def testrepresentConditionalCommaMiss(self):
        self.assertEqual(representTables.representConditional("if p then q"), inputValidator.getInput(customErrors.COMMAERROR))

    def testRepresentConditionalInteger(self):
        self.assertEqual(representTables.representConditional(1), inputValidator.getInput(customErrors.CONDERROR))

    def testRepresentConditionalBoolean(self):
        self.assertEqual(representTables.representConditional(True), inputValidator.getInput(customErrors.CONDERROR))

    def testRepresentConditionalContradiction(self):
        self.assertEqual(representTables.representConditional("if p, then ~p"), inputValidator.getInput(customErrors.CONTRACOND))

    def testRepresentConditionalTautology(self):
        self.assertEqual(representTables.representConditional("if p, then p"), inputValidator.getInput(customErrors.CONTRATAUT))

    def testRepresentConditionalMultiple(self):
        self.assertEqual(representTables.representConditional("if p, then (if q, then r)"), customErrors.MULTICONTRATABLE)

    def testRepresentConditionalMultiMalformedPara(self):
        self.assertEqual(representTables.representConditional("if p, then if q then r"), inputValidator.getInput(customErrors.PARAERROR))

    def testRepresentConditionalMultiMalformedPlacePara(self):
        self.assertEqual(representTables.representConditional("if p, (then if q, then r)"), inputValidator.getInput(customErrors.PARAERROR))

    def testRepresentConditionalMultMalformedComma(self):
        self.assertEqual(representTables.representConditional("if p, then (if q then r)"), inputValidator.getInput(customErrors.COMMAERROR))

class testParser(unittest.TestCase):

    def testBreakConditionIntoLor(self):
        self.assertEqual(logicBlocks.evaluateConditional("if p, then q"), "~p or q")

    def testBreakConditionIntoLorMulti(self):
        self.assertEqual(logicBlocks.evaluateConditional("if p, then (if q, then r)"), "~p or (~q or r)")

    def testBreakConditionalIntLorMalformed(self):
        self.assertEqual(logicBlocks.evaluateConditional("if p then q"), inputValidator.getInput(customErrors.COMMAERROR))

    def testParentheses(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, then q)"), True)

    def testParenthesesMalformed(self):
        self.assertEqual(parserParen.evaluateParentheses("if p, then q)"), inputValidator.getInput(customErrors.PARAERROR))

    def testParenthesesMalformedAll(self):
        self.assertEqual(parserParen.evaluateParentheses("if p, then q"), inputValidator.getInput(customErrors.PARAERROR))

    def testParenthesesBadConditional(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p then q)"), inputValidator.getInput(customErrors.COMMAERROR))

    def testParenthesesMulti(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, then (if q, then r))"), True)

    def testParenthesesMultiMalformed(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, then if q, then r)"), inputValidator.getInput(customErrors.PARAERROR))

    def testParenthesesMultiComma(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, then (if q then r))"), inputValidator.getInput(customErrors.COMMAERROR))

    def testParenthesesTooMany(self):
        self.assertEqual(parserParen.evaluateParentheses("((if p, then (if q, then r)))"), parserParen.evaluateParentheses("(if p, then (if q, then r))"))

    def testParenthesesInvalidConditional(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, then if q, (then r))"), inputValidator.getInput(customErrors.PARAERROR))

    def testParenthesesInvalidHypothesis(self):
        self.assertEqual(parserParen.evaluateParentheses("((if p), then (if q, then r))"), inputValidator.getInput(customErrors.PARAERROR))

    def testParenthesesParaBeforeThen(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, (then, if q, then r))"), inputValidator.getInput(customErrors.PARAERROR))

    def testParenthesesBlank(self):
        self.assertEqual(parserParen.evaluateParentheses("()"), inputValidator.getInput(customErrors.BLANKERROR))

    def testParenthesesMisspelledIf(self):
        self.assertEqual(parserParen.evaluateParentheses("(ef p, then q)"), inputValidator.getInput(customErrors.SPELLERROR))

    def testParenthesesMisspelledThen(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, thenq)"), inputValidator.getInput(customErrors.SPELLERROR))

    def testParenthesesExtraCommas(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, then, q)"), inputValidator.getInput(customErrors.COMMAERROR))

    def testParenthesesExtraCommasEverywhere(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p,, then q)"), inputValidator.getInput(customErrors.COMMAERROR))

    def testParenthesesWrongCharacters(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p,. then q)"), inputValidator.getInput(customErrors.SPELLERROR))

    def testParenthesesMissingSpaces(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p,then q)"), inputValidator.getInput(customErrors.SPACEERROR))

    def testParenthesesExtraSpaces(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p,  then q)"), inputValidator.getInput(customErrors.SPACEERROR))

    def testParenthesesUseOfKeyword(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, then then)"), inputValidator.getInput(customErrors.KEYERROR))

    def testParenthesesKeywordOnly(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, then )"), inputValidator.getInput(customErrors.KEYERROR))

    def testParenthesesExtraKeywords(self):
        self.assertEqual(parserParen.evaluateParentheses("(if if p, then q)"), inputValidator.getInput(customErrors.KEYERROR))

    def testParenthesesExtraKeywordsThen(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, then then q)"), inputValidator.getInput(customErrors.KEYERROR))
