class Alumno:
    def __init__(self):
        self.notas = []

    def get_notas(self):
        return self.notas

    def llenar_notas(self, nota1, nota2, nota3):
        self.notas.append(nota1)
        self.notas.append(nota2)
        self.notas.append(nota3)

    def promedio(self):
        return (self.notas[0] + self.notas[1] + self.notas[2]) / 3

if __name__ == "__main__":
    nota = []

    for i in range(3):
       nota.append(int(input(f"introduce la nota {i + 1}: ")))

    alumno1 = Alumno()
    alumno1.llenar_notas(nota[0], nota[1], nota[2])

    print("----------notas----------")
    print(alumno1.get_notas())
    print(f"Promedio: {alumno1.promedio()}")
    
    if alumno1.promedio() < 1.7:
        print(f"Estás reprovado")
    else:
        print(f"Estás aprovado")