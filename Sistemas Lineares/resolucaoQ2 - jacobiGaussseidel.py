sistema = [[1, 3, 1],[5, 2, 2],[0,6,8], [-2, 3, -6]]
precisao = 0.05
x0 = [0, 0, 0]

#jacobi jacobi(sistema, termosInd, precisao, x0)

def criterioDasLinhas(sistema):
    flag = True
    if(abs(sistema[0][0]) <= (abs(sistema[0][1]) + abs(sistema[0][2]))):
        flag = False
    if(abs(sistema[1][1]) <= (abs(sistema[1][0]) + abs(sistema[1][2]))):
        flag = False
    if(abs(sistema[2][2]) <= (abs(sistema[2][0]) + abs(sistema[2][1]))):
        flag = False
    return flag

def reordenar(sistema):
    if(criterioDasLinhas(sistema) == False):
        aux = sistema[0]
        sistema[0] = sistema[1]
        sistema[1] = aux
        aux1 = sistema[3]
        aux2 = aux1[0]
        aux1[0] = aux1[1]
        aux1[1] = aux2
        if(criterioDasLinhas(sistema) == False):
            aux = sistema[1]
            sistema[1] = sistema[2]
            sistema[2] = aux
            aux1 = sistema[3]
            aux2 = aux1[1]
            aux1[1] = aux1[2]
            aux1[2] = aux2
            if(criterioDasLinhas(sistema) == False):
                aux = sistema[0]
                sistema[0] = sistema[1]
                sistema[1] = aux
                aux1 = sistema[3]
                aux2 = aux1[0]
                aux1[0] = aux1[1]
                aux1[1] = aux2
                if(criterioDasLinhas(sistema) == False):
                    sistema = -1;
    return sistema

def jacobiX1(sistema, x2, x3, termosInd):
    aux = sistema[0][0]
    aux1 = (termosInd[0] - (sistema[0][1] * x2) - (sistema[0][2] * x3))/aux
    return aux1

def jacobiX2(sistema, x1, x3, termosInd):
    aux = 1/sistema[1][1]
    aux1 = termosInd[1] - (sistema[1][0] * x1) - (sistema[1][2] * x3)
    return aux * aux1

def jacobiX3(sistema, x1, x2, termosInd):
    aux = 1/sistema[2][2]
    aux1 = termosInd[2] - (sistema[2][0] * x1) - (sistema[2][1] * x2)
    return aux * aux1

def parada(ant1, ant2, ant3, atual1, atual2, atual3):
    m1 = atual1 - ant1
    m2 = atual2 - ant2
    m3 = atual3 - ant3
    m1 = abs(m1)
    m2 = abs(m2)
    m3 = abs(m3)
    lista = [m1, m2, m3]
    aux = max(lista)
    if(aux < precisao):
        return False
    else:
        return True;

def jacobi(sistema, precisao, x0):
    flagParada = True;
    ant1 = x0[0]
    ant2 = x0[1]
    ant3 = x0[2]
    sistema = reordenar(sistema)
    it = 0
    while(flagParada):
        atual1 = jacobiX1(sistema, ant2, ant3, sistema[3])
        atual2 = jacobiX2(sistema, ant1, ant3, sistema[3])
        atual3 = jacobiX3(sistema, ant1, ant2, sistema[3])
        flagParada = parada(ant1, ant2, ant3, atual1, atual2, atual3)
        ant1 = atual1
        ant2 = atual2
        ant3 = atual3
        it = it + 1
    print("Numero de iterações: "+ str(it) +"\nValor de x1 = " + str(ant1) + "\nvalor de x2 = " + str(ant2) + "\nvalor de x3 = " + str(ant3) + ".\n")
    
def gaussSeidel(sistema, precisao, x0):
    flagParada = True;
    ant1 = x0[0]
    ant2 = x0[1]
    ant3 = x0[2]
    sistema = reordenar(sistema)
    it = 0
    while(flagParada):
        atual1 = jacobiX1(sistema, ant2, ant3, sistema[3])
        atual2 = jacobiX2(sistema, atual1, ant3, sistema[3])
        atual3 = jacobiX3(sistema, atual1, atual2, sistema[3])
        flagParada = parada(ant1, ant2, ant3, atual1, atual2, atual3)
        ant1 = atual1
        ant2 = atual2
        ant3 = atual3
        it = it + 1
    print("Numero de iterações: "+ str(it) +"\nValor de x1 = " + str(ant1) + "\nvalor de x2 = " + str(ant2) + "\nvalor de x3 = " + str(ant3) + ".\n")

    
print("\n Solução Jacobi: \n")
jacobi(sistema, precisao, x0)
print("\n Solução Gauss-Seidel: \n")
gaussSeidel(sistema, precisao, x0)
