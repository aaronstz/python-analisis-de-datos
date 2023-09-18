# ¿Qué nos devolverán los siguientes comandos?

# print(lista_metales[0])

# print(lista_metales[1])

# print(lista_metales[2])

# print(lista_metales[3])

# print(lista_metales[4])

# print(lista_metales[5]) --> si no está definido dirá que el índice de la lista está fuera de rango

# len(lista_compras)  --> devuelve la cantidad de objetos que contiene la lista

# append --> agrega un elemento al final de la lista

# pop --> elimina un elemento en el índice pasado como argumento

# insert --> agrega un elemento en el índice pasado como argumento y en el proceso mueve el elemento que se encontraba en ese índice previamente


lista_metales = ['hierro', 'oro', 'bronce', 'estaño', 'aluminio', 'brillante']
lista_metales.append('plata')

if lista_metales[1] == 'oro':
  lista_metales.pop(1)
  lista_metales.insert(1, 'anillo de oro')
  print(lista_metales)
else:
  print('No se cambió la lista ')

# Si Messi juega ganamos

lista_jugadores = ['Neymar', 'Ronaldo', 'Maradona']
jugador_user = input('Indique qué jugador agregarías a la lista ')

lista_jugadores.append(jugador_user)
respuestas_correctas = ['Messi', 'messi', 'lio', 'lio messi', 'lionel messi', 'lionel andres messi']

if jugador_user in respuestas_correctas:
  print('Ganamos ')
else:
  print('Perdimos ')