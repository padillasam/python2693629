def sasonar(funcion):
    def envolvente():
        print('Añadir sal y pimienta')
        print(funcion())
    return envolvente
@sasonar
def freir():
    return "Fritando"

@sasonar
def asar():
    return "Asando"

def hornear():
    return "Horneando"

horneando=sasonar(hornear)

freir()
asar()
horneando()