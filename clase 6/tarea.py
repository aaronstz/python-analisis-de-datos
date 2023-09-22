# EJERCICIO UNO

# Contar la cantidad de letras a que hay en la lista Contar la cantidad de letras m que hay en la lista Agregale 3 letras a y 7 letras m Volver a contar la cantidad de letras a , m y x que hay en las listas.

# ¿Qué serían a y m en este ejercicio?


lista_letras=["m", "b", "a", "m","s", "a", "l", "o", "c", "o", "a", "m", "o", "r", "a","z", "a", "b", "a", "c", "h", "e"]

def my_function(letra1, letra2, letra3 =' '):
  count_1 = 0
  count_2 = 0
  count_3 = 0
  for i in lista_letras:
    if i == letra1:
      count_1 += 1
    if i == letra2:
      count_2 += 1
    if i == letra3:
      count_3 += 1
  print(f"Hay {count_1} letras {letra1}, {count_2} letras {letra2} y {count_3} letras {letra3}")

lista_letras = lista_letras + ["a"] * 3
lista_letras = lista_letras + ["m"] * 7

my_function("a", "m", "x")


# Hacer un filtro, es decir, armar una nueva lista con solamente los elementos que cumplan una determinada condición. En este caso armaremos una nueva lista que tenga solamente la letra a.

lista_letras=["m", "b", "a", "m","s", "a", "l", "o", "c", "o", "a", "m", "o", "r", "a","z", "a", "b", "a", "c", "h", "e"]

def filter(arg):
  lista_nueva = []
  for i in lista_letras:
    if arg == i:
      lista_nueva = lista_nueva + [i]
      i =+ 1
  return lista_nueva, len(lista_nueva)
filter("a")