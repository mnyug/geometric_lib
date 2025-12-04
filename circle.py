import math


def area(r):
    '''Принимает радиус круга и возращает его площадь'''
    if  r == 0:
        return "erorr" 
    elif isinstance(r, int):
        if r < 0:
            return "erorr"
        else: return math.pi * r * r
    else:
        return "erorr"
    


def perimeter(r):
    '''Принимает радиус круга и возращает его периметр'''
    if  r == 0:
        return "erorr" 
    elif isinstance(r, int):
        if r < 0:
            return "erorr"
        else: return math.pi * r * 2
    else:
        return "erorr"
    


