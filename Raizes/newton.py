import math

def derivar(fun,x,e):
    return (fun(x+e) - fun(x))/e
    

def derivadaNewton(fun,x,e):
    interacao = lambda x: x - fun(x)/derivar(fun,x,e)
    raiz = interacao(x)
    cont = 1
    
    while(abs(raiz - x)> e):
        if (fun(raiz) == 0):
            break
        else:
            x = raiz
            raiz = interacao(raiz)
        cont += 1
    return raiz, cont




    
