import random
tam=random.randint(5,10)
lista=[random.randrange(100) for i in range(tam)]
print(lista)

for i in range(tam-1):
    for j in range(i+1,tam):
        if lista[i]>lista[j]:
            lista[i],lista[j]=lista[j],lista[i]

print(lista)

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