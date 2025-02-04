numero1 = 0
numero2 = 0


def numeros():
    global numero1
    global numero2
    numero1 = int(input())
    numero2 = int(input())

def sumar():
    global numero1
    global numero2
    print(int(numero1 + numero2))
   
def restar():
    global numero1
    global numero2
    print(int(numero1 - numero2))
   
def dividir():
    global numero1
    global numero2
    print(int(numero1 / numero2))  
   
def multiplicar():
    global numero1
    global numero2
    print(int(numero1 * numero2))


numeros()
sumar()
restar() 