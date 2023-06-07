class empleado:

    objetos=0
    def __init__(self,nombre,cargo,salario):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario
        empleado.objetos+=1

    def getnombre(self):
        return self.__nombre
    
    def setnombre(self,nombre):
        self.__nombre=nombre

    def getcargo(self):
        return self.__cargo
    
    def setcargo(self,cargo):
        self.__cargo=cargo

    def getsalario(self):
        return self.__salario
    
    def setsalario(self,salario):
        self.__salario=salario

    def calcularHora(self):
        horastrabajo=8
        diassemana=5
        diasmes=20
        salariohora=self.salario /(horastrabajo * diassemana * diasmes)
        return self.__salariohora
    
    
