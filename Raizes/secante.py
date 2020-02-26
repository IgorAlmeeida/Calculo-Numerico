from math import *

def secante(fun,x0,x1,e):
    f0 = fun(x0)
    cont = 0
    while(True):
        f1 = fun(x1)
        x2 = x1 - ((x1-x0)*f1/(f1-f0))
        if(abs(x2 - x1) < e):
            return x2, cont
        else:
            x0 = x1
            x1 = x2
            f0 = f1
        cont += 1

