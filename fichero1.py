nombre = input("nombra el archivo: ")
texto = input("Introduce un texto: ")
nombre_archivo = f"archivo_{nombre}.txt"
f = open(nombre_archivo, 'w')

for i in range(50):
    f.write(f"{texto}\n")
    
f.close()