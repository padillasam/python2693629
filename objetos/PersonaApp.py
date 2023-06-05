from Persona import *
ob1=Persona('Daniela',654321)
print(type(ob1))
print(ob1.getNombre())
ob1.setNombre(100)
print(ob1.getNombre())
print(ob1.__dict__)