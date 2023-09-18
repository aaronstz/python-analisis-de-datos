# En las imágenes impresas por una impresora de tinta doméstica o industrial, o una imprenta offset, los colores se crean en CMYK (Cyan, Magenta, Yellow y Black), que son los colores de las tintas que tiene la impresora.

# a) Crear un programa que dados dos colores, si esos dos colores son magenta y amarillo, devuelva rojo.

color_1='magenta'

color_2='amarillo'

color_formado='rojo'



# b) Repetí el proceso para la combinación de amarillo y cian, devuelva verde.

color_1='amarillo'

color_2='cian'

color_formado='verde'



color_1 = input('Indique cuál es el primer color ')
color_2 = input('Indique cuál es el segundo color ')
rojo = ['magenta', 'amarillo', 'Magenta', 'Amarillo', 'MAGENTA', 'AMARILLO']
verde = ['amarillo', 'cian', 'Amarillo', 'Cian', 'AMARILLO', 'CIAN']

if color_1 and color_2 in rojo:
  print('El color formado es rojo ')
elif color_1 and color_2 in verde:
  print('El color formado es verde ')
else:
  print('Introduzca un color adecuado ')

# Completar los comentarios indicando qué hace cada parte del código.
# Luego completa el código para obtener azul.
# Finalmente copialo en el colab y fijate cómo funciona


colores=['amarillo', 'magenta', 'cian']

#Completarfgghfhgf
print('Los colores posibles para elegir son', colores)  ## elegir los colores de manera azarosa
color_1=input('Escribí un color en minuscula ') #pide al usuario que elija entre los colores
color_2=input('Escribí un color en minuscula ')
color_formado=''

# vamos a comparar la respuesta del usuario con las opciones que tenemos en nuestra lista
  # si el primer color que eligió el usuario es igual al primer color que se encuentra en la lista (amarillo)
  # y el segundo color que eligió el usuario es igual al segundo color que se encuentra en la lista (magenta)
  # el color es rojo
  # así mismo si el usuario los elije en distinto orden
if (color_1 == colores[0]  and color_2== colores[1]) or (color_1 == colores[1]  and color_2== colores[0]):
 	color_formado='rojo'

  # si el primer color que eligió el usuario es igual al primer color que se encuentra en la lista (amarillo)
  # y el segundo color que eligió el usuario es igual al tercer color que se encuentra en la lista (cian)
  # el color es verde
  # así mismo si el usuario los elije en distinto orden
if (color_1 == colores[0]  and color_2== colores[2]) or (color_1 == colores[2]  and color_2== colores[0]):
 	color_formado='verde'

#Combinar magenta y cian para obtener azul
  # si el primer color que eligió el usuario es igual al segundo color que se encuentra en la lista (magenta)
  # y el segundo color que eligió el usuario es igual al tercer color que se encuentra en la lista (cian)
  # el color es azul
  # así mismo si el usuario los elije en distinto orden
if (color_1 == colores[1] and color_2 == colores[2] or (color_1 == colores[2]) and color_2 == colores[1]):
  color_formado = 'azul'

# imprime el resultado de las combinaciones de colores
print(color_formado)
