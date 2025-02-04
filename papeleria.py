class Papeleria:

    def __init__(self):
        self.inventario = {"cuadernos" : 5, "boligrafos": 3, "lapices": 1 }

    #abajo esta la propueta segun lo que pides
         
    #def __init__(self, material, cantidad):
        #self.inventario = {material: cantidad}     


    def vender_material(self, material, cantidad):
        if material in self.inventario and cantidad <= self.inventario[material]: #comprueba si lo que pide está en el inventario y si hay stock
            print(f"Aquí tienes tu compra de {cantidad} {material}")
            self.inventario[material] -= cantidad #resta la cantidad indicada en el stock del inventario  
        else:
            print(f"lo siento, no tengo {material}")
     


    def pedido_a_proveedor(self, material, cantidad):
        if material in self.inventario: #comprueba si el material indicado esta en el inventario
            self.inventario[material] += cantidad #suma la cantidad indicada al stock del inventario
            return material
        else:
            print("No podemos comprar eso")    



    def listado_material_disponible(self):
        material = self.inventario.get(0)
        for material in self.inventario:
            return material



    def material_menos_stock(self): #rescata el material que tenga el valor mas pequeño
        cantidad_minima = 0
        for cantidad in self.inventario.items():
            if cantidad < cantidad_minima:
                return cantidad
    


    def material_mas_stock(self):
        material_maximo = None
        cantidad_maxima = -1
        for material, cantidad in self.inventario.items():
            if cantidad > cantidad_maxima:
                cantidad_maxima = cantidad
                material_maximo = material
        print({material}, {cantidad})               


            
    # pendiente corregir: def ordenar_menor_a_mayor(self):
        ordenar = sorted(self.inventario.items(), key=lambda item: item[1] )
        return ordenar   



    # pendiente corregir: def ordenar_mayor_a_menor(self):
        ordenar = sorted(self.inventario.items(), key=lambda item: item[1], reverse=True )
        return ordenar



# hago funciones de prueba, para aprender como convertir el diccionario en diferentes modalidades a la suya(dict)

    def convertir_inventario_tupla(self):
        tupla_inventario = tuple((clave, self.inventario[clave])for clave in self.inventario)
        return tupla_inventario



    def convertir_inventario_lista_claves(self):
        lista_inventario_claves = self.inventario.keys()
        return lista_inventario_claves



    def convertir_inventario_lista_valores(self):
        lista_inventario_valores = self.inventario.values()
        return lista_inventario_valores   
        
           



mi_tienda = Papeleria()
#material_vendido = mi_tienda.vender_material()



##############test##########
#mi_tienda.vender_material("cuadernos", 1)
#material_vendido("cuadernos",2)
#mi_tienda.pedido_a_proveedor("cuadernos",5)
#print(mi_tienda.inventario)
#mi_tienda.listado_material_disponible()
#mi_tienda.material_menos_stock()
#mi_tienda.material_mas_stock()
#mi_tienda.ordenar_menor_a_mayor()
#mi_tienda.ordenar_mayor_a_menor()
#mi_tienda.convertir_inventario_tupla()
#mi_tienda.convertir_inventario_lista_claves()
#mi_tienda.convertir_inventario_lista_valores()
