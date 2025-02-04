def multiplicar (num1, num2):
    print(num1*num2)

multiplicar(2,2)   

########################

def saludar(nombre):
    print(f"Hola! {nombre}")

saludar("sandra")  

############################

def presentacion(nombre, edad):
    print(f"Hola! soy {nombre}, y tengo {edad} años")


presentacion("sandra","34")


##########################


def es_par(numero1):
    numero1 = int(numero1)
    if numero1 % 2 == 0:
        print("este número es par")
    else:
        print("este número es impar") 


es_par("3")        


