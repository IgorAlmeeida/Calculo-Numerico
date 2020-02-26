from math import log

def corda (fun, a, b, Xk, e):
    m = (fun(b) - fun(a)/(b-a))
    Xk1 = Xk - (fun(Xk)/m)
    cont = 1
    
    while (abs(Xk1 - Xk) > e):
        if(fun(Xk) == 0):
            break
        else:
            Xk = Xk1
            Xk1 = Xk - (fun(Xk)/m)
        cont += 1
    return Xk1, cont

