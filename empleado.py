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
    
    ######
    ######
    #Agregar
    #Borrar
    #Modificar
    #Info de todos
    #Cosulta individual


    





opcion = 1

def SubMenuEmpleado(opcion):
        if opcion == 1:
            #AGREGAR#
            ID = int(input("Dame el ID de el empleado nuevo:"))
            nombre = input("Dame el Nombre del empleado:")
            direccion = input("Dame la direccion de tu empleado:")

            ArchivoEmpleado = open("./archivos/Empleado.txt","a",encoding="utf8")
            ArchivoEmpleado.write(f"{ID}|{nombre}|{direccion}\n")
            
            ArchivoEmpleado.close()
       

SubMenuEmpleado(opcion)



        

