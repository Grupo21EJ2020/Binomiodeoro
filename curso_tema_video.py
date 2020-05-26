class CursoTemaVideo:
    def __init__ (self,idCT,idCTV,idVideo):
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
    
    


    

        
  