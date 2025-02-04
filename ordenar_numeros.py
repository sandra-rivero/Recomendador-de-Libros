class MiLista:
    def __init__(self):
        self.mi_lista = [1, 15, 2, 17, 25,50,50,2,1,201]


    def numero_mas_alto(self):
        numero_maximo = self.mi_lista [0]
        for numero in self.mi_lista:
            if numero > numero_maximo:
                numero_maximo = numero
        return numero_maximo


    def numero_mas_bajo(self):
        numero_minimo = self.mi_lista[0]
        for numero in self.mi_lista:
            if numero < numero_minimo:
                numero_minimo = numero
        return numero_minimo   


    def ordenar_numeros_menor_a_mayor(self):
        numeros_ordenados = sorted(self.mi_lista)
        return numeros_ordenados
    

    def ordenar_numero_mayor_a_menor(self):
        numeros_odenados = sorted(self.mi_lista, reverse=True)
        return numeros_odenados


    def agregar_numero(self, numero_añadido):
        numero_añadido = self.mi_lista.append(numero_añadido)
        return self.mi_lista 


    def eliminar_numero(self, numero_eliminado):
            if numero_eliminado in self.mi_lista:
                numero_eliminado = self.mi_lista.remove(numero_eliminado)
                print("numero eliminado")
            else:
                print("este numero no existe")      


    def convertir_tupla(self):
        lista_tupla = tuple(self.mi_lista)
        return lista_tupla  


    def buscar_numero(self, numero):
        if numero in self.mi_lista:
            print(f"si está el numero {numero}")
        else:
            return None 

    suma_total = 0
    def sumar_todos_numeros_de_la_lista(self):
        for numeros in self.mi_lista:
            self.suma_total += numeros
        return self.suma_total
    
    cantidad_repetido= 0

    def ocurrencias_de_elementos(self, numero):
        for elementos in self.mi_lista:
            if elementos == numero:
                self.cantidad_repetido +=1
        return numero, self.cantidad_repetido
    

    '''
    quiero eliminar los numeros duplicados.
    necesito recorrer todos los numeros un a uno.
    Si ese numero esta repetido, eliminarlo
    sacar de nuevo la lista sin repetidos
    '''

    def eliminar_numeros_repetidos(self):
        lista_nueva= []
        for items in self.mi_lista:
            if items not in lista_nueva:
                lista_nueva.append(items)
        return lista_nueva        


    def eliminar_numeros_repetidos_set(self):#con set() la lista no mantiene el mismo orden
        lista_nueva = list(set(self.mi_lista))
        return lista_nueva    
    

        


        

    




###pruebas###

mi_lista_de_numeros = MiLista()



#mi_lista_de_numeros.numero_mas_alto()
#mi_lista_de_numeros.numero_mas_bajo()
#mi_lista_de_numeros.ordenar_numeros_menor_a_mayor()
#mi_lista_de_numeros.ordenar_numero_mayor_a_menor()
#mi_lista_de_numeros.agregar_numero(201)
mi_lista_de_numeros.eliminar_numero(2011)
#mi_lista_de_numeros.convertir_tupla()
#mi_lista_de_numeros.buscar_numero(1)
#mi_lista_de_numeros.sumar_todos_numeros_de_la_lista()
#mi_lista_de_numeros.ocurrencias_de_elementos(1)
#mi_lista_de_numeros.eliminar_numeros_repetidos()
#mi_lista_de_numeros.eliminar_numeros_repetidos_set()
