import unittest
from ..TruthTables import inputValidator, representTables, logicProcBool, logicBlocks, parserParen

TRUE = 'T'
FALSE = 'F'
ANDTABLE = '\n:p  :q  :p and q\n:T  :T  :T\n:T  :F  :F\n:F  :T  :F\n:F  :F  :F\n'
ERROR = ("Something went wrong, please enter values again. This program only"
        + "accepts boolean values in most functions.")

INITERROR = ("Something went wrong with your logicProcBool.logical equivalence. Please only"
        + "enter approved characters. Type -h for usage or to see approved characters.")

CONDTABLE = '\n:p  :q  :p -> q\n:T  :T  :T\n:T  :F  :T\n:F  :F  :T\n:T  :F  :F\n'

CONDERROR = ("Something is wrong with the syntax of your conditional statement."
        + "Remember that conditionals must be expressed in the form\"if p then q\"."
        + "Type -h for usage and additional details.")

CONTRACONDTABLE = '\n:p  :q  :p -> q\n:T  :F  :F\n:F  :T  :T\n'

CONTRACOND = ("You have entered a contradiction of the form \"if p then ~p\"."
        + "Since a conditional is false whenever the hypothesis is true but"
        + "the conclusion is false, this statement has the following truth table:"
        + CONTRACONDTABLE
        + "This leads to a contradiction. Please make sure you entered the"
        + "correct values. Would you like to reenter your input? Y/n")

CONTRATAUT = ("You have entered a tautology of the form \"if p then p\". This is"
        + "...rather obvious, don't you think? Did you enter the correct"
        + "input? Would you like to reenter input? Y/n")

MULTICONTRATABLE = ("\n:p  :q  :r  :p -> (q -> r)\n:T  :T  :T  :T\n:T  :F  :T  "
        +":T\n:T  :T  :F  :F\n:F  :T  :T  :T\n:F  :F  :T  :T\n:F  :F  :F  :T\n")

PARAERROR = ("You are missing at least one parenthesis. Please adjust your input"
        + " and make sure you provide parenthesis for all multiple clause expressions.")

COMMAERROR = ("You have attempted to enter an expression using a conditional, but "
        +"you forgot to separate clauses with a comman (,).\nThe hypothesis and"
        +"conclusion of a logicProcBool.logical statement must be separated by a comma, or else"
        +"the world ends.")

ALLOWEDSYMBOLS = ("\nlogicProcBool.logical and: and\n"
        +"logicProcBool.logical or: or\n"
        +"logicProcBool.logical conditional: if {valid character a-z, A-A, no numbers}, then"
        +"{valid character a-z, A-Z, no numbers}"
        +"\nNote: please remember to insert the comma between the if and then clause,"
        +"as this helps the interpreter "
        +"understand your nonsense.\n"
        +"logicProcBool.logical not: ~"
        +"Parentheses: separates clauses. ( ) must be around EVERY clause.")

USAGE = ("To use this truth table script, you need to type in a logicProcBool.logical proposition "
        +"with each clause separated by parentheses.\nEvery logicProcBool.logical operator must "
        +"be in its own separate clause.\n"
        +"For instance, to write \"if p then, if q, then r\" you would input "
        +"\"if p, then (if q, then r).\nUse the words \"if\" and \"then\" instead "
        +"of logicProcBool.logical operators due to symbol ambiguity.\nDo not use synomyms for"
        +"\"if\" and \"then\" such as \"unless\". It scares the computer.\n"
        +"Allowed expressions and symbols:"
        +ALLOWEDSYMBOLS)

BLANKERROR = ("You have entered at least one blank pair of parentheses."
        +"Please repent of your sins and enter again.")

SPELLERROR = ("A keyword, such as \'if\' or \'and'\' has been misspelled or is "
        +"in the wrong location in the proposition.\nPlease repent of your sins "
        +"and enter your proposition again.\nFor usage details type -h.")

SPACEERROR = ("There must be one (1) and only one (1) space between keywords "
        +"and logicProcBool.logical operators.\n")

KEYERROR = ("You have attempted to use a keyword in an invalid place, such as "
        +"after another valid keyword.\nRepent of your sins and enter your "
        +"proposition again.\n")

class testInput(unittest.TestCase):

    def testInput(self):
        self.assertEqual(inputValidator.initInput("a and b"), ANDTABLE)

    def testInputIntegerAlone(self):
        self.assertEqual(inputValidator.initInput(1), inputValidator.getInput(INITERROR))

    def testInputIntegerSymbols(self):
        self.assertEqual(inputValidator.initInput("a^b"), inputValidator.getInput(INITERROR))

    def testInputString(self):
        self.assertEqual(inputValidator.initInput("Hello world"), inputValidator.getInput(INITERROR))

    def testInputBoolean(self):
        self.assertEqual(inputValidator.initInput(True), inputValidator.getInput(INITERROR))

    def testInputIntegerMisspelled(self):
        self.assertEqual(inputValidator.initInput("a adn b"), inputValidator.getInput(INITERROR))

    def testInputIntegerError(self):
        self.assertEqual(inputValidator.initInput(INITERROR), inputValidator.getInput(INITERROR))

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
        self.assertEqual(logicProcBool.logicAnd("Hi", "World"), inputValidator.getInput(ERROR))

    def testAndInteger(self):
        self.assertEqual(logicProcBool.logicAnd(1,2), inputValidator.getInput(ERROR))

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
        self.assertEqual(representTables.representAnd("False", "True"), inputValidator.getInput(ERROR))

    def testrepresentAndInteger(self):
        self.assertEqual(representTables.representAnd(1,0), inputValidator.getInput(ERROR))

    def testrepresentOrTT(self):
        self.assertEqual(representTables.representOr(True, True), True)

    def testrepresentOrString(self):
        self.assertEqual(representTables.representOr("True", "False"), inputValidator.getInput(ERROR))

    def testrepresentOrInteger(self):
        self.assertEqual(representTables.representOr(1, 0), inputValidator.getInput(ERROR))

    def testrepresentFF(self):
        self.assertEqual(representTables.representOr(False, False), False)

    def testrepresentFT(self):
        self.assertEqual(representTables.representOr(False, True), True)

    def testrepresentOrTF(self):
        self.assertEqual(representTables.representOr(True, False), True)

    def testrepresentConditional(self):
        self.assertEqual(representTables.representConditional("if p, then q"), CONDTABLE)

    def testrepresentConditionalMalformed(self):
        self.assertEqual(representTables.representConditional("f p, then q"), inputValidator.getInput(CONDERROR))

    def testrepresentConditionalCommaMiss(self):
        self.assertEqual(representTables.representConditional("if p then q"), inputValidator.getInput(COMMAERROR))

    def testRepresentConditionalInteger(self):
        self.assertEqual(representTables.representConditional(1), inputValidator.getInput(CONDERROR))

    def testRepresentConditionalBoolean(self):
        self.assertEqual(representTables.representConditional(True), inputValidator.getInput(CONDERROR))

    def testRepresentConditionalContradiction(self):
        self.assertEqual(representTables.representConditional("if p, then ~p"), inputValidator.getInput(CONTRACOND))

    def testRepresentConditionalTautology(self):
        self.assertEqual(representTables.representConditional("if p, then p"), inputValidator.getInput(CONTRATAUT))

    def testRepresentConditionalMultiple(self):
        self.assertEqual(representTables.representConditional("if p, then (if q, then r)"), MULTICONTRATABLE)

    def testRepresentConditionalMultiMalformedPara(self):
        self.assertEqual(representTables.representConditional("if p, then if q then r"), inputValidator.getInput(PARAERROR))

    def testRepresentConditionalMultiMalformedPlacePara(self):
        self.assertEqual(representTables.representConditional("if p, (then if q, then r)"), inputValidator.getInput(PARAERROR))

    def testRepresentConditionalMultMalformedComma(self):
        self.assertEqual(representTables.representConditional("if p, then (if q then r)"), inputValidator.getInput(COMMAERROR))

class testParser(unittest.TestCase):

    def testBreakConditionIntoLor(self):
        self.assertEqual(logicBlocks.evaluateConditional("if p, then q"), "~p or q")

    def testBreakConditionIntoLorMulti(self):
        self.assertEqual(logicBlocks.evaluateConditional("if p, then (if q, then r)"), "~p or (~q or r)")

    def testBreakConditionalIntLorMalformed(self):
        self.assertEqual(logicBlocks.evaluateConditional("if p then q"), inputValidator.getInput(COMMAERROR))

    def testParentheses(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, then q)"), True)

    def testParenthesesMalformed(self):
        self.assertEqual(parserParen.evaluateParentheses("if p, then q)"), inputValidator.getInput(PARAERROR))

    def testParenthesesMalformedAll(self):
        self.assertEqual(parserParen.evaluateParentheses("if p, then q"), inputValidator.getInput(PARAERROR))

    def testParenthesesBadConditional(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p then q)"), inputValidator.getInput(COMMAERROR))

    def testParenthesesMulti(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, then (if q, then r))"), True)

    def testParenthesesMultiMalformed(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, then if q, then r)"), inputValidator.getInput(PARAERROR))

    def testParenthesesMultiComma(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, then (if q then r))"), inputValidator.getInput(COMMAERROR))

    def testParenthesesTooMany(self):
        self.assertEqual(parserParen.evaluateParentheses("((if p, then (if q, then r)))"), parserParen.evaluateParentheses("(if p, then (if q, then r))"))

    def testParenthesesInvalidConditional(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, then if q, (then r))"), inputValidator.getInput(PARAERROR))

    def testParenthesesInvalidHypothesis(self):
        self.assertEqual(parserParen.evaluateParentheses("((if p), then (if q, then r))"), inputValidator.getInput(PARAERROR))

    def testParenthesesParaBeforeThen(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, (then, if q, then r))"), inputValidator.getInput(PARAERROR))

    def testParenthesesBlank(self):
        self.assertEqual(parserParen.evaluateParentheses("()"), inputValidator.getInput(BLANKERROR))

    def testParenthesesMisspelledIf(self):
        self.assertEqual(parserParen.evaluateParentheses("(ef p, then q)"), inputValidator.getInput(SPELLERROR))

    def testParenthesesMisspelledThen(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, thenq)"), inputValidator.getInput(SPELLERROR))

    def testParenthesesExtraCommas(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, then, q)"), inputValidator.getInput(COMMAERROR))

    def testParenthesesExtraCommasEverywhere(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p,, then q)"), inputValidator.getInput(COMMAERROR))

    def testParenthesesWrongCharacters(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p,. then q)"), inputValidator.getInput(SPELLERROR))

    def testParenthesesMissingSpaces(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p,then q)"), inputValidator.getInput(SPACEERROR))

    def testParenthesesExtraSpaces(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p,  then q)"), inputValidator.getInput(SPACEERROR))

    def testParenthesesUseOfKeyword(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, then then)"), inputValidator.getInput(KEYERROR))

    def testParenthesesKeywordOnly(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, then )"), inputValidator.getInput(KEYERROR))

    def testParenthesesExtraKeywords(self):
        self.assertEqual(parserParen.evaluateParentheses("(if if p, then q)"), inputValidator.getInput(KEYERROR))

    def testParenthesesExtraKeywordsThen(self):
        self.assertEqual(parserParen.evaluateParentheses("(if p, then then q)"), inputValidator.getInput(KEYERROR))
