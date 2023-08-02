from os import strerror

try:
    character_counter = line_counter = 0
    stream = open('files/prueba.txt', 'rt')
    line = stream.readline()
    while line != '':
        line_counter += 1
        #for char in line:
            #print(char, end='')
            #character_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nCaracteres en el archivo:", character_counter)
    print("Líneas en el archivo:     ", line_counter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))


from os import strerror
try:
    flujo=open('files/prueba.txt','r',encoding='utf-8')
    print(flujo.readline())
    #print(flujo.readline())
except IOError:
    print('errrrrrorrrrr')


flujo=open('files/prueba.txt','r',encoding='utf-8')
lista=flujo.readlines()
print(len(lista))
print(lista)