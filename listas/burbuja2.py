import random
tam=random.randint(5,10)
lista=[random.randrange(100) for i in range(tam)]
print(lista)

for i in range(len(lista)-1):
    if lista[i]<lista[i+1]:
        lista[i],lista[i+1]=lista[i+1],lista[i]

print(lista)
    
#in - not in    

# for i in range(len(lista)):
#     print(lista[i])

for x in lista:
    print(x)

if 10 not in lista:
    print('no esta')
else:
    print('si esta')