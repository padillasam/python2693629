def suma(n1,n2):
    return n1+n2

def resta(n1,n2):
    return n1-n2

def producto(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2

def operacion(funcion,numero1,numero2):
    print(funcion(numero1,numero2))

operacion(suma,10,5)