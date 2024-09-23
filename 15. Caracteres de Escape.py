#Ahora utilizaremos el caracter de escape, este caracter funcion para añadir valores a una cadena cuando 
#normalmente no se puede hacer esto. 
texto = "existe una serie \"Los 100\" y Marvel" #Permite que la cadena "los 100"tenga comillas dobles y se vea refleado en la pantalla 
print(texto)

texto2 = "esto va a incluir una \\(barra invertida)" #Con dos barras invertidas muestra por consola una barra invertida 
print(texto2)
#Para hacer un salto de linea tambien tenemos un caracter de escape 
texto3 = "Discretas\nes lo mejor " #con \n hacemos que se salte la linea y se vea mas organizado
print(texto3)
#con \t lo que hacemos es separa las palabras, como si crearamos un espacio 
texto4 = "hola\tsoy\tjuan"
print(texto4)
#y el contrario de separa con espacio es \b, que hace que une las palabras 
texto5 = "holaaaaa      \bamigos"
print(texto5)
#una barra invertida seguida de tres numeros enteros dara como resultado un valor octal. 
texto6 = "\110\145\154\154\157"
print(texto6) #Aqui imprimimos una palabra que es hola 
#una barra invertida seguida de x y un numero hexadecimal representa un valor hexadecimal 
texto7 = "\x48\x65\x6c\x6c\x6f"
print(texto7) #Aqui imprimimos una palabra que es hola  que esta en hexadecimal