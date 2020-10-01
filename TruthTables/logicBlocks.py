from ..TruthTables import inputValidator, representTables, logicProcBool, parserParen

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

'''
################################################################################
Functions that evaluate a logical statement and break it down to its constituent
elements.
################################################################################
'''

def evaluateConditional(message):
    '''
    Takes a conditional statement and returns a series of logical or statements for further evaluation.

    String -> String
    '''
    pass
