class Prueba:
    
    contador=0
    
    def __init__(self,var=1):
        self.__var=var
    
    def otraVariable(self,var2):
        self.__var2=var2

print(Prueba.__dict__)