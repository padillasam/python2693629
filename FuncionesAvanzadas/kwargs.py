def function(**kwargs):
    #print(type(kwargs))
    for key in kwargs.keys():
        print(key)
    for value in kwargs.values():
         print(value)
    for key,value in kwargs.items():
        print(f'{key} : {value}')


function(programa="adso",ficha=2693629,aprendices=16)




# dict={
#     'programa':'adso',
#     'ficha':2693629,
#     'aprendices':16
# }
