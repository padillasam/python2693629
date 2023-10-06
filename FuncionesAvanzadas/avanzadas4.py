def base(funcion):
    #print('Inicia la función base')
    def interna(n1,n2):
        #print(funcion(n1,n2))#*
        return funcion(n1,n2)
    #print('Finaliza la función base')
    return interna

def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

var1=base(suma)
var2=base(resta)
#var1(10,15)#*
#var2(15,10)#*
print(var1(10,15))
print(var2(15,10))