# def suma(num1,num2):
#     return num1+num2
#     #print(num1+num2)

def suma(*args):
    print(type(args))

def mayor(*args):
    m=0
    for i in args:
        if i>m:
            m=i
    return m

print(mayor(10,23,21,100,1000,1,2,3))

#suma(10,23,21)
#suma('hola',122,[],{})

