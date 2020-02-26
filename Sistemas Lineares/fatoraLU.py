#subtração das linhas de uma matriz
def subLinha(linha1, linha2, mul):
    for i in range(len(linha1)):
       linha1[i] = linha1[i] - mul*linha2[i]

    return linha1
#total de multiplicadores
def numMul (tam):
    suma = 0
    for i in range (tam - 1):
        suma += i+1
    print (suma)
    return suma

#realizar a solução para X e Y
def subY(y,l):
    sub = 0
    for i in range(len(y)):
        sub += y[i]*l[i]
    return sub

#fatora a matriz a em duas Matrizes L e U
def fatoraLu(A):

    mp= []

    L = []
    p1 = 0
    X = []
    Y = []

    #preenche a matriz L com elementos 0 e na diagonal elementos 1
    for i in range(len(A)):
        lista = []
        for j in range (len(A)):
            lista.append(0)
        lista[p1] = 1
        p1 += 1
        L.append(lista)

    #variaveis de controle dos loops
    controle_loop1 = len(A)-1
    controle_multi = len(A)-1
    controle_sub = len(A)-1
    cont = 0

    #função que calcula os multiplicadores
    mul = lambda x, y: x/y

    k = 0
    z = 0
    i = 0
    j = 0
    save_k = 0
    save_i = 0
    #loop ocorrencia de opecação na matrizes
    while(controle_loop1 > 0):
        x = A[z][z]
        #loop definir multiplicadores
        while(controle_multi > 0):
            cont += 1
            m = mul(A[k+1][z],x)
            L[k+1][z] = m
            mp.append(m)
            k += 1
            controle_multi -= 1
        #loop realizar operação de subtração
        while(controle_sub > 0):
            A[i+1] = subLinha(A[i+1],A[z],mp[j])
            i += 1
            j += 1
            controle_sub -= 1
        z += 1
        i = save_i + 1
        save_i = i
        k = save_k + 1
        save_k = k
        controle_multi = cont - 1
        controle_sub = cont - 1
        controle_loop1 -= 1
        cont = 0
    
    U = A
    return L, U

def resolverLU(L,U, b):
    X = []
    Y = []
    #preenchendo os vetores X e Y com elementos 0
    for a in range (len(U)):
        Y.append(0)
        X.append(0)

    #primeiro elemento do vetor Y
    Y[0] = b[0]

    #encontrando os outros elementos do vetor Y
    for i in range (len(Y)-1):
        l = L[i+1]
        Y[i+1]= (b[i+1] - subY(Y[0:i+1],l[0:i+1]))/l[i+1]

    #revertendo as matrizes Y e U para encontrar para X
    Y.reverse()
    U.reverse()

    #resolvendo para o último elemento de X
    X[0] = Y[0]/U[0][len(U[0])-1]

    #encontrando os outros elementos de X
    for i in range (len(X)-1):
        u = U[i+1]
        u.reverse()
        X[i+1]= (Y[i+1] - subY(X[0:i+1],u[0:i+1]))/u[i+1]


    #deixando X na ordem correta
    X.reverse()

    #exibindo a solução do sistema
    for g in range(len(X)):
        print ("X"+str(g+1)+" = "+str(X[g]))
