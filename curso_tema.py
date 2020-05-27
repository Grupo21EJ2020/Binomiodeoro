class Curso_Tema:
    def __init__(self, idct, idcurso, idtema):
        self.__idct = idct
        self.__idcurso = idcurso
        self.__idtema = idtema
    
    @property
    def idct(self):
        return self.__idct
    @idct.setter
    def idct(self, valor):
        self.__idct = valor
    
    @property
    def idcurso(self):
        return self.__idcurso        
    @idcurso.setter
    def idcurso(self, valor):
        self.__idcurso = valor
    
    @property
    def idtema(self):
        return self.__idtema        
    @idtema.setter
    def idtema(self, valor):
        self.__idcurso = valor

    def __eq__(self, otro):
        return self.__idct == otro.__idct

    def agregarct(self):
        archivo = open('./archivos/curso_tema.txt', 'a', encoding='utf8')
        archivo.write(f"{'ID_Curso_Tema: %s'%self.__idct} {'ID_Curso: %s'%self.idcurso} {'ID_Tema: %s'%self.__idtema} \n")
        archivo.close()
    
    def borrarct(self, valor):
        archivo = open('./archivos/curso_tema.txt', 'r')
        clave = archivo.readlines()

        for i in clave:
            if valor in i:
                clave.remove(i)
        archivo = open('./archivos/curso_tema.txt', 'w')
        clave = " ".join(clave)
        archivo.write("%s"%clave)
        archivo.close

    def modificarct(self, valor, valor2, valor3):
        archivo = open('./archivos/curso_tema.txt', 'r')
        clave = archivo.readlines()
    
        for i in clave:
            if valor in i:
                clave.remove(i)
        
        clave = " ".join(clave)
        archivo = open('./archivos/curso_tema.txt', 'w', encoding='utf8')
        clave = (f"ID_Curso_Tema: {valor}  ID_Curso: {valor2}  ID_Tema: {valor3} \n" + "%s"%clave)
        archivo.write("%s"%clave)
        archivo.close
    


primero = Curso_Tema("10", "500", "35")
segundo = Curso_Tema("15", "400", "40")

primero.agregarct()
segundo.agregarct()

primero.modificarct("10", "400", "600")
segundo.borrarct("15")