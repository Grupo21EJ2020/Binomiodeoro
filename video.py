class Video:
    def __init__ (self,idVideo,nombre,url,fechapublicacion):
        self.__idVideo, self.__nombre, self.__url, self.__fechapublicacion = idVideo, nombre, url, fechapublicacion 
    @property
    def idVideo(self):
        return self.__idVideo
    @idVideo.setter
    def idVideo(self,valor):
        self.__idVideo = valor
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor
    @property
    def url(self):
        return self.__url
    @url.setter
    def url(self,valor):
        self.__url = valor
    @property
    def fechapublicacion(self):
        return self.__fechapublicacion
    @fechapublicacion.setter
    def fechapublicacion(self,valor):
        self.__fechapublicacion = valor   
    #-------------------------------------------------------------------------------------------
    def AgregarVideo(self):
        archivo = open('./archivos/videos.txt','a',encoding='utf8')
        archivo.write(self.__idVideo + '|' + self.__nombre + '|' + self.__url + '|' + self.__fechapublicacion + '\n')
        archivo.close()
    #--------------------------------------------------------------------------------
    @classmethod
    def Eliminar(self,archivo,clave):
        Lista = []
        archivo1 = open(archivo, encoding='utf8')
        for n in archivo1:
            Lista.append(n)
            if clave == n[0]:
                Lista.remove(n)
            archivo2 = open(archivo,"w",encoding = "utf8")
            for g in Lista:
                archivo2.write(g)
            archivo2.close()
        archivo1.close()
    #---------------------------------------------------------------------------------------------------
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
    #----------------------------------------------    
    @classmethod
    def ConsultarTodo(self,archivo):
        archivo1 = open(archivo, encoding='utf8')
        print(archivo1.read())
        archivo1.close()
    #------------------------------------------------
    @classmethod
    def EditarVideo(self,archivo,clave):
        Lista = []
        Lista2 = []
        archivo1 = open(archivo,"r",encoding ='utf8')
        store = archivo1.readlines()
        for n in store:
            n = n.replace("\n", "")
            Lista.append(n)
        for y in Lista:
            datos = y.split("|")
            if datos[0] == clave:
                TituloN, UrlN, FechaN = input('Nombre nuevo: '), input('Url nueva: '), input('Fecha Nueva: ')
                V = clave + '|' + TituloN + '|' + UrlN + '|' + FechaN + '\n'
                Lista2.append(V)
            else:
                datos = (y + "\n")
                Lista2.append(datos)
        archivos2 = open(archivo,"w",encoding = "utf8")                
        for x in Lista2:
            Nuevo = x
            archivos2.write(Nuevo)       
        archivos2.close()
        
        archivo1.close()
    #--------------------------------------------------------------------------------------------------------
    @classmethod
    def Agregar(self,archivo,archivo2,contador):
        nombre, url, fechapublicacion = input('Nombre: '), input('Url: '), input('Fecha de publicación: ')
        Lista = []
        archivo1 = open(archivo2, encoding='utf8')
        for n in archivo1:
            dato = n.split('\n')
            contador = contador - 1
            Lista.append(dato[0])
            if contador == 0:
                idVideo = str(int(dato[0]) + 1)
                Lista.remove(dato[0])
                Lista.append(idVideo)
            archivo3 = open(archivo2,"w",encoding = "utf8")
            for a in Lista:
                archivo3.write(a + '\n')
            archivo3.close()
        archivo1.close()
        V = Video(idVideo,nombre,url,fechapublicacion)
        V.AgregarVideo()
    #-------------------------------------------------------------------------------------------------------------
    @staticmethod
    def OpcionDeVideo(Opcion):
        if Opcion == 1:
            contador = 4
            archivo = './archivos/videos.txt'
            archivo2 = 'Numeros.txt'
            Video.Agregar(archivo,archivo2,contador)

        elif Opcion == 2:
            archivo = './archivos/videos.txt'
            clave = input('¿Cuál es la clave del video?\n')
            Video.Eliminar(archivo,clave)

        elif Opcion == 3:
            Clave = input('¿Cual es la clave del video que quieres editar?\n')
            archivo = './archivos/videos.txt'
            Video.EditarVideo(archivo,Clave)

        elif Opcion == 4:
            archivo = './archivos/videos.txt'
            Video.ConsultarTodo(archivo)

        elif Opcion == 5:
            archivo = './archivos/videos.txt'
            clave = input('¿Cuál es la clave del video?\n')
            Video.ConsultaEspecifica(archivo,clave)