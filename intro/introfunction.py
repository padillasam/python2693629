import math
import random


print(math.sqrt(100))
print(math.pow(2,5))
print(2**5)
print(math.sqrt(100))
print(math.pow(27,(1/3)))

num=int(random.random()*100)
print(num)
num1=random.randint(10,20)
print(num1)

def saludo(nombre):
    return f'Hola {nombre}'

var=saludo('Soacha')
print(len(var))
print(var)


saludo('Maria')
saludo('Pedro')
saludo('Ana')