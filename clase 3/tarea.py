# En Python hay muchas maneras de guardar información, una de esas es las listas. La clase de hoy vamos a trabajar con cómo manejar distintos tipos de datos y cómo hacer loops con Python.

# **Actividad 1:**

# **Consigna 1**


# Ahora vamos a aprender a manejar información en la computadora. Para eso vamos a usar *listas*. Busquen información sobre listas en python para entender un poco qué son.

# Un link para empezar es este: https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/python-list/ .

# **Consigna 2**

# En la siguiente terminal hay ejemplos de una base de datos de cinco personas hecha a partir de listas. Observen cómo funciona y luego les proponemos unos pequeños desafíos.


nombres=['Juan','Maria','Juan','Laura','Ana']
edades=[45,18,60,26,32]
mascotas=[2,1,0,2,1]
tiempo_de_viaje=[15,10,18,9,65]

print(nombres)
print(nombres[0])

# **Consigna 3:**

# La información está guardada de forma tal que significa que Juan tiene 45 años, 2 mascotas y tarda 15 minutos en llegar al trabajo.

# a) ¿Cómo serían las respuestas de María?

# b) Entonces... ¿Con qué criterio está ordenada la información de las cuatro listas?

# c) Observen los print de la terminal anterior. ¿Qué es lo que hace el comando  "[0]" al lado de nombres? ¿Cómo harían para que en vez de "Juan" esa línea devuelva "Ana"?

# d) Ahora, vamos a generar una pequeña base de datos, haciendo una lista de listas, como indica el link de la consigna anterior. Observen qué sucede.


# a) 18 años, 1 mascota y tarda 10 minutos en llegar.

# b) Las posiciones de las listas coinciden entre sí.

# c) El comando [0] devuelve la primer posición de la lista. Para que devuelva Ana debería usar [4]



base_de_datos=[nombres,edades,mascotas,tiempo_de_viaje]

base_de_datos

base_de_datos[1][1]

# Ahora, vamos a mirar los datos de Juan de nuestra base de datos.

nombre=base_de_datos[0][1]
edad=base_de_datos[1][0]
mascota=base_de_datos[2][3]
tiempo=base_de_datos[3][0]

print(f"{nombre} tiene {edad} años y {mascota} mascotas, y tiene {tiempo} minutos de viaje.")

# a)Interpreten cómo funciona el código anterior, entendiendo de dónde saca y como está indexada la información para hacer el print. Hagan que aparezca lo mismo para Laura en la siguiente terminal.

# b)¿Qué pasa si ponen un corchete en vez de dos? O sea, si ponen nombre[2]

# a) El código funciona de la siguiente manera: al introducir base_de_datos[0,1,2,3] estamos recorriendo las distintas listas que se encuentran dentro del array base_de_datos, por ejemplo, el 0 es nombres, el 1 es edades, el 2 mascotas y el 3 tiempo de viaje. Una vez hayamos decidido que lista recorrer vamos a agregarle la respuesta deseada dentro de esa lista, por ejemplo, si quiero devolver la edad de María debería hacer lo siguiente: base_de_datos[1][1] porque edades está en el [1] y 18 (que es la edad de María) está en el [1].

# b) Al ser nombre una variable designada con el valor 'María' cuando nosotros le pedimos que devuelva la posición [2] le estamos diciendo que devuelva lo que sea que esté ubicado en esa posición. En este caso en la posición [2] se encuentra la 'r' de 'María'.


# Ahora queremos agregar la información de Camila a la lista. Ella tiene 34 años, 10 minutos de viaje y 0 mascotas. Busquen en internet cómo agregarle elementos a una lista y agreguen a Camila.

base_de_datos[0].append('Camila')
base_de_datos[1].append(34)
base_de_datos[2].append(0)
base_de_datos[3].append(10)

print(base_de_datos)

# Laura se arrepintió y no quiere estar en la base de datos. Busquen en internet cómo sacarle información a una lista y saquen la de Laura (su nombre, edad y mascotas)

nombres.pop(3)
edades.pop(3)
mascotas.pop(3)
tiempo_de_viaje.pop(3)
print(base_de_datos)


# **Tarea**

# **Ejercicio 1**

# Entren a la página de precios justos y miren el stock en algún supermercado. Puede ser Coto. Elijan cinco productos y hagan las siguientes listas

# 1) Los nombres de los productos que eligieron

# 2) Los precios que debería tener según precios justos

# 3) Los precios en el súper que eligieron

# Cuando hayan hecho las listas, hagan un código que para todos los elementos diga si el precio en el supermercado respeta los "precios justos" o no




nombres_productos = ['Mate cocido Saquitos Nobleza Gaucha', 'Galletita Clásica Express Terrabusi', 'Aquarius Naranja 1,5Lt', 'Cepillos Dentales ORAL-B Sensitive', 'Leche Parcialmente Descremada Larga Vida 1% La Martona 1 Ltr']
precios_coto = [870, 323, 294, 1075, 383]
precios_justos = [901, 323, 319, 1075, 397]

supermercado_coto = [precios_coto]
precios_justos_lista = [precios_justos]

count = 0
while count >= 0 or count == 4:
  for x in supermercado_coto:
    for y in precios_justos_lista:
      if x[count] == y[count]:
        print(f'El precio de {nombres_productos[count]} es justo')
        count += 1

      elif x[count] != y[count]:
        print(f'El precio de {nombres_productos[count]} no es justo')
        count += 1
  if count == 4:
    break
