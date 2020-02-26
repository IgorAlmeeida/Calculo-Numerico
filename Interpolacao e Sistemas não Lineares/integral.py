def derivada(x):
    return 2*x

def funPonto(x):
    return x*x

precisao = 0.1
a = 0.1
b = 1
area = 0
cont = 0

while a < b:
    area += derivada(a)/funPonto(a)
    a += precisao

print(area)
print (cont)


