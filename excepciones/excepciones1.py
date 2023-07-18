try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
        
except (ZeroDivisionError,ValueError):
    print("No puedes dividir entre cero o ingrese numero")
# except ArithmeticError:
#     print('Primero por Arithmetic')
# except ValueError:
#     print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salió mal...")

print("FIN.")



# try:
#     print("alpha"[1/1])
# except ZeroDivisionError:
#     print("cero")
# except IndexError:
#     print("índice")
# except:
#     print("algo")