def area(a, h): 
    if a == 0 or h == 0:
        return "erorr"
    elif isinstance(a, int) and isinstance(h, int):
        if a<0 or h<0:return "erorr"
        else:return a * h / 2
    else:
        return "erorr"
     

def perimeter(a, b, c): 
    if a == 0 or b == 0 or c == 0:
        return "erorr"
    elif isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
        if a<0 or b<0 or c<0 :return "erorr"
        elif(a+b < c) or (a+c < b) or(c+b < a):return "erorr"
        else:return a + b + c 
    else:
        return "erorr"
    
