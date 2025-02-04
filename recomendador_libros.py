class Libro:
    def __init__(self, titulo, genero, autor, año):
        self.titulo = titulo
        self.genero = genero
        self.autor = autor
        self.año = año

    def get_info(self):
        print(f" mi info es {self.titulo} {self.genero}")    


class RecomendadorDeLibros:

    def __init__(self):
        self.conteo = {}
        self.libros = [
            Libro("Cien años de soledad", "Realismo mágico", "pepe","1985"),
            Libro("1984", "Distopía", "pepe","1985"),
            Libro("El principito", "Ficción", "pepe","1985"),
            Libro("El castillo", "Distopía", "jose","1985")
        ]

    def numero_de_busquedas(self,titulo):
        return self.conteo.get(titulo,0)
        

    def obtener_libros_por_genero(self, genero): 
        resultados = [libro for libro in self.libros if libro.genero == genero] 
        self.actualizar_conteo(resultados)
        return resultados

 
    def obtener_libros_por_autor(self, autor): 
        resultados = [libro for libro in self.libros if libro.autor == autor]
        self.actualizar_conteo(resultados)
        return resultados

    def añadir_libro(self,libro):
        r = self.obtener_libro_por_titulo(libro.titulo)
        if r:
            raise ValueError("el libro ya está añadido")
        self.libros.append(libro)
    
            
    def actualizar_conteo(self, resultados):
        for libro in resultados:
            if libro.titulo in self.conteo:
                self.conteo[libro.titulo]+= 1
            else:
                self.conteo[libro.titulo] = 1    


    def eliminar_libro(self,titulo):
        libro_a_borrar = self.obtener_libro_por_titulo(titulo)
        self.libros.remove(libro_a_borrar)

    def obtener_libro_por_titulo(self,titulo):
        resultados = [libro for libro in self.libros if libro.titulo == titulo]
        self.actualizar_conteo(resultados)
        if not resultados:
            return None
        else:
            return resultados[0]
        


#############################################################

recomendador_de_libros = RecomendadorDeLibros()

recomendados = recomendador_de_libros.obtener_libros_por_genero("Distopía")
for libro in recomendados:
    libro.get_info()

recomendador_de_libros.añadir_libro(Libro("el barco", "Distopía","antonia","2001"))

recomendador_de_libros.obtener_libros_por_genero("Distopía")

print("")
recomendados = recomendador_de_libros.obtener_libros_por_genero("Distopía")
for libro in recomendados:
    libro.get_info()

recomendado = recomendador_de_libros.obtener_libro_por_titulo("el barco")
if not recomendado:
    print("Libro borrado")
else:
    print("error")
recomendado = recomendador_de_libros.obtener_libro_por_titulo("Cien años de soledad")
recomendado = recomendador_de_libros.obtener_libro_por_titulo("Cien años de soledad")
recomendado = recomendador_de_libros.obtener_libro_por_titulo("Cien años de soledad")
recomendado = recomendador_de_libros.obtener_libro_por_titulo("Cien años de soledad")
recomendado = recomendador_de_libros.obtener_libro_por_titulo("Cien años de soledad")

########################
numero_busquedas = recomendador_de_libros.numero_de_busquedas("el barco")
print(numero_busquedas)
numero_busquedas = recomendador_de_libros.numero_de_busquedas("Cien años de soledad")
print(numero_busquedas)


