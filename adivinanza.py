#juego de adivinanzas donde tendremos una respuesta correcta
#tendremos una respuesta del usuario
#tendremos que decidir si es correcta o no la respuesta del usuario

respuesta_correcta = "platano"

while True:
    respuesta_usuario = input("Oro parece, plata no es ¿que es?:  ")
    if respuesta_correcta == respuesta_usuario:
        print("Genial! lo adivinaste!!")
        break
    else:
        print("Incorrecto, vuelve a intentarlo")