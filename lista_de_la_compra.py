class ListaCompra:
    def __init__(self, productos):
        self.lista_compra = []


    def agregar_productos (self, producto):
        if not producto in self.lista_compra:
            self.lista_compra.append(producto)
        else:
            print("este producto ya esta en la lista")
    

    def eliminar_producto (self, producto):
        if producto in self.lista_compra:
            self.lista_compra.remove(producto)
        else:
            print("Ese producto no está en la lista")  


    def cuantos_productos_hay_en_la_lista (self):
        return len(self.lista_compra)
              

    def borrar_lista_de_la_compra_1(self):
        self.lista_compra.clear()
        

    def borrar_lista_de_la_compra_2(self):
            self.lista_compra=[]

    def borrar_lista_de_la_compra_3(self):
        del self.lista_compra[:]


    def buscar_producto_en_la_lista(self,producto):
        if producto in self.lista_compra:
            print(f"si esta {producto} en la lista de la compra")
        else:
            print(f"{producto} no esta en la lista de la compra")    


    def ultimo_elemento_de_la_lista (self):
        return self.lista_compra[-1]

    productos_faltantes = []
    def lista_de_productos_que_faltan (self, productos):
            if productos not in self.lista_compra:
                self.productos_faltantes.append(productos)
                self.lista_compra.append(self.productos_faltantes)
            else:
                print("estos podructos ya están")


          




    

lista_compra = ListaCompra("agua")

###pruebas###
lista_compra.agregar_productos("fregona")
lista_compra.agregar_productos("colacao")
#lista_compra.agregar_productos("colacao")
#lista_compra.agregar_productos("leche")
#lista_compra.eliminar_producto("leche")
#lista_compra.cuantos_productos_hay_en_la_lista()
#lista_compra.borrar_lista_de_la_compra_1()
#lista_compra.buscar_producto_en_la_lista("fregona")
#lista_compra.ultimo_elemento_de_la_lista()
#lista_compra.lista_de_productos_que_faltan("pan")