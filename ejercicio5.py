usuarios_autenticados = {"admin": "4321", "leo": "1234", "pp": "546"}

usuario = input("Introduce el usuario: ")

if usuario in usuarios_autenticados:
    intentos = 3

    while(intentos > 0):
        contraseña = input("Introduce la contraseña: ")

        if contraseña == usuarios_autenticados[usuario]:
            print("Contraseña correcta, acceso concedido")
            break
        else:
            print("contraseña incorrecta, acceso denegado")
            intentos -= 1
            print(f"Te quedan {intentos} intento(s)")
            print("--------------------------------")
            if intentos == 0:
                print("¡¡Cuenta bloqueada!!")
else:
    print("El usuario no existe")