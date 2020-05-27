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
    
    def AgregarCursoTemaVideo(self):
        archivo = open('./archivos/Curso_Tema_Video.txt','a',encoding='utf8')
        archivo.write(self.__idCTV + '|' + self.__idCT + '|' + self.__idVideo +'\n')
        archivo.close()
    
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
    
    @classmethod
    def ModificarCursoTemaVideo(self):



        pass    

    def ConsultarCursoTemaVideo():
        archivo = open('./archivos/Curso_Tema_Video.txt',"r",encoding="utf8")
        for x in archivo:
            datos = x.split('|')
            print("idCTV:",datos[0])
            print("idCT:",datos[1])
            print("idVideo:",datos[2])
        archivo.close()


    def OpcionCTV(Opcion):
        if Opcion == 1:
            #contador = 4
            #archivo = './archivos/Curso_Tema_Video.txt'
            IDCTVV, IDCTT, IDVID = input("cual es el ID curso tema video"), input("cual es el ID curso tema"), input("cual es el ID del video")
            ids = CursoTemaVideo(IDCTVV, IDCTT, IDVID)
            ids.AgregarCursoTemaVideo()
        if Opcion == 2:
            archivo = './archivos/Curso_Tema_Video.txt'
            clave = input("¿Cual es la clave del video?\n")
            CursoTemaVideo.EliminarCursoTemaVideo(archivo,clave)
        if Opcion == 3:
            #modificar
            pass
        if Opcion == 4:
            archivo = './archivos/Curso_Tema_Video.txt'
            t = CursoTemaVideo
            t.ConsultarCursoTemaVideo()
        if Opcion == 5:
            pass



N = int(input("L\n"))
CursoTemaVideo.OpcionCTV(N)

    


#primero = CursoTemaVideo("15", "500", "35")
#primero.AgregarCursoTemaVideo()
        
#archivo = './archivos/Curso_Tema_Video.txt'
#clave = input("¿Cual es la clave del video?\n")
#CursoTemaVideo.EliminarCursoTemaVideo(archivo,clave)


#primero = CursoTemaVideo("10")
#primero.AgregarCursoTemaVideo()

#v = CursoTemaVideo
#v.ConsultarCursoTemaVideo()


