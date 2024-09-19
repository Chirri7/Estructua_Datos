#Phyton tiene varias funciones que permiten modificar el valor de las variables 
#la funcion upper() hace que toda la frase este en mayuscula 
a = "yo vivo en colombia "
print(a.upper())
#La funcion lower hace que toda la frase este en minuscula 
x = "YO NO VIVO en barbosa"
print(x.lower())
#La funcion strip () elimina cualquier espacio en blanco al inicio y al final de cada frase
y = " el color verde es mejor que el amarillo "
print(y.strip()) 
#Si nosotros queremos remplazar una cadena por otra cadena lo que hacemoes es utilizar la funcion 
z  = "viva colombia "
print(z.replace("H", "J")) 

f = "hola, mis amigos"
print(f.split(",")) # El split()método divide la cadena en subcadenas si encuentra instancias del separador: