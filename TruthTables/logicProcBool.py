from ..TruthTables import customErrors, representTables


'''
################################################################################
Functions that evaluate truth tables
################################################################################
'''

def logicAnd(p, q):
    '''
    Takes a pair of boolean values and returns a string to be printed indicating
    truth table for that pair of boolean AND expressions.

    Boolean, Boolean -> string
    '''
    evalLogic = representTables.representAnd(p, q)
    if type(p) != bool or type(q) != bool:
        return customErrors.ERROR
    return_eval = ':p  :q  :p and q\n:'
    return logicAndProcessing(evalLogic, p, q, return_eval)


def logicAndProcessing(evalLogic, p, q, return_eval):
    if evalLogic is True:
        return return_eval + customErrors.TRUE + '  :' + customErrors.TRUE + '  :' + customErrors.TRUE + '\n'
    if p is True:
        if q is False:
            return return_eval + customErrors.TRUE +'  :'+ customErrors.FALSE+'  :'+ customErrors.FALSE+'\n'
        return customErrors.ERROR
    if p is False:
        if q is False:
            return return_eval + customErrors.FALSE+'  :'+ customErrors.FALSE+'  :'+ customErrors.FALSE+'\n'
        if q is True:
            return return_eval + customErrors.FALSE+'  :'+ customErrors.TRUE+'  :'+ customErrors.FALSE+'\n'
        return customErrors.ERROR
    return customErrors.ERROR
