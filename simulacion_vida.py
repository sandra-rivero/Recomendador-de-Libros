#este simulador hará preguntas y dependiendo de las elecciones, el día termina de una manera u otra.

#primero solicitaremos los datos del usuario, creando una función para pedir dátos básicos, estos datos básicos han de ser variables:

def bienvenida():
    nombre = input("Indique su nombre: ")
    edad = input("Indique su edad: ")
    lugar = input("Indique el lugar donde vive: ")
    #una vez solicitado los datos, daremos un breve mensaje al usuario:
    print(f"¡Hola, {nombre}! Ahora ya sé que tienes {edad} años y que vives en {lugar}. A partir de ahora, te acompañaré a lo largo del día.")
    print("A medida que avancemos, te haré preguntas sobre tus decisiones diarias. Las elecciones que hagas influirán en cómo termina tu día, de una manera u otra.")
    print("¡Comencemos!")

#vamos a separar el día en 3 partes, mañana/tarde/noche, creando una función para cada una de ellas, de esta manera, según la parte que se use, se harán diferentes acciones.

puntos = 0
trabajar = "trabajar"
descansar = "descansar"
mañana_productiva = "mañana productiva"
mañana_con_problemas = "mañana con problemas"
seguir_trabajando = "seguir trabajando"
tarde_de_descanso = "tarde de descanso"
hobbies = "hobbies"
tirado_en_el_sofa = "tirado en el sofa"
cena_rica = "cena rica"
algo_rapido = "algo rapido"
leer = "leer"
ver_serie = "ver serie"


def mañana ():
    decision_1_mañana = input(f"Es hora de tu primera decisión del día ¿irás a {trabajar} o vas a {descansar} ?: ").lower()
    if decision_1_mañana == "trabajar":
        puntos += 1
    elif decision_1_mañana == "descansar":
        puntos += 5    

    decision_2_mañana = input(f"Continuemos averiguando que tal va tu día ¿como ha ido la mañana? {mañana_productiva} o más bien ha sido una {mañana_con_problemas} ").lower()
    if decision_2_mañana == "mañana productiva":
        puntos += 3
    elif decision_2_mañana == "mañana con problemas":
        puntos += 1  


def tarde():
    decision_1_tarde = input(f"¿tu día como avanza? {seguir_trabajando} o {tarde_de_descanso}").lower()
    if decision_1_tarde == "seguir trabajando":
        puntos +=1
    elif decision_1_tarde == "tarde de descanso":
        puntos += 5    
    

    decision_2_tarde = input(f"¿que harás estar tarde? Harás algo de {hobbies} o {tirado_en_el_sofa}").lower()
    if decision_2_tarde == "hobbies":
        puntos += 6
    elif decision_2_tarde == "te_tiraras_en_el_sofa":
        puntos += 2


def noche (): 
    decision_1_noche = input(f"¿cuale serán tus últimas tareas del dia? harás {cena_rica}  o cenarás {algo_rapido}").lower()
    if decision_1_noche == "cena rica":
        puntos +=5
    elif decision_1_noche == "algo rapido":
        puntos +=1   

    decision_2_noche = input(f"para finalizar el día ¿que harás? {leer} o {ver_serie} en la tele").lower()
    if decision_2_noche == "leer":
        puntos +=5
    elif decision_2_noche == "ver serie":
        puntos +=4    

#una vez establecido el tema de las preguntas y decisiones, hay que hacer el cómpunto de puntos acumulados:

def puntuacion():
    if puntos < 10:
        print(" Vaya hoy has tenido un día pésimo, el consejo de hoy es que te vayas a dormir y mañana será otro día")

    elif puntos >11 and puntos >20:
        print("tu día no ha estado mal, podría mejorar, mañana a ver que pasa")    

    elif puntos >21 and puntos >30:
        print("Bueno, ha sido un día bueno, ole!")

    elif puntos <31:
        print("pedazo de día, mañana podría ser igual")    



bienvenida()
mañana()
tarde()
noche()
puntuacion()