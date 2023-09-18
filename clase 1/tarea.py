# ##1°) Vamos a armar el algoritmo(en papel) y luego el código en el Colab de las compras en la Panadería:

# a) Armar las instrucciones para calcular el precio de venta de: una docena de facturas (cada factura $110)

# y dos kilos de pan a $600 el kilo.

# b) A último momento, vimos una cremona pequeña a $900 y decidimos agregarla al pedido.

# c) En la panadería hay un descuento de $150 ¿cómo podemos incorporarlo a nuestro programita?

# No te olvides de colocar un comentario explicando qué haces en cada paso

#le asigno el precio como valor a cada variable
factura = 110
pan = 600
cremona = 900
descuento = 150

#y hago la cuenta con sus respectivas cantidades, restandole al final el descuento
total = (factura * 12) + (pan * 2) + cremona - descuento

print(total)

# #le asigno el precio como valor a cada variable
# factura = 110
# pan = 600
# cremona = 900
# descuento = 150

# #y hago la cuenta con sus respectivas cantidades, restandole al final el descuento
# total = (factura * 12) + (pan * 2) + cremona - descuento

# print(total)



# 2o)a) Armar un bloque de código que le pregunte al usuario la siguiente información(Es importante que uses como nombre de variables las propuestas):

# ● nombre

# ● apellido

# ● edad

# ● ¿Sabés usar Excel?(excel)

# Opciones: sí/no

# ● ¿Sabes algún lenguaje de programación?¿Cuál?(lenguaje)

# Opciones: ningún, C, C++, Java, JavaScript, Python,R, SQL

# b) Agregá la siguiente línea de código en un bloque de código posterior y ejecutá ambos bloques de código print("El estudiante", nombre, apellido, "de edad", edad, "que", excel, "sabe usar excel y conoce", lenguaje, "lenguaje de programación") ¿Qué sucedió? .......................................................................................................................... .......................................................................................................................... .......................................................................................................................... .......................................................................................................................... ..........................................................................................................................

print('escribe tus datos ')
nombre = input('nombre ')
apellido = input('apellido ')
edad = input('edad ')

opcion_si = ['si', 's', 'y']
opcion_no = ['no', 'n']

excel= input('¿Sabés usar Excel? Si/No ')


lenguajes_opciones = ['c', 'c++', 'java', 'javascript', 'python', 'r', 'sql ']

lenguajes_user = input('¿Sabes algún lenguaje de programación? ¿Cuál?: Ningun, C, C++, Java, Javascript, Python, R, SQL ')

sabe_lenguajes = 'conoce '

if lenguajes_user.lower() in lenguajes_opciones:
  sabe_lenguajes += lenguajes_user.capitalize()
else:
  sabe_lenguajes = 'no conoce ningún lenguaje '

if excel.lower() in opcion_si:
  sabe_excel = 'sabe usar excel'
else:
  sabe_excel = 'no sabe usar excel'

print('El estudiante', nombre.capitalize(), apellido.capitalize(), 'de', edad, 'años, que', sabe_excel, 'y', sabe_lenguajes)