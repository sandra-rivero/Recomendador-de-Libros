class KebabRestaurante:
    def __init__(self):
        self.panes = 0

    def hacer_kebab(self, ingredientes):
        if self.panes <= 0:
            return "lo siento amego no pan hoy"

        print(f"estoy haciendo tu kebab con {ingredientes}")

        # lo hace
        self.panes = self.panes - 1

        return f"Kebab con {ingredientes}"

    def pedir_pan_al_proveedor(self, numero_de_panes):
        self.panes += numero_de_panes

    def darle_un_pan_extra_al_cliente(self):
        if self.panes > 0:
            self.panes -= 1
            return "aquí está tu pan"
        else:
            return "no queda pan"

    def darle_panes_extra_al_cliente(self, numero_de_panes):
        if self.panes > numero_de_panes:
            self.panes -= numero_de_panes
            return "aquí está tu pan"
        else:
            return f"no queda tanto pan, sólo tengo {self.panes}"


k = KebabRestaurante()

k.darle_panes_extra_al_cliente(2)
