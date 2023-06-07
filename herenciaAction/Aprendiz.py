from Persona import *
from Curso import *

class Aprendiz(Persona):
    def __init__(self,nombre,documento,formacion,ficha):
        Persona.__init__(self,nombre,documento)
        self.__formacion=formacion
        self.__ficha=ficha
        self.__cursos=[]
    
    def agregarCurso(self,curso):
        self.__cursos.append(curso)
    
    def componerCurso(self):
        nombreCurso=input('Ingrese nombre del curso')
        tipoCurso=input('Ingrese tipo del curso')
        objcurso=Curso(nombreCurso,tipoCurso)
        self.__cursos.append(objcurso)
    
    def verCursos(self):
        return self.__cursos

        