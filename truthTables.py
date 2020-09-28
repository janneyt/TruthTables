TRUE = 'T'
FALSE = 'F'
ANDTABLE = '\n:p  :q  :p and q\n:T  :T  :T\n:T  :F  :F\n:F  :T  :F\n:F  :F  :F\n'
ERROR = ("Something went wrong, please enter values again. This program only"
        + "accepts boolean values in most functions.")

INITERROR = ("Something went wrong with your logical equivalence. Please only"
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

def getInput(message):
    pass

def initInput(message):
    pass

def representOr(p, q):
    pass

def representAnd(p, q):
    '''
    represents two booleans in an AND truth table and returns the corresponding
    truth table value.

    Boolean, Boolean -> Boolean
    '''
    if type(p) != bool or type(q) != bool:
        return ERROR
    if p and  q:
        return True
    else:
        return False

def logicAnd(p, q):
    '''
    Takes a pair of boolean values and returns a string to be printed indicating
    truth table for that pair of boolean AND expressions.

    Boolean, Boolean -> string
    '''
    eval = representAnd(p, q)
    if type(p) != bool or type(q) != bool:
        return ERROR
    return_eval = ':p  :q  :p and q\n:'

    if eval == True:
        return return_eval + TRUE + '  :' + TRUE + '  :' +TRUE + '\n'
    elif p == True:
        if q == False:
            return return_eval + TRUE+'  :'+FALSE+'  :'+FALSE+'\n'
        else:
            return ERROR
    elif p == False:
        if q == False:
            return return_eval + FALSE+'  :'+FALSE+'  :'+FALSE+'\n'
        elif q == True:
            return return_eval + FALSE+'  :'+TRUE+'  :'+FALSE+'\n'
        else:
            return ERROR
    else:
        return ERROR

def representConditional(message):
    '''
    Takes a conditioal statement and returns a string with the truth table for a conditional.

    String -> String
    '''
