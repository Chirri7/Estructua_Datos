#Como ya sabemos podemos utilizar comillas simples o dobleas para mostrar una cadena pero tambien podemos utilizar comillas dentro de esas comillas
print("¿quien es el que canta'Johnny'")
print('hola, "Johnny"')
#Tambien a una variable podremos asignar cadenas multilineales utilizando 3 comillas dobles
a = """ Juego entre dos equipos de once jugadores cada uno, cuyo objetivo es hacer entrar en la
portería contraria un balón que no puede ser tocado con las manos ni con los brazos, salvo por e
l portero en su área de meta. balompié, balón."""
print(a)
#Tambien podemos utilizar 3 comillas simples y obtendremos el mismo resultado 
x = '''Juego entre dos equipos de once jugadores cada uno, cuyo objetivo es hacer entrar en la
portería contraria un balón que no puede ser tocado con las manos ni con los brazos, salvo por e
l portero en su área de meta. balompié, balón.'''
print(x)
#Una forma de ver las cadenas son como matrices, por medio de corchetes podremos obtener la letra que este en una cierta posicion 
j = "qwertyuiop"
print( j[3])

#Tambien podremos obtener la longitud de una cuerda mediante una funcion leng(), 
a = """Juego entre dos equipos de once jugadores cada uno, cuyo objetivo es hacer entrar en la
portería contraria un balón que no puede ser tocado con las manos ni con los brazos, salvo por e
l portero en su área de meta. balompié, balón."""
print(len(a))

#Otra funcion es la de verificar si una palabra esta dentro de una variables, para esto podemos utilizar la variables in 
txt = "Hola, estoy en cuarto semestre y estudio sistemas"
print("estudio" in txt)

#tambien podemos utilizar el indicador if para verificar 
txt2 = "El mejor equipo del mundo es el Real Madrid "
if "equipo" in txt2:
  print("si, equipo esta en la variables ")
  
#Podemos marcar si una palabra no esta en una frase por medio del comando not in 
txt = "El mejor equipo del mundo es el Real Madrid "
print("futbol" not in txt)