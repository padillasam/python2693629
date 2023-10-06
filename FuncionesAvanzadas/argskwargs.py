def funcion(*args,**kwargs):
    for elemento in args:
        print(elemento)
    
    for key,val in kwargs.items():
        print(f'{key} : {val}')

funcion(1,2,3,4, fecha='6-10-2023',hora='7:30 am')

x=100
print(isinstance(x,int))

