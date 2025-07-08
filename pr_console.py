def solicitar_nombre_jugador():
    """
    Pide al jugador su nombre y lo devuelve.
    """
    nombre = input("¡Bienvenido al juego del ahorcado! ¿Cuál es tu nombre?: ")
    return nombre.strip().title()


def mostrar_categoria(categoria):
    """
    Muestra la categoría de la palabra seleccionada.
    """
    print(f"\n La categoría es: {categoria}")


def mostrar_intentos_restantes(intentos_restantes, intento_actual):
    """
    Muestra los intentos restantes e intento actual.
    """
    print(f"Intento {intento_actual} - Te quedan {intentos_restantes} intento(s).\n")


def mostrar_felicitaciones(nombre_jugador, palabra):
    """
    Felicita al jugador por adivinar correctamente.
    """
    print(f"\n ¡Felicidades, {nombre_jugador}! Adivinaste la palabra: {palabra} \n")


def mostrar_palabra_correcta(nombre_jugador, palabra):
    """
    Muestra la palabra correcta cuando el jugador pierde.
    """
    print(f"\n Lo siento, {nombre_jugador}. Se acabaron los intentos.")
    print(f"La palabra correcta era: {palabra} \n")
