from math import *
from bicessao import *
from secante import *
from corda import *
from newton import *

diametro = [["Branquial",0.510], ["Radial",0.350], ["Interóssea anterior",0.070]]

a = 0.2802
b = -5.053
c = 0.01324
d = -0.1114
e = math.e

precisao = 0.0000001

for d1 in diametro:
    print(("Artéria: "+str(d1[0])+" - Diâmetro: "+str(d1[1])).center(80))
    d1 = d1[1]
    fun = lambda r: 2*r + 2*r*((a*e**(b*r)+ c*e**(d*r))) - d1

    iA = d1/4
    iB = d1/2

    x0 = d1/2 - d1/4
    x1 = d1/2

    raiz, qttLoop = bicessao(fun, iA, iB, precisao)

    print("Bicessão - Raiz: "+str(raiz)+", Loop: "+str(qttLoop))

    raiz, qttLoop = corda(fun, iA, iB, d/2, precisao)

    print("Corda -    Raiz: "+str(raiz)+", Loop: "+str(qttLoop))

    raiz, qttLoop = secante(fun, x0, x1, precisao)
    
    print("Secante -  Raiz: "+str(raiz)+", Loop: "+str(qttLoop))

    raiz, qttLoop = derivadaNewton(fun, d/2, precisao)

    print("Newton -   Raiz: "+str(raiz)+", Loop: "+str(qttLoop))

    print(fun(raiz))

    print("")

    
