class Curso:
    def __init__ (self, id_curso, descripcion, id_empleado):
        self.__id_curso = id_curso
        self.__descripcion = descripcion 
        self.__id_empleado = id_empleado
 
        
    #Privatizacion de atributos de la clase Curso
    @property
    def id_curso(self):
        return self.__id_empleado
    
    @property
    def descripcion(self):
        return self.__descripcion
    
    @property
    def id_empleado(self):
        return self.__id_empleado
    
    #Se crean los setter de la clase Curso
    @id_curso.setter
    def id_curso(self,valor):
        self.__id_curso = valor
    
    @descripcion.setter
    def descripcion(self, valor):
        self.__descripcion = valor

    @id_empleado.setter
    def id_empleado(self, valor):
        self.__id_empleado = valor

   #Metodo Agregar
    def agregar_curso(self):
        archivo = open("./archivos/Cursos.txt","a",encoding='utf8')
        archivo.write(f"{self.__id_curso:<5} | {self.__descripcion:<20} | {self.__id_empleado:<5}| \n")
        archivo.close()
    
    #Metodo estatico para pedir opciones
    @staticmethod
    def clave():
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("Introduce la clave del curso: "))
                correcto=True
            except ValueError:
                print('Error, Solo se aceptan numeros enteros, intentalo nuevamente')
        return num

    @staticmethod
    def empleado():
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("Introduce la clave del instructor del curso: "))
                correcto=True
            except ValueError:
                print('Error, Solo se aceptan numeros enteros, intentalo nuevamente')
        return num

    @staticmethod
    def nombre_curso():
        nombre = input("Introduce el nombre del curso: ")
        return nombre
    

   #Metodo consultar todo
    @classmethod
    def consultar_todo(self, fichero):
        archivo = open(fichero,encoding='utf8')
        print(archivo.read())
        archivo.close()

    #Metodo consulta especifica
    @classmethod
    def consultar_curso(self,codigo):
        archivo = open("./archivos/Cursos.txt",encoding='utf8')
        for linea in archivo.readlines():
            lista = list(linea)
            if codigo == lista[0]:
                print(linea)
        archivo.close()

    #Metodo de eliminar un curso
    @classmethod
    def eliminar(self,archivo,clave):
        Lista = []
        fichero = open(archivo, encoding='utf8')
        for dato in fichero:
            Lista.append(dato)
            if clave == dato[0]:
                Lista.remove(dato)
            resultado = open(archivo,"w",encoding = "utf8")
            for nuevo in Lista:
                resultado.write(nuevo)
            resultado.close()
        fichero.close()

   #Metodo de actualizar
    @classmethod
    def modificar(self,archivo,clave,nombre,empleado):
        Lista = []
        fichero = open(archivo, encoding='utf8')
        for dato in fichero:
            Lista.append(dato)
            if clave == dato[0]:
                Lista.remove(dato)
                Lista.append(f"{clave:<5} | {nombre:<20} | {empleado:<5}| \n")
            resultado = open(archivo,"w",encoding = "utf8")
            for nuevo in Lista:
                resultado.write(nuevo)
            resultado.close()
        fichero.close()


 
    
    
