# Jesús López Funes

from typeguard import typechecked
from abc import ABC, abstractmethod


class Informes(ABC):
    @abstractmethod
    def generarInforme(self):
        pass


@typechecked
class Empleado:
    def __init__(self, nombre: str, id: int, salario: float):
        self.__nombre = nombre
        self.__id = id
        self.__salario = salario

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,value):
        self.__nombre = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,value):
        self.__id = value

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self,value):
        self.__salario = value

    def __str__(self):
        return f"nombre {self.nombre}, id: {self.id}, salario: {self.salario}"


@typechecked
class Gerente(Empleado, Informes):
    def __init__(self, nombre: str, id: int, salario: float,departamento: str):
        super().__init__(nombre, id, salario)
        self.__departamento = departamento

    def generarInforme(self):
        return f"El gerente {self.nombre} trabaja en el departamento {self.__departamento}"


@typechecked
class Desarrollador(Empleado, Informes):
    def __init__(self, nombre: str, id: int, salario: float, lenguaje: str):
        super().__init__(nombre, id, salario)
        self.__lenguaje = lenguaje

    def generarInforme(self):
        return f"El gerente {self.nombre} trabaja en el departamento {self.__lenguaje}"


@typechecked
class BDEmpleados:
    def __init__(self):
        self.__empleados = {}

    def insertarEmpleado(self, empleado):
        self.__empleados[empleado.id] = empleado

    def verEmpleado(self, id):
        if id in self.__empleados:
            print(self.__empleados[id].generarInforme())
        else:
            print(f"No se ha encontrado el empleado con id {id}")

    def informe(self):
        for empleado in self.__empleados.values():
            print(empleado.generarInforme())


# Crear instancias de empleados
ger1 = Gerente("Luís Martínez", 1, 60000, "Proyectos Web")
ger2 = Gerente("Ana Torrija", 2, 50000, "Marketing")
des1 = Desarrollador("Ana García", 4, 40000, "Python")
des2 = Desarrollador("José Flores", 5, 30000, "Java")

# Crear BD de empleados
bd1 = BDEmpleados()

# Insertar empleados en la BD
bd1.insertarEmpleado(ger1)
bd1.insertarEmpleado(ger2)
bd1.insertarEmpleado(des1)
bd1.insertarEmpleado(des2)

print ("\nDatos del Empleado 1 y 3: ")
print("=======================")
bd1.verEmpleado(1)
bd1.verEmpleado(3)

# Generar e imprimir informes
print ("\nInforme de todos los empleados: ")
print ("=================================")
bd1.informe()


