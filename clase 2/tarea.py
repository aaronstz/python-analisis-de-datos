intentos = 0
contraseña_correcta = False
contraseña_creada = input('Cree su contraseña ')
usuario_libro = False

while intentos < 3 and contraseña_correcta == False:  #específico un límite de intentos incorrectos y compruebo que la contraseña sea incorrecta y los intentos fallidos sean menores a 3 y solo así el código puede avanzar
  contraseña_user = input('Introduzca su contraseña ')
  if int(contraseña_user) == int(contraseña_creada): #si la contraseña ingresada es igual a la contraseña que creó el usuario
    print('Bienvenido')
    contraseña_correcta = True #esto es para que no vuelva a ingresar al while y no vuelva a pedir la contraseña
    while usuario_libro == False: #otro while para comprobar que el usuario no se haya llevado ya un libro
      if usuario_libro == False: #este if es para concatenar más condiciones
        libro_deseado = input('Qué libro busca? 1.Las malas, 2.No es un río, 3.Nuestra parte de Noche o 4.Rayuela ')
        respuestas_si = ['si', 'yes', 'y', 's']
        if int(libro_deseado) == 1:
          print('Las malas es la primera novela de la escritora y actriz travesti​ argentina Camila Sosa Villada. Fue publicada en Argentina el 1 de marzo de 2019, bajo la editorial Tusquets Editores con sede en Barcelona, España.​')
          eleccion = input('Desea llevar este libro? Si/No ')
          if eleccion in respuestas_si: #verifico que haya respondido 'Si'
            usuario_libro = True #en este caso y en los siguientes el usuario ya registró un libro por ende no se entraría de vuelta al while ni a los if y se terminaría la compra
            print('Usted está llevando el libro "Las Malas"')
          else:
            usuario_libro = False #en este caso el usuario no registró un libro y se le vuelven a ofrecer las opciones anteriores
        elif int(libro_deseado) == 2:
          print('La trama de la novela sigue a Enero Rey y al Negro, quienes deciden llevar al hijo de su amigo muerto, Tilo, a pescar al mismo río en el que el padre de este se ahogó quince años atrás.')
          eleccion = input('Desea llevar este libro? Si/No ')
          if eleccion in respuestas_si:
            usuario_libro = True
            print('Usted está llevando el libro "No es un río"')
          else:
            usuario_libro = False
        elif int(libro_deseado) == 3:
          print('En el Buenos Aires de 1981, durante la dictadura militar que acosaba a Argentina, Juan y su hijo Gaspar emprenden un abrupto viaje en coche hacia las Cataratas del Iguazú, tras la inesperada y poco clara muerte de la madre, Rosario, con el fin de escapar del crudo destino que eclipsa el futuro del pequeño.')
          eleccion = input('Desea llevar este libro? Si/No ')
          if eleccion in respuestas_si:
            usuario_libro = True
            print('Usted está llevando el libro "Nuestra parte de noche"')
          else:
            usuario_libro = False
        elif int(libro_deseado) == 4:
          print('Rayuela es la segunda novela del escritor argentino Julio Cortázar. Escrita en París y publicada por primera vez el 28 de junio de 1963, constituye una de las obras centrales del boom latinoamericano y de la literatura en español.')
          eleccion = input('Desea llevar este libro? Si/No ')
          if eleccion in respuestas_si:
            usuario_libro = True
            print('Usted está llevando el libro "Rayuela"')
          else:
            usuario_libro = False
        else:
            print('Por favor introduzca una de las opciones presentadas ') #esto es por si el usuario eligió por ejemplo el número 5 o cualquier otro que no sean las opciones ofrecidas
  else:
    intentos += 1 #acá sumo un intento al array de intentos fallidos
    print('Contraseña incorrecta ')
    print(intentos)
if intentos == 3 and contraseña_correcta == False: #una vez que el usuario haya llegado al límite de intentos se le comunicará que deberá realizar para recuperar su cuenta
  print('Debe pasar por la libreria central a restaurar su cuenta')
