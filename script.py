lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
print(lista[0], lista[-1], len(lista), max(lista), min(lista), sum(lista), sorted(lista))
lista.append(6)
lista.insert(5, 7)
lista.pop()
lista.reverse()
print(lista)
lista1 = ["xd"]
lista2 = ["xddd"]
lista3 = lista1 + lista2
listaM = lista3*5
print(listaM)

print(lista[:5])
print(lista[5:])
print(lista[5:6:2])
print(lista[::-1])
