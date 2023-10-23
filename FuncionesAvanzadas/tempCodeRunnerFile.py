def base(funcion):
    
    def interna(*args,**kwargs):
        print('Inicia la función base')
        print(funcion(*args,*kwargs))#*        
        #return funcion(n1,n2)
        #funcion(n1,n2)
        print('Finaliza la función base')
    return interna

def suma2(num1,num2):
    return num1+num2
@base
def misuma(*args,**kwargs):
    s=0
    for x in args:
        s+=x
    return s

misuma(1,2,10,20)