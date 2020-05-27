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
    
    def AgregarTema(self):
        archivo = open('./archivos/Temas.txt','a',encoding='utf8')
        archivo.write(self.__idtema + '|' + self.__nombre  + '\n')
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
#--------------------------------------------------
   @classmethod
    def Eliminar(self,ubi,clave):
        Lista = []
        archivo1 = open(ubi, encoding='utf8')
        for n in archivo1:
            Lista.append(n)
            if clave == n[0]:
                Lista.remove(n)
            archivo2 = open(ubi,"w",encoding = "utf8")
            for g in Lista:
                archivo2.write(g)
            archivo2.close()
        archivo1.close()

#--------------------------------------------------
   @classmethod
    def EditarTema(self,ubi,idt):
        Lista = []
        Numeros = ['0','1','2','3','4','5','6','7','8','9']
        archivo1 = open(ubi, encoding='utf8')
        for n in archivo1:
            Lista.append(n)
            if idt == n[0] and n[1] not in Numeros:
                if idt == n[0]:
                    Nombre = input('Nombre nuevo: ')
                    T = idt + '|' + Nombre + '\n'
                    Lista.remove(n)
                    Lista.append(T)
            elif idt == (n[0] + n[1]):
                Nombre = input('Nombre nuevo: ')
                T = idt + '|' + Nombre + '\n'
                Lista.remove(n)
                Lista.append(T)
            archivos2 = open(ubi,"w",encoding = "utf8")                
            for x in Lista:
                archivos2.write(x)       
            archivos2.close()
        archivo1.close()
#---------------------------------------------------
    @classmethod
    def ConsultarTodo(self,ubi):
        archivo = open(ubi, encoding='utf8')
        print(archivo.read())
        archivo.close()

#----------------------------------------------------
    @classmethod
    def ConsultaEspecifica(self,ubi,clave):
        archivo = open(ubi, encoding='utf8')
        Lista = []
        Numeros = ['0','1','2','3','4','5','6','7','8','9']
        for n in archivo:
            Lista.append(n)
            if clave == n[0] and n[1] not in Numeros:
                if clave == n[0]:
                    print(n)
            elif len(clave) == len(n[0] + n[1]):
                if clave == (n[0] + n[1]):
                    print(n)
        archivo.close()


    