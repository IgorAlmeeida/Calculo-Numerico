from fatoraLU import *
from copy import deepcopy

A = [[1, -1, 2],[3, 7, -4],[5, -2,1]]
b = [-2,1,5]
c = [1,-1,3]

L,U = fatoraLu(A)

print("Questão 1".center(120))

print("Matriz L:")
print(L)
print("")
print("Matriz U:")
print (U)
print("")

print("Resolvendo para b = "+str(b))
l1 = deepcopy(L)
u1 = deepcopy(U)
resolverLU(l1,u1,b)
print("")

print("Resolvendo para c = "+str(c))
l1 = deepcopy(L)
u1 = deepcopy(U)
resolverLU(l1,u1,c)

