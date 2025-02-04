nombre = "Alice"
contraseña = "123"
intentos = 0


#Ahora pedimos al usuario que indique el nombre y la contraseña:
while intentos < 3:
    nombre_usuario = input("Indique su nombre: ")
    contraseña_usuario = input("Indique su contraseña: ")

#Ahora comprobamos si usuario y contraseña son correctos para acceder:
    if nombre_usuario== nombre and contraseña_usuario == contraseña:
        print("Hola Alice! Bienvenida!")
        break
    else:
         intentos += 1
         if intentos < 3:
            print("Nombre o contraseña incorrecto, vuelva a intentarlo") 
         else:
            print("Su cuenta ha sido bloqueada, por favor, póngase en contacto con su operador")