# Actividad 4

# Consigna 1:
# Teniendo en cuenta, lo  visto en el ejercicio anterior, crear un algoritmo que indique que pare si la luz está roja y que avance si la luz está verde.

# Consigna 2:
# ¿cómo deberíamos modificar el código para que pare si la luz está roja, avance si la luz está verde y que acelere si la luz está amarilla?

# Consigna 3:
# Agreguemosle al código la luz naranja para que frene.

colores = ['roja','verde', 'amarilla', 'naranja']

for i in colores:
    if i == 'roja':
        print('Pare')
    elif i == 'verde':
        print('Avance')
    elif i == 'amarilla':
        print('Acelere')
    elif i == 'naranja':
        print('Frene')
    else:
        break