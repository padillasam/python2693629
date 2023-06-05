class Prueba:
        
    contador=0
    
    def __init__(self,var=1):
        Prueba.contador+=1
        self.__var=var
        
    
    def otraVariable(self,var2):
        self.__var2=var2

print(Prueba.contador)


ob1=Prueba(100)
print(ob1.__dict__,ob1.contador)
ob2=Prueba()
ob2.otraVariable(22)
print(ob2.__dict__,ob2.contador)
ob3=Prueba()
ob3.otraVariable(333)
ob3.tercerVariable=1500
print(ob3.__dict__,ob3.contador)

print(Prueba.contador)