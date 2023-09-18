## Condicional

#Resolución del ejercicio planteado por el compañero

##Listas

# Vamos a armar una lista con comidas

comidas=['milanesa', 'dulce de leche', 'hamburguesa', 'pizza', 'cerveza'] #COMPLETAR
comidas[2:]

# Explorar los siguientes comandos



# ```
# comidas[0]  trae el primer elemento
# comidas[:3] trae los primeros tres elementos (milanesa, dulce de leche, hamburguesa)
# comidas[2:] trae desde el elemento de la posicion 2 (hamburguesa, pizza, cerveza)
# comidas[2] trae el elemento de la posicion 2
# len(comidas) imprime la cantidad de elementos
# ```



# 1. Probarlos y comentar al lado de cada uno qué hace cada uno
# 2. ¿Cómo podemos hacer para obtener el segundo elemento de la lista?
# 3. ¿Cómo harían para obtener el último?
# 4. ¿Cómo obtenemos los primeros 4 elementos? ¿Y los últimos 4?

print(comidas[1]) #para traer el segundo elemento
print(comidas[4]) #para traer el ultimo elemento
print(comidas[:4]) #los primeros cuatro
print(comidas[1:]) #los ultimos cuatro


print(comidas[-1]) #trae el ultimo
print(comidas[-2:]) #trae los ultimos dos
print(comidas[2:4]) # trae desde la posicion 2 (hamburguesa) hasta el elemento 4 (pizza)

# EXTRA:
# Probar estos otros comandos.



# ```
# comidas[-1]
# comidas[-2:]
# comidas[2:4]
# ```

# ¿Alguna de las consignas anteriores se podrían resolver más fácil con estos comandos?


## Actualizar una lista

# Probar los siguientes comandos y discutir qué hacen.

# ```
# comidas[4] = 'fideos'
# comidas.append('papas al horno')
# ```



comidas[4] = 'fideos' #reemplaza lo que haya en la posicion 4 por fideos
comidas.append('papas al horno') #agrega al final de la lista papas al horno
print(comidas)

## Lista vacía

# ¡Podemos armar una lista vacía!

lista_vacia = []
len(lista_vacia)

# ¿Qué longitud piensan que va a tener? Comprobalo

lista_vacia.append('fideos')
lista_vacia.append('papas fritas')
print(lista_vacia)

# ¿Qué largo piensan que va a tener ahora? Comprobalo!

len(lista_vacia)

#Operaciones con números en Listas:
# Analicemos listas de números

lista_numeros=[0,3,2,7,8]
lista_numeros[0] += 3
lista_numeros[1] -= 1
lista_numeros[2] *= 5
len(lista_numeros)
print(lista_numeros)

print(sum(lista_numeros))


# 1) Sumale 3 al primer elemento

# 2)Restale 2 al segundo elemento

# 3)Multiplica por 5 al último elemento

# 4)Averigua el largo de la lista

# 5) Averigua la suma de todos los elementos de la lista
