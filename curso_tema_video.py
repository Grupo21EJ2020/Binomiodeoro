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

#primero = CursoTemaVideo("10", "500", "35")
#primero.AgregarCursoTemaVideo()

#v = CursoTemaVideo
#v.ConsultarCursoTemaVideo()


