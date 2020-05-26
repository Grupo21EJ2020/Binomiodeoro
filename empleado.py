class Empleado:
    def __init__ (self,idempleado,nombre,direccion):
        self.__idempleado, self.__nombre, self.__direccion = idempleado, nombre, direccion

    @property 
    def idempleado(self):
        return self.__idempleado
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor
    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self,valor):
        self.__nombre = valor



ArchEmple = open("./archivos/Empleado.txt","a",encoding="utf8")

Lineas = ArchEmple.readlines()
Lineas[3] = "esta es la linea 4 indice 3"



ArchEmple.close()
        

