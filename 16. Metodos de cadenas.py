#Ahora miremos algunos metodos que phyton permiten para programar. 
#1.capitalize() = lo que hace es volver la primera letra de una cadena mayuscula
texto1 = "hola mundo "
x = texto1.capitalize()
print(x)
#2. Casefold()= lo que hace es que convierte toda una cadena en letras minusculas
texto2 = "hola mundo "
x = texto2.casefold()
print(x)
#3. El center()método alineará al centro la cadena, y podremos ponerle los otros espacios de relleno 
texto3 = "carro"
x = texto3.center(10) #La palabra carro va a estar a una distancia de 10 en el centro
print(x)
#4.count()=  Devuelve el numero de veces que aparece una palabra en una cadena 
texto4 = "Los carros son rapidos, pero los carros son costosos"
x = texto4.count("carros")
print(x)
#5. endswith()= método devuelve True si la cadena termina con el valor especificado, de lo contrario, False.
texto5 = "Los carros son rapidos, pero los carros son costosos."
x = texto5.count(".")#Aqui comprobamos si la cadena termina con un punto "."
print(x)
#El expandtabs()método establece el tamaño de la tabulación en la cantidad especificada de espacios en blanco.
texto6 = "H\te\tl\tl\to"
x =  texto6.expandtabs(2)
print(x)
#El find()método encuentra la primera aparición del valor especificado.
texto7 = "Hello, welcome to my world."
x = texto7.find("welcome")
print(x)
#El format()método formatea los valores especificados y los inserta dentro del marcador de posición de la cadena.
texto8 = "un carro de juguete por solo  {price:.2f} dolares!"
print(texto8.format(price = 49))
#El index()método encuentra la primera aparición del valor especificado.
texto9 = "Hello, welcome to my world."
x = texto9.index("welcome")
print(x)
#El isalnum()método devuelve Verdadero si todos los caracteres son 
# alfanuméricos, es decir, letras del alfabeto (az) y números (0-9).
texto10 = "Company12"
x = texto10.isalnum()
print(x)