def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("¡Problema Aritmético!")
    return None

bad_fun(0)

print("FIN.")
#----------------------------------------------

def bad_fun(n):
    return 1 / n
    #return None
try:
    bad_fun(0)
except ArithmeticError:
    print("¡Problema Aritmético!")

print('El programa continua')

#---------------------------------------------------

def bad_fun(n):
    try:
        raise ZeroDivisionError
    except ArithmeticError:
        print("¡Problema Aritmético.......!")
    return None

bad_fun(10)

print("FIN.")

#--------------------------
try:
    for i in range(10):        
        raise SyntaxError
except SyntaxError:
    print('Error de escritura')
print('continuacion')
#-----------------------------------
def bad_fun(n):
    try:
        return n / 0
    except:
        print("¡..........Lo hice otra vez!")
        raise
try:
    bad_fun(0)
except ArithmeticError:
    print("¡Ya veo!")

print("FIN.")

