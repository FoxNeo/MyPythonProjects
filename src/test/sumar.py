# DOCtest
def sumar(num1, num2):
    """
    Docu with test
    >>> sumar (4,3)
    7

    >>> sumar (5,4)
    9

    """
    return num1 + num2

result = sumar(2,4)
print(result)

import doctest
doctest.testmod()
# py sumar.py -v