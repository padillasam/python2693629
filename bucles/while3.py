num=1
cont=0
sum=0
mayor=0
menor=1000000
while num!=0:
    num=int(input('ingrese numero'))
    cont=cont+1 #cont+=1
    sum=sum+num
    if num>mayor:
        mayor=num
    if num<menor and num!=0:
        menor=num

print(f'El usuario ingreso {cont-1} numeros')
print(f'La suma es {sum}')
print(f'El promedio es {sum/(cont-1)} numeros')
print(f'El mayor es {mayor}')
print(f'El menor es {menor}')
#print('El usuario ingreso', cont, 'numeros')

