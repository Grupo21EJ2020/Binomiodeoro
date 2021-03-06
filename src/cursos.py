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
        archivo.write(f"{self.__id_curso}| {self.__descripcion:<20} | {self.__id_empleado}| \n")
        archivo.close()
    
    #Metodo estatico para pedir opciones
    @staticmethod
    def clave(cadena):
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input(f"{cadena}"))
                correcto=True
            except ValueError:
                print('Error, Solo se aceptan numeros enteros, intentalo nuevamente')
        return num

    @staticmethod
    def empleado(cadena):
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input(f"{cadena}"))
                correcto=True
            except ValueError:
                print('Error, Solo se aceptan numeros enteros, intentalo nuevamente')
        return num

    @staticmethod
    def nombre_curso(cadena):
        nombre = input(f"{cadena}")
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
            info = linea.split('|')
            if codigo == info[0]:
                print(linea)
        archivo.close()

    #Metodo de eliminar un curso
    @classmethod
    def eliminar(self,archivo,clave):
        Lista = []
        fichero = open(archivo, encoding='utf8')
        for dato in fichero:
            Lista.append(dato)
            info = dato.split('|')
            if clave == info[0]:
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
            info = dato.split('|')
            if clave == info[0]:
                Lista.remove(dato)
                Lista.append(f"{clave}| {nombre:<20} | {empleado}| \n")
            resultado = open(archivo,"w",encoding = "utf8")
            for nuevo in Lista:
                resultado.write(nuevo)
            resultado.close()
        fichero.close()
    #Metodo para generar codigos
    @classmethod
    def Agregarid(self,contador):
        nombre, empleado = input('Nombre del curso: '), input('Empleado asigando: ')
        Lista = []
        archivo1 = open('./archivos/Numeros.txt', encoding='utf8')
        cont = 6
        for n in archivo1:
            dato = n.split('\n')
            contador = contador - 1
            cont = cont - 1
            Lista.append(dato[0])
            if contador == 0:
                id_curso = str(int(dato[0]) + 1)
                Lista.remove(dato[0])
                Lista.append(id_curso)
            archivo2 = open('./archivos/Numeros.txt',"w",encoding = "utf8")
            for a in Lista:
                archivo2.write(a + '\n')
            archivo2.close()
            if cont == 0:
                break
        archivo1.close()
        C = Curso(id_curso,nombre,empleado)
        C.agregar_curso()
        
    #Metodo para elegir opciones
    @staticmethod
    def gestion_cursos(Opcion):
        if Opcion == 1:
            contador = 2
            Curso.Agregarid(contador)
        elif Opcion == 2:
            codigo = Curso.clave("Ingresa la clave del registro que vas a eliminar: ")
            clave = str(codigo)
            archivo = "./archivos/Cursos.txt"
            Curso.eliminar(archivo,clave)
            
        elif Opcion == 3:
            fichero = "./archivos/Cursos.txt"
            clave = Curso.clave("Ingresa la clave del registro que vas a actualizar: ")
            nombre = Curso.nombre_curso("Nuevo nombre del curso:")
            empleado = Curso.empleado(f"Nuevo empleado asignado al curso {nombre}:")
            codigo = str(clave)
            Curso.modificar(fichero,codigo, nombre, empleado)
            print("Informacion actualizada con exito")
        elif Opcion == 4:
            fichero = "./archivos/Cursos.txt"
            Curso.consultar_todo(fichero)
        elif Opcion == 5:
            clave = Curso.clave("Clave del curso que desea consultar: ")
            codigo = str(clave)
            Curso.consultar_curso(codigo)



 
    
    
