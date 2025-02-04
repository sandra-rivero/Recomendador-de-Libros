class MiAgenda:   
    def __init__(self):
        self.mi_agenda={}

    def agregar_contacto(self,nombre, telefono):
        if nombre.isalpha() and telefono.isdigit():
            if not nombre in self.mi_agenda:
                self.mi_agenda[nombre]=telefono
                print(f"el contacto de {nombre} ha sido agregado")
            else:
                print("Contacto ya existente")
        else:
            print("nombre/telefono incorrecto, intentelo de nuevo")  

    def mostrar_agenda_completa(self):
        return self.mi_agenda  

    def eliminar_contacto(self,nombre):
        if nombre in self.mi_agenda:
            del self.mi_agenda[nombre]
            print("Contacto eliminado")
        else:
            print(f"el contacto {nombre} no se encuentra en la agenda")   

    def buscador_contacto(self, nombre):
        if nombre in self.mi_agenda:
            return nombre, self.mi_agenda[nombre]

    def modificar_nombre_a_un_contacto_existente(self,nombre):
        if nombre in self.mi_agenda:
            nuevo_nombre = input("indique el nuevo nombre: ")
            self.mi_agenda[nuevo_nombre] = self.mi_agenda.pop(nombre)
            print("El contacto se ha modificado")
        else:
            print("El contacto indicado no se encuentra en la agenda")  

    def invertir_agenda(self):
        nuevo_diccionario={}
        for clave, valor in self.mi_agenda.items():
            nuevo_diccionario[valor] = clave
        print(nuevo_diccionario)    







###creamos variables para llamar a las clases###
clase_agenda = MiAgenda()
###ejemplos para poder probar las funciones creadas###
clase_agenda.agregar_contacto("12sandra","649561296")
clase_agenda.agregar_contacto("Jose","965451236")
#clase_agenda.agregar_contacto("Maria","666232325")
#clase_agenda.agregar_contacto("Pedro","622252514")
#clase_agenda.eliminar_contacto("sandra")
#clase_agenda.buscador_contacto("Maria")
#clase_agenda.modificar_nombre_a_un_contacto_existente("Maria")
#clase_agenda.mostrar_agenda_completa()
#clase_agenda.invertir_agenda()
    
