from Usuario import *
from Oferta import *
class Aspirante(Usuario):
    def __init__(self,nombre):
        #super().__init__()
        self.__nombre=nombre
        self.__experiencia
        self.__educacion
        self.__certificados
        self.__contactos
        self.__ofertas=[]
    
    def filtra_la_busqueda(self):
        pass
    def se_postula(self,oferta):
        self.__ofertas.append(oferta)
