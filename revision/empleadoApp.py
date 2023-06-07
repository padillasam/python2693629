from empleado import *

empleado1 = empleado("Jose", "dearrollador", 1160)

print(empleado1.getnombre())
empleado1.setnombre("Juan")
print(empleado1.getnombre())
#print(empleado1.__dict__)

print(empleado1.getcargo())
empleado1.setcargo("arquitecto")
print(empleado1.getcargo())

print(empleado1.getsalario())
empleado1.setsalario(2000)
print(empleado1.getsalario())
#print(empleado1.calcularHora())
print(empleado1.__dict__)