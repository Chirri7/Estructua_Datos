#Las variables globales pueden utilizarse en cualquier parte del codigo pero las locales, solo en donde esta la funcion
x = "lo mejor"
def futbol():
    x = "lo peor"
    print("El futbol es: "+x)
futbol()
print("El futbol es: "+x)

j = "david"

def myfunc():
  global j
  j = "varela"

myfunc()

print("El nombre es: " + j)