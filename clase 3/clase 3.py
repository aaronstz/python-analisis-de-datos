# 1- Si sale el sol no uso paraguas


sol = input('Salió el sol? ')
respuestas_true = ['true', 'True', 't', 'si', 'tengo', 'S', 'T']
respuestas_false = ['false', 'False', 'f', 'no', 'F', 'N']

if sol in respuestas_true:
  print('No uso paraguas')
elif sol in respuestas_false:
  print('Uso paraguas')
else:
  print('Error')

# 2.Si el paquete de chocolinas sale menos de $300, compro dos paquetes y hago una chocotorta, si no compro chocodia y hago una chocotorta

chocolinas = input('Indique el precio de las chocolinas ')

if int(chocolinas) > 300:
  print('Compro chocodia y hago una chocotorta ')
elif int(chocolinas) <= 300:
  print('Compro dos paquetes de chocolinas y hago una chocotorta ')
else:
  print('Error')

# 3- La calefacción de mi casa funciona con termostato. La temperatura óptima de la casa es de 16 a 26ºC. Con lo cual si la temperatura de la casa es menor a ese valor se prende la calefacción y si es mayor se prende el aire acondicionado. Si la temperatura es óptima, no se prende

temp_min = 16


temp_max = 26
temp_actual = input('Indique la temperatura actual ')

if int(temp_actual) > temp_max:
  aire_acondicionado = True
  print('Se prendió el aire acondicionado')
elif int(temp_actual) < temp_min:
  calefaccion = True
  print('Se prendió la calefacción')
else:
  print('La temperatura es óptima')

# 4- Cuando tengo plata o ganas, preparo un asado con amigos

plata = input('Indique True si tiene plata, False si no tiene ')
ganas = input('Indique True si tiene ganas, False si no tiene ')

respuestas_true = ['true', 'True', 't', 'si', 'tengo', 'S', 'T']
respuestas_false = ['false', 'False', 'f', 'no', 'F', 'N']

if plata in respuestas_true:
  tiene_plata = True
elif plata in respuestas_false:
  tiene_plata = False
if ganas in respuestas_true:
  tiene_ganas = True
elif ganas in respuestas_false:
  tiene_ganas = False

if tiene_plata == True or tiene_ganas == True:
  hago_asado = True
  print('Preparo un asado')
else:
  hago_asado = False
  print('No hago un asado')

# Queremos decidir qué medio de transporte usar según la distancia y el tráfico. Si son hasta 15 cuadras, voy caminando. Si son mas de 15 cuadras y hay tráfico, tomo el tren. Si no, me tomo el colectivo.
cuadras = input('Indique la cantidad de cuadras ')
trafico = input('Indique si hay tráfico ')
respuestas_true = ['true', 'True', 't', 'si', 'tengo', 'S', 'T', 's']

if int(cuadras) <= 15:
  print('Voy caminando')
elif int(cuadras) > 15 and trafico in respuestas_true:
  print('Voy en tren')
else:
  print('Voy en colectivo')


# Queremos decidir si comprar un artículo basado en su precio y nuestro presupuesto.

presupuesto = input('Indique su presupuesto ')
articulo = input('Indique el precio del producto ')

if int(presupuesto) > int(articulo):
  print('Compro el producto ')
else:
  print('No compro el producto')

#7.En la argentina, la inflación mes a mes de un 8%, asi que si si este mes está entre 4% y 6% festejo

inflacion = input('Indique el valor de la inflacion ')

if int(inflacion) < 4 or int(inflacion) < 6:
  print('Festejo')
else:
  print('No festejo ')
