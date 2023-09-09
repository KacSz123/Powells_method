import re
import numpy as np

REPLACE = {
    'sin': 'np.sin',
    'cos': 'np.cos',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**',
    'pi' : 'np.pi',
    'abs' : 'np.absolute',
    'tan' : 'np.tan',
    'atan' : 'np.arctan'
}

ALLOWED = {
    'x1', 'x2', 'x3', 'x4', 'x5',
    'sin',
    'cos',
    'exp',
    'sqrt',
    'pi',
    'abs',
    'tan',
    'atan'
}

# function parser sing white list
def parseFunction(funcString: str):
    
    #Looking for not allowed expressions. If one is found, an exception is thrown.
    for expr in re.findall('[a-zA-Z_]+[0-9]*', funcString):
        if(expr not in ALLOWED):
            raise Exception(f'{expr} is not allowed in function')

    #Searching for and replacing expressions (i.e. "sin" to "np.sin")
    funcString = re.sub(r"([\d]+)([a-zA-Z_])", r"\1*\2", funcString)
    for toReplace, newValue in REPLACE.items():
        funcString = funcString.replace(toReplace, newValue)
    print(funcString)

    def func(x1=0, x2=0, x3=0, x4=0, x5=0):
        return eval(funcString)

    return func