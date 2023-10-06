def validar(**kwargs):
   
    for key,value in kwargs.items():
        if key=="edad":
            print(isinstance(value,int))
        if key=="peso":
            print(isinstance(value,float))
        if key=="estatura":
            print(isinstance(value,float))
  

#validar(edad=15,peso=60.0, estatura=1.60)
#validar(edad='siete',peso='39', estatura='1.39')
validar(edad='34',peso=60, estatura=1.90)

#print(isinstance(60.0,float))