import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "bd_traductor_py")

cursor = mydb.cursor()

palabra = ""
while palabra != 0:
    palabra = input("Ingrese la palabra a traducir: ")
    sentencia = f"select ingles from traductor where espanol like '{palabra}'"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()

    if len(resultado) > 0:
        for x in resultado:
            print(f"(es) {palabra} (in) {x[0]}")
            print("========================================")
    elif palabra != 0:
        print("desea agregarlo al diccionario?")
        respuesta = input("s/n: ")
        print("========================================")
        if respuesta in ["S", "s"]:
            traduccion = input(f"ingrese la traduccion de {palabra}: ")
            sentencia = f"insert into traductor values('defult', '{palabra}', '{traduccion}')"
            cursor.execute(sentencia)
            mydb.commit()
            print(f"{palabra} se ha agregado al diccionario")
            print("========================================")