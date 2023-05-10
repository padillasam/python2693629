import random
tam=random.randint(5,20)
#tam=10#
lista=[random.randrange(100) for i in range(tam)]
rebanada1=lista[len(lista)//2:-1]
rebanada2=lista[len(lista)//2:]
print(lista)
print(rebanada1)
print(rebanada2)