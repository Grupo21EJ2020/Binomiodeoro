class TEMAS:
    def __init__ (self,idtema,nombre):
        self.__idtema, self.__nombre = idtema, nombre    
    @property 
    def idtema(self):
        return self.__idtema
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor
    @idtema.setter
    def idtema(self):
        self.__idtema   
    #-------------------------------------------------------------------------------------------
    def AgregarTema(self):
        archivo = open('./archivos/Temas.txt','a',encoding='utf8')
        archivo.write(self.__idtema + '|' + self.__nombre + '\n')
        archivo.close()
    
    @classmethod
    def Agregar(self,ubi,ubi2,contador):
        nombre = input('Nombre: ')
        Lista = []
        archivo1 = open(ubi2, encoding='utf8')
        cont = 6
        for n in archivo1:
            dato = n.split('\n')
            contador = contador - 1
            cont = cont - 1
            Lista.append(dato[0])
            if contador == 0:
                idtema = str(int(dato[0]) + 1)
                Lista.remove(dato[0])
                Lista.append(idtema)
            archivo2 = open(ubi2,"w",encoding = "utf8")
            for a in Lista:
                archivo2.write(a + '\n')
            archivo2.close()
            if cont == 0:
                break
        archivo1.close()
        T = TEMAS(idtema,nombre)
        T.AgregarTema()
    #--------------------------------------------------------------------------------
    @classmethod
    def Eliminar(self,ubi,clave):
        Lista = []
        archivo1 = open(ubi, encoding='utf8')
        for n in archivo1:
            Lista.append(n)
            dato = n.split('|')
            if clave == dato[0]:
                Lista.remove(n)
            archivo2 = open(ubi,"w",encoding = "utf8")
            for g in Lista:
                archivo2.write(g)
            archivo2.close()
        archivo1.close()
    #---------------------------------------------------------------------------------------------------
    @classmethod
    def EditarTema(self,ubi,idt):
        Lista = []
        archivo1 = open(ubi, encoding='utf8')
        for n in archivo1:
            Lista.append(n)
            dato = n.split('|')
            if idt == dato[0]:
                Nombre = input('Nombre nuevo: ')
                T = idt + '|' + Nombre + '\n'
                Lista.remove(n)
                Lista.append(T)
            archivos2 = open(ubi,"w",encoding = "utf8")                
            for x in Lista:
                archivos2.write(x)       
            archivos2.close()
        archivo1.close()
    #----------------------------------------------------
    @classmethod
    def ConsultarTodo(self,ubi):
        archivo = open(ubi, encoding='utf8')
        print(archivo.read())
        archivo.close()
    #-----------------------------------------------------
    @classmethod
    def ConsultaEspecifica(self,ubi,clave):
        archivo = open(ubi, encoding='utf8')
        Lista = []
        for n in archivo:
            Lista.append(n)
            dato = n.split('|')
            if clave == dato[0]:
                print(n)
        archivo.close()
    #-------------------------------------------------------------------------------------------------------------
    @staticmethod
    def Opciones(Opcion):
        if Opcion == 1:
            contador = 3
            ubicacion = './archivos/Temas.txt'
            ubicacion2 = './archivos/Numeros.txt'
            TEMAS.Agregar(ubicacion,ubicacion2,contador)

        elif Opcion == 2:
            ubicacion = './archivos/Temas.txt'
            idt = input('¿Cuál es la clave del video?\n')
            TEMAS.Eliminar(ubicacion,idt)

        elif Opcion == 3:
            idt = input('¿Cual es la clave del video que quieres editar?\n')
            ubicacion = './archivos/Temas.txt'
            TEMAS.EditarTema(ubicacion,idt)

        elif Opcion == 4:
            ubicacion = './archivos/Temas.txt'
            TEMAS.ConsultarTodo(ubicacion)

        elif Opcion == 5:
            ubicacion = './archivos/Temas.txt'
            idt = input('¿Cuál es la clave del video?\n')
            TEMAS.ConsultaEspecifica(ubicacion,idt)
    