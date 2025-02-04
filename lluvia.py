#DATOS/CONFIGURACION
esta_lloviendo = True
coche_en_el_garaje = True 
tengo_paraguas = False
tengo_ganas = True


#PREGUNTAS
print(f"¿tengo ganas de salir?")
print(f"¿esta lloviendo?: {esta_lloviendo}")
print(f"¿tengo paraguas?: {tengo_paraguas}")
print(f"¿tengo el coche en el garaje?: {coche_en_el_garaje}")

#DECISION

if not tengo_ganas:
    print("Que les den")
else:
    if not esta_lloviendo and tengo_paraguas:
        print("Me voy de fiesta")
    elif coche_en_el_garaje:
        print("Que bien, puedo salir")  
    else:
        print("me quedo en casa")

