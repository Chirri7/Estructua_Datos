#Puede convertir de un tipo a otro con los métodos int(), float()y complex():
x = 8   # int
y = 5.8  # float
z = 9j   # complex
#para convertir a un numero flotante utilizamos la funcion float como a continuacion 
a = float(x)

#para convertir a un numero entero utilizamos la funcion int como a continuacion 
b = int(y)

#para convertir a un numero complejo utilizamos la funcion complex como a continuacion 
c = complex(x)
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
#Tambien podemos crear numeros alzar o random importanto un modulo aleatorio 
import random
#por medio de la funcion print con random.randrange creamos un numero aleatorio poniendo limites. como en el ejemplo de 1 a 9   
print(random.randrange(1, 10))