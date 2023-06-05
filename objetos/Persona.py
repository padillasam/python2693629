class Persona:
    def __init__(self,nombre,documento):
        #print('Se instancio un objeto')
        self.__nombre=nombre
        self.__documento=documento
        #self.__telefono
        self.__cursos=[]
        
    def setNombre(self,nombre):
        self.__nombre=nombre
        
    def getNombre(self):
        return self.__nombre
    