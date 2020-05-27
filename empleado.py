from os import system,name
def limpiar():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def EmpleadoVigente():
    ##SE CREA LA COMPARACION DE EMPLEADO Y EMPLEADO BORRADO##
    ArchivoEmpleado = open("./Archivos/Empleado.txt","r",encoding="utf8")
    ArchivoEB = open("./archivos/EmpleadoBorrado.txt","r",encoding="utf8")
    ListaEmpleados = (ArchivoEmpleado.read().splitlines())
    ListaBorrados = (ArchivoEB.read().splitlines())
    ListaEmpleadosVigentes = []
    IDEmpleados = []
    for E in ListaEmpleados:
        A = (E.split("|"))
        N = A[0]
        IDEmpleados.append(N)

    IDEmpleadoSET = set(IDEmpleados)
    ListaEmpleadosSET = set(ListaBorrados)

    final = IDEmpleadoSET - ListaEmpleadosSET
    FINAL = list(final)

    for E in ListaEmpleados:
        R = (E.split("|"))
        N = R[0]
        for S in FINAL:
            if N == S:
                ListaEmpleadosVigentes.append(E)
        else:
            pass
    ArchivoEmpleado.close()
    ArchivoEB.close()
    return(ListaEmpleadosVigentes) 

def BorrarLinea(Archivo, Indice, Texto):
    ##SE BORRA 1 LINEA DE UN ARCHIVO##
    lines = open(Archivo, 'r').readlines()
    lines[Indice] = Texto
    out = open(Archivo, 'w')
    out.writelines(lines)
    out.close()

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
    
    
    @classmethod
    def OpciondeEmpleado(self,opcion):
        ##AGREGAR##
        if opcion == 1:
            Lista = []
            contador = 1
            archivo1 = open('./archivos/Numeros.txt', encoding='utf8')
            cont = 6
            for n in archivo1:
                dato = n.split('\n')
                contador = contador - 1
                cont = cont - 1
                Lista.append(dato[0])
                if contador == 0:
                    ID = str(int(dato[0]) + 1)
                    Lista.remove(dato[0])
                    Lista.append(ID)
                archivo2 = open('./archivos/Numeros.txt',"w",encoding = "utf8")
                for a in Lista:
                    archivo2.write(a + '\n')
                archivo2.close()
                if cont == 0:
                    break
            archivo1.close()

            nombre = input("Dame el Nombre del empleado:")
            direccion = input("Dame la direccion de tu empleado:")
            ArchivoEmpleado = open("./archivos/Empleado.txt","a",encoding="utf8")
            ArchivoEmpleado.write(f"{ID}|{nombre}|{direccion}\n")
            ArchivoEmpleado.close()
            limpiar()
            ##ELIMINAR##
        elif opcion == 2:
            IDborrarINT = int(input("Dame la id del empledo que quieres borrar:"))
            IDborrarSTR = str(IDborrarINT)
            ArchivoEB = open("./archivos/EmpleadoBorrado.txt","a",encoding="utf8")
            ArchivoEB.write(f"{IDborrarSTR}\n")
            ArchivoEB.close()
            Actualizacion1 = (EmpleadoVigente())
            limpiar()

        ## MODIFICAR ##
        elif opcion == 3:
            EmpledoM = int(input("Dame el ID del empleado que quieres modificar:"))
            NombreN = input("Dame el nombre nuevo que le quieres poner:")
            DireccionN = input("Dame la direccion nueva que le quieres poner:")
            Indice = EmpledoM - 1
            BorrarLinea("./archivos/Empleado.txt", Indice, f"{EmpledoM}|{NombreN}|{DireccionN}\n")
            limpiar()
        ##CONSULTA ESPECIFICA##
        elif opcion == 5:
            ConsultaEspecifica = int(input("Dame el ID del empledo que quieres consultar:"))
            limpiar()
            ConsultaSRT = str(ConsultaEspecifica)
            Actualizacion2 = (EmpleadoVigente())
            print("-----------------------------------")
            for Z in Actualizacion2:
                O = Z.split("|")
                A = O[0]
                if A == ConsultaSRT:
                    print(Z)
            
        elif opcion == 4:
            ##CONSULTAR TODOS##
            Actualizacion3 = (EmpleadoVigente())
            ArchivoEmpleado = open("./Archivos/Empleado.txt","r",encoding="utf8")
            limpiar()
            print("-----------------------------------")
            ListaEmpleados = (ArchivoEmpleado.read().splitlines())
            
            for F in ListaEmpleados:
                B = F.split("|")
                A = B[0]
                for J in Actualizacion3:
                    S = J.split("|")
                    M = S[0]
                    if A == M:
                        print(F)
                    else:
                        pass