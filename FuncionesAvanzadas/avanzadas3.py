def base(funcion):
    
    def interna():
        print('Inicia la función base')
        funcion()    
        print('Finaliza la función base')
    return interna

def integrada():
    print('Funcion Integrada')

def otraFuncion():
    print('Otra Funcion')

var1=base(integrada)
var2=base(otraFuncion)
var1()
var2()


# def integrada(parametro):
#     print(f'{parametro} de la funcion Integrada')



