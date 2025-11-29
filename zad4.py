podaj = input("Podaj slowo: ")
lista = []
x = len(podaj)
y = 0
z = 1
for y in range(x):

    lista.append(podaj[y:z])
    y += 1
    z += 1

print(lista)