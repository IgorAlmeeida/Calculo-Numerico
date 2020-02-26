def polinomioLinearPonto(lista, pontos):
    
    for i in range (len(pontos)):
        imagem = 0
        aux = 0
        for j in range (len(lista)):
            lx0 = lista[j]
            inferior = 1
            superior = 1
            for k in range(len(lista)):
                if lista[k][0] != lx0[0]:
                    inferior *= lx0[0] - lista[k][0]
                    superior *= pontos[i] - lista[k][0]
            imagem += lx0[1]*(superior/inferior)
        round(imagem, 4)
        print("X = "+str(pontos[i])+ " -> F(X) = "+str(imagem))

    
rx = [[0,0.2301],[12,0.2077]]
hx = [[0,0.0499],[12,0.0472]]
pontos = [3,6,9]
print("Para o raio interno r(x):")
polinomioLinearPonto(rx, pontos)
print("")
print("Para a espesura h(x)")
polinomioLinearPonto(hx, pontos)

