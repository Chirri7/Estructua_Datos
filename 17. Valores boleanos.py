#En programación, a menudo es necesario saber si una expresión es Trueo False.
print(10 > 9)
print(10 == 9)
print(10 < 9)
#Cuando se ejecuta una condición en una declaración if, Python devuelve Trueo False:
a = 200
b = 33

if b > a:
  print("b es mayor que a")
else:
  print("b no es mayor que a")
  #La bool()función te permite evaluar cualquier valor y darte Trueo False a cambio,
  x = "pato"
y = 15
print(bool(x))
print(bool(y))
#De hecho, no hay muchos valores que evalúen como False, 
# excepto valores vacíos, como (), [], {}, "", el número 0y el valor None. Y, por supuesto, el valor Falsese evalúa como False.
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#Tambien para las funciones pueden devolver un valor booleano 
def myFunction() :
  return True

if myFunction():
  print("si")
else:
  print("no")