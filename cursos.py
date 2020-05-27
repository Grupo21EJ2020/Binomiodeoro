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
    
