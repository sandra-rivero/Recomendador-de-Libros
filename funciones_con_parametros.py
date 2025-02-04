dinero = 100.3
persona_con_dinero = "sandra"

def sacar_dinero(persona, saldo_a_retirar):
    global dinero
    # ENTRADA
    print("soy un cajero...🤖")
    print("veo que quieres sacar:", saldo_a_retirar)

    if persona != persona_con_dinero:
        print(" No estas autorizado, vete")
        return 0
    
    # OPERACIÓN    
    if saldo_a_retirar <= dinero:
        dinero -= saldo_a_retirar
        print(f"Has retirado {saldo_a_retirar} euros.")
        print(f"Saldo restante: {dinero} euros.")  # Mostramos el dinero restante
        return saldo_a_retirar
    else:
        print("No tienes suficiente dinero")
    
    return 0 

# persona = "sandra"
dinero_sacado = sacar_dinero("sandra",40)
print(f"\n el dinero que he sacado es {dinero_sacado}")


def consultar_saldo(persona):
    if persona != persona_con_dinero:
        print(" No estas autorizado, vete")
        return 0

    return dinero


def ingresar_dinero(persona, saldo_a_ingresar):
    global dinero

    if persona != persona_con_dinero:
        print(" No estas autorizado, vete")
        return

    dinero = dinero + saldo_a_ingresar
