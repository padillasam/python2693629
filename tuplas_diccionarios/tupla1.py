import random

t1=(1,2,3)
t2=()
t3=1,20,300,4
print(t3)
t3=t3+(543,)
print(t3)

#No se llena por comprensión
# tupla=(for x in range(10))
# print(tupla)

print(type(t2))
print(t1)
print(t2)
print(t3)
t4=100,
t5=(100,1,2,3,4)
print(len(t5))
for x in t5:
    print(x)
#t5.append(200)
print(t5)
print('...',t3+t5)
print(t5*2)
print(1000 not in t5)
print(100 in t5)

var=1
t11 = (1, )
t21 = (2, )
t31 = (3, var)
 
t11, t21, t31 = t21, t31, t11
 
print(t11, t21, t31)

tt=(1,'a','cadena')
print(tt)

tam=random.randint(10,20)
t=()
for i in range(tam):
    n=random.randrange(100)
    t=t+(n,)
print(t)
mitad=int(len(t)/2)
print(t[0:mitad])
print(t[mitad:])


