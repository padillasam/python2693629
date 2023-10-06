def base(x):
    def suma(y):
        return x+y
        #print(x+y)
    def resta(y):
        return x-y
    return [suma,resta]

#print(base(1))
usoFuncionRetornada=base(10)
print(usoFuncionRetornada[1](20))





# def prueba():
#     pass

# print(prueba)

# class Prueba:
#     pass

# x=Prueba()
# print(x)