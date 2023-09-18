# ##Lista

# comidas=['papas','raviol','arroz','milanesa']

# ## Actualizar una lista

# Probar los siguientes comandos y discutir qué hacen.

# ```
# comidas[2] = 'fideos'
# print(comidas)
# ```




# **Consigna 1**

# El siguiente código sirve para que, dado un vector de números, la computadora imprima en la pantalla esos números. Miren cómo funciona y resuelvan las consignas a continuación. Observen estos códigos.

edad=[2,3,4,9,20]

for elemento in edad:
 print(elemento + 1)

comidas=['papas','fideos','arroz','milanesa']

for i in comidas:
 print(len(i))

# 1) Modificar el primer código para que se muestren los números de la lista edad, más uno.

# 2) Modificar el segundo código para ver cuántas letras tiene cada una de las palabras de la lista comida. (Pista: Así cómo con len() podemos saber el largo de una lista, ¿podremos saber el de una palabra?)

# Ahora queremos usar la función range, miren cómo es

range(0,10)



for i in range(5,21):
  print(i)

# 1) Modifiquen el codigo anterior para que muestre los números del 5 al 20.

# 2) Entonces... ¿para qué sirve range? -> para saber la cantidad de elementos que hay entre los parámetros.

# Acá hay un código que combina range y for, miren como funciona y resuelvan las siguientes consignas

#solucion

numeros=[42,6,3,7,8,0,8]
N=len(numeros) #len me dice cuántos elementos hay en "numeros"

for i in range(N): #para i en el rango de N, o sea, varia entre 0 y N
  print(numeros[i])



print(numeros[2])
print(numeros[3])
print(numeros[2] + 1)
print(numeros[3] + 1)
print(numeros[4] + 1)
print(numeros[5] + 1)

# 1) Las palabras *for* y *range* están escritas en inglés ¿qué significan?

# 2) Escriban en castellano, de forma coloquial, la órden que está dando el for

# 3) Abran el colab de la clase anterior y miren la estructura del "if" (condicional). En grupos de tres, armen una tabla comparativa entre el if y el for, donde reflejen las semejanzas y diferencias de las estructuras.

# 4) Modifiquen el código anterior para que en vez de escribir números del vector, escriba el número *siguiente*. La respuesta debería ser 3 7 4 8 9 1


# for significa para y range significa rango
# en este caso el for está diciendo que para el índice en el rango de la variable N que es la cantidad de numeros
# realice una impresión del numero en el índice
# o sea, entre 0(i) y 7(N/rango) imprime el número del indice[0] y avanza

# IF:

# recibe condiciones.

# se frena cuando no se cumplen las condiciones

# FOR:

# es un bucle que recibe parámetros

# se frena cuando se termina de recorrer esos parámetros

# ##Ciclos for
# 1) Digamos 3 veces hola. Y 100 veces

# 2) Contemos del 1 al 10

# 3) Imprimamos los elementos de una lista

for i in range(3):
  print('Hola')

for e in range(1, 11):
  print(e)

lista = ['Azucar', 'Fideos', 'Piedritas', 'Tomates']

for y in range(len(lista)):
  print(lista[y])

# **Actividad 2**


# Ahora, teniendo las estructuras de *for*, discutan cómo podrían implementarlas (puede ser usando una o la otra) para imprimir en la pantalla los nombres, lo que deberíamos ver es

# Juan

# María

# Juan

# Laura

# Ana


# Ahora, aprovechando los códigos anteriores, hagan uno que pueda juntar la información diciendo "Pirulo tiene 20 años y 3 mascotas" para todos los nombres de la lista

nombres=["Juan","Maria", "Juan","Laura","Ana"]
edades=[45,18,60,26,32]
mascotas=[2,1,0,2,1]
N=len(nombres)
i=0

for i in range(N):
  print(f"{nombres[i]} tiene {edades[i]} años y {mascotas[i]} mascotas")
  i=i+1

