traductor = {"arriba": "up", "brazo": "arm", "corazón": "hart", "dios": "god", "estadio": "stadium", "frio": "cold"}

salir = False
while not salir:
    palabra = input("Introduce una palabra: ")
    if palabra in traductor:
        print(f"es: {palabra} - en: {traductor[palabra]}")
        print("--------------------")
    elif palabra != "" and palabra != "0":
        print(f"la palabra {palabra} No se encuentra en este diccionario, desea agregarla?")
        respuesta = input("(y/n): ")
        if respuesta == "y":
            traduccion = input(f"Escribe la traducción de {palabra}: ")
            traductor.update({palabra: traduccion})
            print(f"La palabra {palabra} se añadió al diccionario")
            print("--------------------")
    else:
        salir = True