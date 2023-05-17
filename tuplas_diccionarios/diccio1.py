a,b,c=[],(),{}
diccionario={}
print(type(a))
print(type(b))
print(type(c))

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

d1={1:50,'1':200,3:300,0:'100'}
print(d1)

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

print(f'gato en frances= {dictionary["gato"]}')

dictionary = {"gato": "chat", 
              "perro": "chien", 
              "caballo": "cheval"}

words = ['gato', 'león', 'caballo']
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")
        
print(f'las claves de dictionary: {dictionary.keys()}')

for x in dictionary.keys():
    print('clave',x,'valor',dictionary[x])
    
for x in dictionary.items():
    print(x)
    print('clave=',x[0])
    print('valor=',x[1])
    
dictionary["gato"]='minou'
print(dictionary)
dictionary['cisne'] = 'cygne'
dictionary.update({"pato": "canard"})
print(dictionary)

del dictionary['perro']
print(dictionary)
dictionary.popitem()
print(dictionary) 