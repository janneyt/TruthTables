TRUE = 'T'
FALSE = 'F'
ANDTABLE = '\n:p  :q  :p and q\n:T  :T  :T\n:T  :F  :F\n:F  :T  :F\n:F  :F  :F\n'
ERROR = "Something went wrong, please enter values again. This program only accepts boolean values in most functions."

def evaluateOr(p, q):
    pass

def evaluateAnd(p, q):
    '''
    Evaluates two booleans in an AND truth table and returns the corresponding
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
    eval = evaluateAnd(p, q)
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
