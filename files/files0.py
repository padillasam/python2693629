import os
lista=['azul','rojo','verde','amarillo']
contenido=''
try:
    stream=open("files\\prueba.txt","r+t",encoding="utf-8")
    print('leyendo')    
    #print(type(contenido))
    #print(len(contenido))        
    for color in lista:
        stream.write(color+'\n')
    #stream.write("...................")
    contenido=stream.read()
    print(contenido)
    stream.close()
except IOError as e:
    print('Error con el archivo')
    print(e.errno)