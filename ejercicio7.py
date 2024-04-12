import random

def ordenar(lista, orden):
    if orden == "asc":
        for i in range(len(lista) - 1):
            for j in range(len(lista) - 1):
                if lista[j] > lista[j + 1]:
                    aux = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = aux
    elif orden == "des":
        for i in range(len(lista) - 1):
            for j in range(len(lista) - 1):
                if lista[j] < lista[j + 1]:
                    aux = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = aux
    
    return lista

lista = []

for i in range(14):
    lista.append(random.randint(0, 100)) 

ordenar(lista, "asc")
print(f"Lista ordenada de forma ascendente: {lista}")
ordenar(lista, "des")
print(f"Lista ordenada de forma descendente: {lista}")