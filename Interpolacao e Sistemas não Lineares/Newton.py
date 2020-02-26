import numpy as np

def parada(x0, x1):
    lista = []
    for i in range (len(x0)):
        lista.append(x0[i] - x1[i])
    return max(lista)


dvX = lambda x,y: 6*x*y
dvY =  lambda x,y: 3*x*x - 3*y*y
dvX1 = lambda x,y: 2*x + y*y*y
dvY1 = lambda x,y: 3*x*y*y

x0 = [-1,-2]
x1 = [0,0]
jb = np.array([[dvX(x0[0], x0[1]),dvY(x0[0], x0[1])],[dvX1(x0[0], x0[1]),dvY1(x0[0], x0[1])]])
solucao = np.array([2, 0])
precisao = 0.001


while True:
    rlc = np.linalg.solve(jb, solucao)
    aux = max(rlc)
    print(rlc)
    for i in range (len(x0)):
        x1[i] = x0[i] + rlc[i]
    if parada(x0, x1) < precisao:
        break
    else:
        x0 = x1
        jb = np.array([[dvX(x0[0], x0[1]),dvY(x0[0], x0[1])],[dvX1(x0[0], x0[1]),dvY1(x0[0], x0[1])]])

print(rlc)       
            
    
    
