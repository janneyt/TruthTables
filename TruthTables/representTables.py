from ..TruthTables import customErrors



'''
################################################################################
Functions that generate representations of truth tables and logical statements
################################################################################
'''

def representOr(p, q):
    '''
    Takes two booleans and generates the corresponding truth table value.

    Boolean, Boolean -> Boolean
    '''
    pass

def representAnd(p, q):
    '''
    Represents two booleans in a AND truth table and returns the corresponding
    truth table value.

    Boolean, Boolean -> Boolean
    '''
    if type(p) != bool or type(q) != bool:
        return customErrors.ERROR
    if p and  q:
        return True
    return False

def representConditional(message):
    '''
    Takes a conditioal statement and returns a string with the truth table for a conditional.

    String -> String
    '''
    pass
