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
        archivo.write(f"{'ID_Curso_Tema: %s'%self.__idct} | {'ID_Curso: %s'%self.idcurso} | {'ID_Tema: %s'%self.__idtema} \n")
        archivo.close()
       
#Methods inicializadores para el static
    @classmethod
    def agregarI(self, contador):
        print("La clave de la relacion sera la concatenacion de ambas claves.")
        valor2 = input("Introduce el ID del curso: ")
        valor3 = input("Introduce el ID del tema: ")
        valor = valor2 + valor3
        relacion= Curso_Tema(valor, valor2, valor3)
        relacion.agregarct()

    @classmethod
    def borrarI(self, seleccion):
        archivo = open('./archivos/curso_tema.txt', 'r')
        clave = archivo.readlines()
        for i in clave:
            if seleccion in i:
                clave.remove(i)
        archivo = open('./archivos/curso_tema.txt', 'w')
        clave = " ".join(clave)
        archivo.write("%s"%clave)
        archivo.close
        

    @classmethod
    def modificarI(self, valor, valor2, valor3):
        archivo = open('./archivos/curso_tema.txt', 'r')
        clave = archivo.readlines()
    
        for i in clave:
            if valor in i:
                clave.remove(i)
        
        clave = " ".join(clave)
        archivo = open('./archivos/curso_tema.txt', 'w', encoding='utf8')
        valor = valor2 + valor3
        clave = (f"ID_Curso_Tema: {valor} | ID_Curso: {valor2} | ID_Tema: {valor3} \n" + "%s"%clave)
        archivo.write("%s"%clave)
        archivo.close
    
    @classmethod
    def busquedaI(self, valor):
        archivo = open('./archivos/curso_tema.txt', 'r')
        clave = archivo.readlines()
        for i in clave:
            if valor in i:
                return i
        archivo.close

    @staticmethod
    def opcionct(opcion):
        relacion = Curso_Tema("0", "0", "0")
        if opcion == 1:
            contador = 0
            relacion.agregarI(contador)
        elif opcion == 2:
            seleccion = input("Introduce la clave de la relacion Curso_Tema que deseas borrar: ")
            relacion.borrarI(seleccion)
        elif opcion == 3:
            valor = input("Introduce la clave de la relacion Curso_Tema que deseas modificar: ")
            valor2 = input("Introduce el nuevo ID del curso: ")
            valor3 = input("Introduce el nuevo ID del tema: ")
            relacion.modificarI(valor, valor2, valor3)
        elif opcion == 4:
            archivo = open('./archivos/curso_tema.txt', 'r')
            clave = archivo.readlines()
            clave = " ".join(clave)
            print(clave)
        elif opcion == 5:
            valor = input("Coloque la clave de la relacion que busca: ")
            print(relacion.busquedaI(valor))
        else:
            print("Su eleccion fue incorrecta")