from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self, cedula, nombre, apellido):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido

    @abstractmethod
    def __str__(self):
        return f"{str(self.cedula)}, {self.nombre}, {self.apellido}"

class Alumno(Persona):
    def __init__(self, cedula, nombre, apellido, carrera):
        super().__init__(cedula, nombre, apellido)
        self.carrera = carrera
    
    def __str__(self):
        return f"{super().__str__()}, {self.carrera}"
    
if __name__ == "__main__":
    alumno = Alumno(21546, "Pepe", "Pérez", "informática")
    print(alumno.__str__())