#Variables




# Ejercicio 1:

# Contestar

# a) Asigná una variable con tu nombre(Recordá que no hace falta usar el input)

# b) ¿Cuál es la diferencia entre asignar y llamar una variable?

# c) ¿Qué pasa si llamas a una variable y no está asignada?

# para asignar una variable se hace lo siguiente:

nombre = 'Aaron'

#se le da nombre a la variable y luego del = se le da valor

nombre #así se llama a la variable
#si intentamos llamar a una variable que no este asignada la consola nos avisará con un error que esta no está definida

#Ejercicio 2: Nombres de variables
# Podemos asignar el nombre que queramos, respetando no usar las palabras reservadas de Python ni espacios, guiones o números al principio.
# ```python

# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']
# ```

# a) ¿Cuáles de la siguiente listas de palabras cuales pueden ser nombres de variables?

# precio1, 1precio, cantidad_, _cantidad, FpWx, lambda, lambda1, 7for.

# b) Probá las variables elegidas asignandole un número real.


#las variables que no se pueden usar son las que empiezan con un número por ejemplo 1precio o 7for

precio1 = 200
lambda1 = 40
_cantidad = 3
cantidad_ = 4



##Listas

# 1) Crea una lista con los siguientes objetos: mouse, teclado, CP, Ram, Monitor.

# #resolución

lista_computadora = ['Mouse', 'Teclado', 'CP', 'Ram', 'Monitor']

# 2) Con un comando averigua el largo de la lista(¿cuantos elementos tiene?)

# #resolución
# len(lista_computadora)

# 3) Con un comando averigua el primer elemento de la lista creada

# #resolucion
# lista_computadora[0]

# 4)Con un comando averigua el ultimo elemento de la lista

# #resolución
# lista_computadora[4]

# 5) Imprimí los primeros 3 elementos de la lista

count = 0

while count < 3:
  print(lista_computadora[count])
  count += 1
  if count > 3:
    break

# 6) El siguiente codigo sirve para cambiar un elemento 0 de la lista: emplealo para cambiar monitor por pantalla.Observen y expliquen como funciona
# ¿Se animan a cambiar otro elemento en la lista?


lista_comida=['pescado','pollo','pasta', 'pure', 'ensalada']

lista_comida[0]='buñuelos'
print(lista_comida)

lista_computadora[4] = 'Pantalla'
print(lista_computadora)

##Extra Listas

# a) ¿Qué sucede cuando sumamos las listas entre sí? -> se concatenan las listas

lista_1=[2,3,7]
lista_2=[1,0,4]
lista_total=lista_1 + lista_2
print(lista_total)


# b) ¿Qué pasa si multiplicamos una lista por un número? (Pueden mirar en el explorador de variables o agregar un print)

lista_ceros=[0]*5
print(lista_ceros)

# Estás multiplicando una lista con un objeto 0 por 5, lo cual devuelve una lista con 5 objetos

#Listas con 3 holas
lista_holas=['hola', 'hola', 'hola']

# c) Indicar de qué son las siguientes listas¿Cómo te diste cuenta?

jugadores=['Riquelme','Maradona','Messi', 'Tevez', 'Palermo','El dibu'] #strings

precio_alquileres=[8000.2, 32095.6,20000] #enteros

lista_palabras=['circo', 'máscara', 'silla', 'teléfono','carpeta'] #strings

# d)Realizar este comando sobre la lista de palabras ¿para qué sirve?

lista_palabras.append('rosa') #agrega un elemento al final de la lista
print(lista_palabras)


# e) ¿Y este comando para qué sirve?


lista_palabras.remove('máscara') #elimina el elemento si lo encuentra en la lista
print(lista_palabras)

#Alternativa condicional y listas

# Ejecicio 3: Vamos al cine
# a) Armar un programa que pregunte la edad al usuario y le diga si puede ver la película o no. Recordá que la película "Argentina 1985" es Apta para Mayores de 13 años.

# b) La entrada al cine sale $1200, armá el código de un programa que pregunte la plata que tiene el cliente e indique si puede sacar la entrada

# c) Opcional:
# Las siguientes listas corresponden a las edades y la plata que tienen 3 personas que van juntas al cine:

edades = [10,15,72]

plata=[1000,1500,700]

# i) ¿Las personas pueden acceder al cine por edad?¿quiénes si y quiénes no?

# ii)¿Y por el importe del cine?

# iii) ¿Te animás a adaptar el código que armaste para el item a y b para que la computadora responda a nuestras preguntas?


edad = input('Introduce tu edad ')
plata = input('Indique cuánto dinero tiene ')

edades = [10, 15, 72]
platas = [1000, 1500, 700]

if int(edad) >= 13 and int(plata) >= 1200 :
  print('Podes ver la película ')
else:
  print('Anda a tu casa nene ')


count = 0

while count < 3:
  if edades[count] > 13 and platas[count] > 1200:
    print(f'La persona de {edades[count]} años y {platas[count]} pesos puede ir al cine ')
    count += 1
  else:
    print(f'La persona de {edades[count]} años y {platas[count]} pesos no puede ir al cine ')
    count += 1
  if count >= 3:
    break

#Ejercicio 4:Listas
# La siguiente lista representa el TOP 50 de las canciones más escuchadas en Spotify en la Argentina
# lista_top_50:


# Fuente: https://open.spotify.com/playlist/37i9dQZEVXbMMy2roB9myp

# i) Hacer un código que imprima los 10 primeros temas de la lista

# ii)Hacer otro código que imprima los 3 primeros y un último que imprima los 3 últimos.

# iii) Redefini el tema 2 de la lista con tu canción favorita.

# iv)Opcional: Te animas a encontrar un tema en la lista("Perfecta") ¿En qué posición esta?


lista_top_10 = ['La morocha', 'Ni Una Ni Dos', 'Columbia', 'CORAZÓN VACÍO', 'GTA', 'LALA', 'Los del Espacio', 'Mentiras', 'OJITOS ROJOS', 'Un Finde']

print('Las 3 primeras canciones son: ', lista_top_10[:3])
print('Las 3 ultimas canciones son: ', lista_top_10[-3:])
lista_top_10[1] = 'TOLKIN YIT'

name = 'LALA'
cancion = lista_top_10.index(name)

if name in lista_top_10:
  print(f'La canción {name} se encuentra en la posición', cancion + 1)
else:
  print('No se encuentra ')