i=1
sum=0
while i<=10:
    print(i)
    sum+=i #sum=sum+i
    i+=1 #i=i+1
print('la suma es:',sum)

i=0
sp,si=0,0
while i<=10:
    print(i)
    if i%2==0:
        sp+=i
    else:
        si+=i
    i+=1
print('la suma de los pares es:',sp)
print('la suma de los impares es:',si)
