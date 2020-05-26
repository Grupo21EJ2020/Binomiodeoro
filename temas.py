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
    