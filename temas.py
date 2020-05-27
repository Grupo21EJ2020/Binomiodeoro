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



    