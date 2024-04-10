import random

class Nodo:
    dato = None
    siguiente = None

    def __init__(self, dt):
        self.dato = dt
        self.siguiente = None
    
    def getDato(self):
        return self.dato
    
    def getSiguiente(self):
        return self.siguiente

    def setDato(self, dt):
        self.dato = dt

    def setSiguiente(self, sg):
        self.siguiente = sg

class Lista:
    cabeza = None

    def __init__(self):
        self.cabeza = None

    def esVacio(self):
        return self.cabeza == None
    
    def longitud(self):
        if(self.esVacio()):
            return 0
        else: 
            puntero = self.cabeza
            count = 1
            while(puntero.getSiguiente() != None):
                puntero = puntero.getSiguiente()
                count += 1
            return count

    def agregar(self, dt):
        nodo1 = Nodo(dt)
        if(self.esVacio()):
            self.cabeza = nodo1
        else:
            puntero = self.cabeza
            while(puntero.getSiguiente() != None):
                puntero = puntero.getSiguiente()
            puntero.setSiguiente(nodo1)

    def mostrar(self, pos):
        if(self.esVacio()):
            print("Error!, la lista está vacia")
        elif(pos < 0 or pos > self.longitud() - 1):
            print("Error!, posicion no valida")
        else:
            puntero = self.cabeza
            count = 0
            while(count < pos):
                puntero = puntero.getSiguiente()
                count += 1
            return puntero.getDato() 

    def insertar(self, dt, pos):
        nodo2 = Nodo(dt)
        if(self.esVacio()):
            print("Error!, la lista está vacia")
        elif(pos < 0 or pos > self.longitud() - 1):
            print("Error!, posicion no valida")
        elif(pos == 0):
            nodo2.setSiguiente(self.cabeza)
            self.cabeza = nodo2
        else:
            puntero = self.cabeza
            count = 0
            while(count < pos - 1):
                puntero = puntero.getSiguiente()
                count += 1
            nodo2.setSiguiente(puntero.getSiguiente())
            puntero.setSiguiente(nodo2)
    
    def eliminar(self, pos):
        if(self.esVacio()):
            print("Error!, la lista está vacia")
        elif(pos < 0 or pos > self.longitud() - 1):
            print("Error!, posicion no valida")
        elif(pos == 0):
            self.cabeza = cabeza.getSiguiente()
        else:
            puntero = self.cabeza
            count = 0
            while(count < pos - 1):
                puntero = puntero.getSiguiente()
                count += 1
            puntero.setSiguiente(puntero.getSiguiente().getSiguiente())

    def busquedaLineal(self, elemento):
        pos = -1
        puntero = self.cabeza
        count = 0
        while(count < self.longitud()):
            if(puntero.getDato() == elemento):
                pos = count
                break
            puntero = puntero.getSiguiente()
            count += 1
        return count

    def vaciar(self):
        self.cabeza = None
    
if __name__ == "__main__":
    lista1 = Lista()
    opcion = 1
    while(opcion != 0):
        print("(1): Llenar lista aleatoriamente")
        print("(2): Llenar lista de forma manual")
        print("(3): Agregar elemento")
        print("(4): Comprobar si la lista está vacia")
        print("(5): Mostrar longitud de la lista")
        print("(6): Mostrar elemento en alguna posición")
        print("(7): Insertar elemento en alguna posición")
        print("(8): Eliminar elemento en alguna posición")
        print("(9): Comprobar si un elemento se encuentra en la lista")
        print("(10): Imprimir lista")
        print("(11): Vaciar lista")
        print("(0): Salir")
        opcion = int(input("Seleccione: "))
        print("-----------------------------------")

        if(opcion == 1):
            if(not lista1.esVacio()):
                print("Error!, la lista ya está llena")
            else:
                long = int(input("Defina la longitud inicial de la lista: "))
                for i in range(0, long):
                    lista1.agregar(str(random.randint(0, 50)))
                print("Se llenó la lista")
        elif(opcion == 2):
            if(not lista1.esVacio()):
                print("Error!, la lista ya está llena")
            else:
                long = int(input("Defina la longitud inicial de la lista: "))
                for i in range(0, long):
                    el = input(f"Agrega el elemento {i}: ")
                    lista1.agregar(el)
                print("Se llenó la lista")
        elif(opcion == 3):
            el = input("Introduce el dato que desa agregar: ")
            lista1.agregar(el)
        elif(opcion == 4):
            if(lista1.esVacio()):
                print("La lista está vacia")
            else:
                print("La lista no está vacia")
        elif(opcion == 5):
            print(f"La longitud de la lista es: {lista1.longitud()}")
        elif(opcion == 6):
            pos = int(input("Introduce una posición: "))
            if(lista1.esVacio()):
                print("Error!, la lista está vacia")
            elif(pos < 0 or pos > lista1.longitud() - 1):
                print("Error!, posicion no valida")
            else:
                print(f"El elemento en la posición {pos} es: {lista1.mostrar(pos)}")
        elif(opcion == 7):
            dat = input("Introduce un dato: ")
            pos = int(input("Introduce una posición: "))
            if(lista1.esVacio()):
                print("Error!, la lista está vacia")
            elif(pos < 0 or pos > lista1.longitud() - 1):
                print("Error!, posicion no valida")
            else:
                lista1.insertar(dat, pos)
                print("Elemento agregado")
        elif(opcion == 8):
            pos = int(input("Introduce una posición: "))
            if(lista1.esVacio()):
                print("Error!, la lista está vacia")
            elif(pos < 0 or pos > lista1.longitud() - 1):
                print("Error!, posicion no valida")
            else:
                lista1.eliminar(pos)
                print("elemento eliminado")
        elif(opcion == 9):
            dat = input("Introduce el elemento que desea comprobar: ")
            if(lista1.busquedaLineal(dat) == -1):
                print(f"El elemento: {dat} no se encuentra en la lista")
            else:
                print(f"El elemento: {dat} se encuentra en la posición {lista1.busquedaLineal(dat)} de la lista")
        elif(opcion == 10):
                if(lista1.esVacio()):
                    print("Error!, la lista está vacia")
                else:
                    for i in range(0, lista1.longitud()):
                        print(f"({i}): {lista1.mostrar(i)}")
        elif(opcion == 11):
            lista1.vaciar()
            print("La lista se vació")
        elif(opcion == 0):
            print("Salió")
        else:
            print("Opción no valida")
        print("-----------------------------------")