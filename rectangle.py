
def area(a, b): 
    if a == 0 or b == 0:
        return "erorr"
    elif isinstance(a, int) and isinstance(b, int):
        if a < 0 or b<0:return "erorr"
        else: return a * b
    else:
        return "erorr"

def perimeter(a, b): 
    if a == 0 or b == 0:
        return "erorr"
    elif isinstance(a, int) and isinstance(b, int):
        if a < 0 or b<0: return "erorr"
        else:return (a + b)*2
    else:
        return "erorr"
