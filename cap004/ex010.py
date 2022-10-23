lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for indice, valor in enumerate(lista):
    if indice <= 5:
        continue
    else:
        print (valor)