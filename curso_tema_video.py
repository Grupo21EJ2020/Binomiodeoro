class CursoTemaVideo:
    def __init__ (self,idCTV,idCT,idVideo):
        self.idCTV, self.idCT, self.__idVideo = idCTV, idCT, idVideo
    @property
    def idCTV(self):
        return self.__idCTV
    @idCTV.setter
    def idCTV(self, valor):
        self.__idCTV = valor
    @property
    def idCT(self):
        return self.__idCT
    @idCT.setter
    def idCT(self, valor):
        self.__idCT = valor
    @property
    def idVideo(self):
        return self.__idVideo
    @idVideo.setter
    def idVideo(self, valor):
        self.__idVideo = valor
    
    #Agregar-------------------------------------------------------------------------------
    def AgregarCursoTemaVideo(self):
        archivo = open('./archivos/Curso_Tema_Video.txt','a',encoding='utf8')
        archivo.write(self.__idCTV + '|' + self.__idCT + '|' + self.__idVideo +'\n')
        archivo.close()
    
    #Elminar-----------------------------------------------------------------------------
    @classmethod
    def EliminarCursoTemaVideo(self,archivo,clave):
        Numeros = ['0','1','2','3','4','5','6','7','8','9']
        Lista = []
        archivo1 = open(archivo, encoding='utf8')
        for n in archivo1:
            Lista.append(n)
            if clave == n[0] and n[1] not in Numeros:
                if clave == n[0]:
                    Lista.remove(n)
            elif clave == (n[0] + n[1]): 
                Lista.remove(n)
            archivo2 = open(archivo,"w",encoding = "utf8")
            for g in Lista:
                archivo2.write(g)
            archivo2.close()
        archivo1.close()
    
#Modificar-----------------------------------------------------------------------------
    @classmethod
    def ModificarCursoTemaVideo(self,clave):
        Lista = []
        archivo1 = open('./archivos/Curso_Tema_Video.txt', encoding='utf8')
        for n in archivo1:
            Lista.append(n)
            dato = n.split('|')
            if clave == dato[0]:
                IDCTTn, IDVIDn = input("cual es el ID curso tema"), input("cual es el ID del video")
                CTV = clave + '|' + IDCTTn + '|' + IDVIDn + '\n'
                Lista.remove(n)
                Lista.append(CTV)
            archivos2 = open('./archivos/Curso_Tema_Video.txt',"w",encoding = "utf8")                
            for x in Lista:
                archivos2.write(x)       
            archivos2.close()
        archivo1.close()
    
    #Consultar todo----------------------------------------------------------------------
    @classmethod
    def ConsultarCursoTemaVideo(self,ubicacion):
        archivo = open(ubicacion,"r",encoding="utf8")
        for x in archivo:
            datos = x.split('|')
            print("idCTV:",datos[0])
            print("idCT:",datos[1])
            print("idVideo:",datos[2])
        archivo.close()

    #Consulta especifica---------------------------------------------------------------------
    @classmethod
    def ConsultarEspCursoTemaVideo(self,clave):
        archivo = open('./archivos/Curso_Tema_Video.txt',encoding='utf8')
        for i in archivo.readlines():
            i = list(i)
            if clave == lista[0]:
                print(i)
        archivo.close()

    @staticmethod
    def OpcionCTV(Opcion):
        #agregar
        if Opcion == 1:
            IDCTT, IDVID = input("cual es el ID curso tema"), input("cual es el ID del video")
            contador = 6
            Lista = []
            archivo1 = open('./archivos/Numeros.txt', encoding='utf8')
            cont = 6
            for n in archivo1:
                dato = n.split('\n')
                contador = contador - 1
                cont = cont - 1
                Lista.append(dato[0])
                if contador == 0:
                    IDCTVV = str(int(dato[0]) + 1)
                    Lista.remove(dato[0])
                    Lista.append(IDCTVV)
                archivo2 = open('./archivos/Numeros.txt',"w",encoding = "utf8")
                for a in Lista:
                    archivo2.write(a + '\n')
                archivo2.close()
                if cont == 0:
                    break
            archivo1.close()
            ids = CursoTemaVideo(IDCTVV, IDCTT, IDVID)
            ids.AgregarCursoTemaVideo()
        
        #eliminar
        if Opcion == 2:
            archivo = './archivos/Curso_Tema_Video.txt'
            clave = input("¿Cual es la clave del video?\n")
            CursoTemaVideo.EliminarCursoTemaVideo(archivo,clave)
        
        #modificar
        if Opcion == 3:
            clave = int(input('¿Cual es la clave del tema del video que quieres editar?\n'))
            CursoTemaVideo.ModificarCursoTemaVideo(clave)
        
        #consultarTodo
        if Opcion == 4:
            archivo = './archivos/Curso_Tema_Video.txt'
            CursoTemaVideo.ConsultarCursoTemaVideo(archivo)
        
        #consultarEsp
        if Opcion == 5:
            clave = int(input('¿Cual es la clave del tema del video que quieres imprimir?\n'))
            CursoTemaVideo.ConsultarEspCursoTemaVideo(clave)

n = int(input("dame"))
CursoTemaVideo.OpcionCTV(n)
