from Aprendiz import *
from Curso import *

objeto=Aprendiz("Ana Kurnikova",123456,'ADSO',2693629)
#print(objeto.__dict__)
objcurso=Curso("Programacion Software","tecnico")
objeto.agregarCurso(objcurso)
#print(objeto.__dict__)
objeto.componerCurso()
objeto.componerCurso()
#print(objeto.verCursos())
for cursito in objeto.verCursos():
    print(cursito.getNombre())


