#Ahora modemos concatener cadenas y numeros por medio del f- String el cual funciona poniendo el numero 
# en llaves {} y una f antes de estas llaves como lo siguiente: 
age = 45
texto = f"yo tengo {age} años "
print(texto)
#ahora veremos Un marcador el cual puede contener variables, operaciones, funciones y modificadores para formatear el valor.
#Se incluye un modificador agregando dos puntos :seguidos de 
# un tipo de formato legal, como .2fque significa un número de punto fijo con 2 decimales:
loco = 59
texto = f"The price is {price:.2f} dollars"
print(loco)
txt = f"The price is {20 / 59} dollars" #Aqui desarrollamos una division gracias al marcador de posicion 
print(txt)