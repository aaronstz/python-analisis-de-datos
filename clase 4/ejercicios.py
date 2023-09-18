#si son las 8 de la mañana y ya sali para el trabajo, estoy llegando a tiempo
#si son las 8 de la mañana y no sali para el trabajo, voy a llegar un poco tarde
#si son las 9 de la mañana y no sali para el trabajo, no llego

hora=int(input("Que hora es? "))
salir=input("Ya saliste para el trabajo? si/no ")
if hora == 8 and salir== "si":
  print("Estas llegando a tiempo.")
elif hora== 8 and salir== "no":
  print("Vas a llegar un poco tarde.")
elif hora==9 and salir=="no":
  print("No llegas.")
elif hora<8 and salir=="no":
  print("Todavia tenes tiempo para salir")
elif hora<8 and salir=="si":
  print("Vas a llegar temprano.")
else: print("Opción incorrecta")

#si me encuentro un perro en la calle y me lo quiero llevar a casa, verificar las siguientes condiciones:
#si el perro está sano y tengo comida en casa, me lo llevo directo
#si el perro está sano pero no tengo comida en casa, debería ir a comprar antes de llevarlo
#si el perro está lastimado, lo debería llevar primero al veterinario

sano = input("El perro está sano? si/no ")
comida = input("Tengo comida en casa? si/no ")
if sano== "si" and comida == "si":
  print("Me lo llevo directamente.")
elif sano=="si" and comida=="no":
  print("Tengo que comprar comida antes de llevarlo.")
elif sano=="no" and comida=="si":
  print("Solo tengo que llevarlo al veterinario. Comida ya tengo.")
elif sano=="no" and comida=="no":
  print("Tengo que llevarlo al veterinario y comprar comida.")
else: print("Opcion incorrecta")
