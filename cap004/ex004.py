lista = [0, 1, 2, 3, 4]

def square(x):
        return (x**2)
    
def cube(x):
        return (x**3)

funcs = [square, cube]

for i in lista:
    valor = map(lambda x: x(i), funcs)
    print(list((valor)))
