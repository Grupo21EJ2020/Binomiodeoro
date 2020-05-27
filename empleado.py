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
def EmpleadoVigente():
    ArchivoEmpleado = open("./Archivos/Empleado.txt","r",encoding="utf8")
    ArchivoEB = open("./archivos/EmpleadoBorrado.txt","r",encoding="utf8")

    ListaEmpleados = (ArchivoEmpleado.read().splitlines())
    ListaBorrados = (ArchivoEB.read().splitlines())

    ListaEmpleadosVigentes = []

    IDEmpleados = []
    for E in ListaEmpleados:
        N = (E[0:1])
        IDEmpleados.append(N)

    IDEmpleadoSET = set(IDEmpleados)
    ListaEmpleadosSET = set(ListaBorrados)

    final = IDEmpleadoSET - ListaEmpleadosSET
    FINAL = list(final)



    for E in ListaEmpleados:
        N = (E[0:1])
        for S in FINAL:
            if N == S:
                ListaEmpleadosVigentes.append(E)
        else:
            pass
    ArchivoEmpleado.close()
    ArchivoEB.close()
    return(ListaEmpleadosVigentes)    


    







def SubMenuEmpleado(opcion):
        if opcion == 1:
            #AGREGAR#
            ID = int(input("Dame el ID de el empleado nuevo:"))
            nombre = input("Dame el Nombre del empleado:")
            direccion = input("Dame la direccion de tu empleado:")

            ArchivoEmpleado = open("./archivos/Empleado.txt","a",encoding="utf8")
            ArchivoEmpleado.write(f"{ID}|{nombre}|{direccion}\n")
            
            ArchivoEmpleado.close()

        elif opcion == 2:
            IDborrarINT = int(input("Dame la id del empledo que quieres borrar"))
            IDborrarSTR = str(IDborrarINT)

            ArchivoEB = open("./archivos/EmpleadoBorrado.txt","a",encoding="utf8")
            ArchivoEB.write(f"{IDborrarSTR}\n")
            ArchivoEB.close()
            Actualizacion1 = (EmpleadoVigente())
            print(yes)
            print("##Empleado borrado##")
        ## MODIFICAR ##
        elif opcion == 3:
            EmpledoM = int(input("Dame el ID del empleado que quieres modificar"))
            EmpledoMSTR = str(EmpledoM)
            Actualizacion2 = (EmpleadoVigente())
            EmpleadoAModificar = []
            
            for Ac2 in Actualizacion2:
                N = (Ac2[0:1])
                if N == EmpledoMSTR:
                    EmpleadoAModificar.append(Ac2)

            print(EmpleadoAModificar)

opcion = 3
SubMenuEmpleado(opcion)



        

