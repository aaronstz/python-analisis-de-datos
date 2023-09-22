#"La diferencia entre suerte y azar radica en que la suerte es particular y el azar es universal. La suerte es generalmente subjetiva mientras que el azar es objetivo. La buena o mala suerte es específicamente de una persona, en cambio el azar es la constatación de que las circunstancias de la vida son aleatorias."

import random

jugador_1 = input('Inserte el nombre del primer jugador ')
jugador_2 = input('Inserte el nombre del segundo jugador ')
prenda_1 = input('Inserte la prenda para el segundo jugador ')
prenda_2 = input('Inserte la prenda para el primer jugador ')
def tira_moneda(): #Esta función determina el resultado de tirar una moneda al aire

  resultados = []
  secas = 0
  caras = 0
  count = 0

  while count < 6:
    moneda = random.randint(0, 1)
    if moneda == 0:
      resultados += [f"{count + 1}: cara"]
      count += 1
      caras += 1
    elif moneda == 1:
      resultados += [f"{count + 1}: seca"]
      count += 1
      secas += 1
    if count >= 6:
      if secas == 3 and caras == 3:
        return resultados, 'Empate '
      if caras > secas:
        return resultados, f'Ganó {jugador_1} y {jugador_2} tiene que hacer la prenda: {prenda_1}'
      elif secas > caras:
        return resultados, f'Ganó {jugador_2} y {jugador_1} tiene que hacer la prenda: {prenda_2}'

num = 1
for i in range(0, 3): #Se ejecuta la función tres veces para comprobar que no estén trucados los resultados :p
  i = tira_moneda()
  print(f"Partida {num}",i)
  num += 1