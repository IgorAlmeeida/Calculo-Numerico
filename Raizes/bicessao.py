from math import log

def bicessao(fun, a, b, e):
    y = (b - a)/2
    y = y/e
    numPassos = log(y, 2)
    numPassos = numPassos - 1
    numPassos = int(numPassos)
    numPassos1 = numPassos
    while(numPassos > 0):
        Xk = (b + a)/2
        if (fun(Xk) == 0):
            break
        elif (fun(Xk)*fun(b) < 0):
            a = Xk
        else:
            b = Xk
        numPassos-= 1
    return Xk, numPassos1 
        
