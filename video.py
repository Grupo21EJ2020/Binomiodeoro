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


    def AgregarVideo(self):
        archivo = open('Video.txt','a',encoding='utf8')
        archivo.write(self.__idVideo + '|' + self.__nombre + '|' + self.__url + '|' + self.__fechapublicacion + '\n')
        archivo.close()

    
def Eliminar(archivo,clave):
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

def ConsultaEspecifica(archivo,clave):
    archivo1 = open(archivo, encoding='utf8')
    Lista = []
    for n in archivo1:
        Lista.append(n)
        if clave == n[0]:
            print(n)
    archivo1.close()

def ConsultarTodo(archivo):
    archivo1 = open(archivo, encoding='utf8')
    print(archivo1.read())
    archivo1.close()

def EditarVideo(archivo,clave):
    archivo1 = open(archivo, encoding='utf8')
    Lista = []
    for n in archivo1:
        Lista.append(n)
        if clave == n[0]:
            ClaveN = clave
            Lista.remove(n)
            TituloN, UrlN, FechaN = input('Nombre nuevo: '), input('Url nueva: '), input('Fecha Nueva: ')
            V = ClaveN + '|' + TituloN + '|' + UrlN + '|' + FechaN + '\n'
            Lista.append(V)
        archivo2 = open(archivo,"w",encoding = "utf8")
        for g in Lista:
            archivo2.write(g)
        archivo2.close()
    archivo1.close()    

def Agregar(archivo,contador):
    nombre, url, fechapublicacion = input('Nombre: '), input('Url: '), input('Fecha de publicación: ')
    Lista = []
    archivo1 = open(archivo, encoding='utf8')
    for n in archivo1:
        dato = n.split('\n')
        contador = contador - 1
        Lista.append(dato[0])
        if contador == 0:
            idVideo = str(int(dato[0]) + 1)
            Lista.remove(dato[0])
            Lista.append(idVideo)
        archivo2 = open(archivo,"w",encoding = "utf8")
        for a in Lista:
            archivo2.write(a[0] + '\n')
        archivo2.close()
    archivo1.close()
    V = Video(idVideo,nombre,url,fechapublicacion)
    V.AgregarVideo()

def OpcionDeVideo(Opcion):
    if Opcion == 1:
        contador = 5
        archivo = 'Numeros.txt'
        Agregar(archivo,contador)

    elif Opcion == 2:
        archivo = "Video.txt"
        clave = input('¿Cuál es la clave del video?\n')
        Eliminar(archivo,clave)

    elif Opcion == 3:
        Clave = input('¿Cual es la clave del video que quieres editar?\n')
        archivo = 'Video.txt'
        EditarVideo(archivo,Clave)

    elif Opcion == 4:
        archivo = "Video.txt"
        ConsultarTodo(archivo)

    else:
        archivo = "Video.txt"
        clave = input('¿Cuál es la clave del video?\n')
        ConsultaEspecifica(archivo,clave)

def main():
    while True:
        OpUsuario2 = int(input(" "))
        if OpUsuario2 == 6:
            break
        OpcionDeVideo(OpUsuario2)

main()