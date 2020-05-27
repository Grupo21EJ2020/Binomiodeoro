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
        archivo = open('./archivos/Temas.txt','w',encoding='utf8')
        archivo.write(self.__idtema + '|' + self.__nombre  + '\n')
        archivo.close()
#--------------------------------------------------
    @classmethod
    def ConsultarTodo(self,archivo):
        archivo1 = open(archivo, encoding='utf8')
        print(archivo1.read())
        archivo1.close()

#--------------------------------------------------
    @classmethod
    def ConsultaEspecifica(self,archivo,clave):
        archivo1 = open(archivo, encoding='utf8')
        Lista = []
        Numeros = ['0','1','2','3','4','5','6','7','8','9']
        for n in archivo1:
            Lista.append(n)
            if clave == n[0] and n[1] not in Numeros:
                if clave == n[0]:
                    print(n)
            elif len(clave) == len(n[0] + n[1]):
                if clave == (n[0] + n[1]):
                    print(n)
        archivo1.close()
#---------------------------------------------------



    