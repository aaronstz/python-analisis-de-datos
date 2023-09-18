#ACTIVIDAD 1

# Indicar el precio de cada producto
precio_arroz = 300
precio_fideos = 400

#Indicar la cantidad de cada producto a comprar
cant_arroz=2
cant_fideos=5

#Calcular el importe de compra
importe_compra= precio_arroz*cant_arroz+precio_fideos*cant_fideos

#Informar el valor del importe
print(importe_compra)# Indicar el precio de cada producto
precio_arroz = 300
precio_fideos = 400

#Indicar la cantidad de cada producto a comprar
cant_arroz=2
cant_fideos=5

#Calcular el importe de compra
importe_compra= precio_arroz*cant_arroz+precio_fideos*cant_fideos

#Informar el valor del importe
print(importe_compra)


# resolución...
# Indicar el precio de cada producto
precio_arroz = 300
precio_fideos = 400
precio_chocolate = 500

#Indicar la cantidad de cada producto a comprar
cant_arroz=2
cant_fideos=5
cant_chocolate=3

#Calcular el importe de compra
importe_compra= precio_arroz*cant_arroz+precio_fideos*cant_fideos+precio_chocolate*cant_chocolate

#Informar el valor del importe
print(importe_compra)


#ACTIVIDAD 2

nombre=input('Escribir nombre ')
procedencia=input('lugar de procedencia ')
edad=input('edad')

#veamos que hizo el algoritmo

print(nombre)
print(procedencia)
print(edad)


#Hacer las modificaciones correspondientes para cumplir con la consigna 2
print(edad)
print(nombre)
print(procedencia)
helado=input('escribir gusto de helado favorito ')



#introducimos valor hora del salario
salario=50

#decide si es mayor a 100
if salario>100:
  print('el salario es mayor a 100 por hora')

else:
  print('el salario es menor a 100 por hora')


#Resolución...
edad=int(input('ingrese su edad '))

if edad >= 18:
    print('la persona es mayor de edad')

else:
    print('la persona es menor de edad')


#ACTIVIDAD 4


# Resolución
luz= 'roja'

if luz == 'roja':
  print('detenerse')

if luz == 'verde':
  print('avanzar')


#Resolución
luz= 'amarilla'

if luz == 'roja':
  print('detenerse')

if luz == 'amarilla':
  print('acelere')

if luz == 'verde':
  print('avance')


#Resolución

luz= 'naranja'

if luz == 'roja':
  print('detenerse')

if luz == 'amarilla':
  print('acelere')

if luz == 'verde':
  print('avance')

if luz == 'naranja':
  print('frene')




#ACTIVIDAD 5

#Resolución
print('Selecciona un número que indique el nombre de tu película favorita')

opcion1 = 'Opción 1: Madagascar'
opcion2 = 'Opción 2: Los Increíbles'
opcion3 = 'Opción 3: Saw'
opcion4 = 'Opción 4: Los Vengadores'

print(opcion1, opcion2, opcion3, opcion4)

opcion1_info = 'Madagascar. 17 de junio de 2005 en cines / 1h 26min / Animación , Aventura...'
opcion2_info = 'Una familia de superhéroes, obligados a vivir como civiles, vuelve a la acción...'
opcion3_info = 'Es una película de terror y Aventura estrenada en 2004 y dirigida por James Wan...'
opcion4_info = 'Cuando un enemigo inesperado surge como una gran amenaza para la seguridad mundial...'

numero = input()

eleccion = 'opcion' + numero

if eleccion == 'opcion1':
  print(opcion1_info)
elif eleccion == 'opcion2':
  print(opcion2_info)
elif eleccion == 'opcion3':
  print(opcion3_info)
elif eleccion == 'opcion4':
  print(opcion4_info)
else:
  print('Selecciona una de las opciones')

