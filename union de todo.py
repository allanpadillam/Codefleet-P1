import random

# Diccionario de palabras categorizadas (todas de al menos 10 letras)
PALABRAS_POR_CATEGORIA = {
    "Frutas": [
        "maracuya", "frambuesa", "granadilla", "mandarina", "arándanos"
    ],
    "Países": [
        "argentinano", "australiana", "guatemala", "kazajistán", "uzbekistán"
    ],
    "Nombres": [
        "fernandito", "cristopher", "alejandros", "franciscas", "jacqueline"
    ],
    "Continentes": [
        "sudamerica", "norteamérica", "oceaniaaaa", "antártidaa", "europaaaaa"
    ],
    "Animales": [
        "hipopotamo", "orangutanes", "cocodrilos", "camaleones", "chimpances"
    ]
}

def obtener_palabra_aleatoria():
    """
    Selecciona aleatoriamente una categoría y una palabra dentro de ella.

    :return: Una tupla con la categoría y la palabra secreta.
    """
    categoria = random.choice(list(PALABRAS_POR_CATEGORIA.keys()))
    palabra = random.choice(PALABRAS_POR_CATEGORIA[categoria]).upper()
    return categoria, palabra


# draw.py

DIBUJOS = [
    # 0 - Solo base
    """
    
       
       
       
       
       
    =========
    """,
    # 1 - Base + poste vertical
    """
       |
       |
       |
       |
       |
       |
    =========
    """,
    # 2 - Base + poste vertical + techo
    """
       ------
       |
       |
       |
       |
       |
       |
    =========
    """,
    # 3 - Base + poste vertical + techo + cuerda
    """
       ------
       |    |
       |
       |
       |
       |
       |
    =========
    """,
    # 4 - Estructura completa sin muñeco
    """
       ------
       |    |
       |    |
       |    
       |    
       |    
    =========
    """,
    # 5 - Cabeza
    """
       ------
       |    |
       |    |
       |    O
       |    
       |    
       |    
    =========
    """,
    # 6 - Cabeza + torso
    """
       ------
       |    |
       |    |
       |    O
       |    |
       |    
       |    
    =========
    """,
    # 7 - Cabeza + torso + brazo izquierdo
    """
       ------
       |    |
       |    |
       |    O
       |   /|
       |    
       |    
    =========
    """,
    # 8 - Cabeza + torso + ambos brazos
    """
       ------
       |    |
       |    |
       |    O
       |   /|\\
       |    
       |    
    =========
    """,
    # 9 - Ahorcado completo
    """
       ------
       |    |
       |    |
       |    O
       |   /|\\
       |   / \\
       |    
    =========
    """
]

def mostrar_dibujo(longitud_palabra: int, errores: int):
    """
    Muestra el dibujo del ahorcado basado en el número de letras de la palabra y la cantidad de errores.

    :param longitud_palabra: Número de letras de la palabra a adivinar.
    :param errores: Número de intentos fallidos hasta el momento.
    """
    max_dibujos = len(DIBUJOS)

    # Asegura que errores no sobrepase el límite
    indice_dibujo = min(errores, max_dibujos - 1)

    print(DIBUJOS[indice_dibujo])

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
    print(f"\n🧠 La categoría es: {categoria}")


def mostrar_intentos_restantes(intentos_restantes, intento_actual):
    """
    Muestra los intentos restantes e intento actual.
    """
    print(f"🔄 Intento {intento_actual} - Te quedan {intentos_restantes} intento(s).\n")


def mostrar_felicitaciones(nombre_jugador, palabra):
    """
    Felicita al jugador por adivinar correctamente.
    """
    print(f"\n🎉 ¡Felicidades, {nombre_jugador}! Adivinaste la palabra: {palabra} ✅\n")


def mostrar_palabra_correcta(nombre_jugador, palabra):
    """
    Muestra la palabra correcta cuando el jugador pierde.
    """
    print(f"\n😢 Lo siento, {nombre_jugador}. Se acabaron los intentos.")
    print(f"La palabra correcta era: {palabra} ❌\n")

# from wordbank import obtener_palabra_aleatoria
# Las siguientes importaciones se mantienen si existen los módulos, si no, comentar o eliminar.
# from pr_console import (
#     solicitar_nombre_jugador,
#     mostrar_categoria,
#     mostrar_intentos_restantes,
#     mostrar_felicitaciones,
#     mostrar_palabra_correcta
# )
# from draw import mostrar_dibujo

def mostrar_progreso(palabra, letras_adivinadas):
    """
    Muestra el estado actual de la palabra con guiones bajos y letras acertadas.
    """
    progreso = ' '.join([letra if letra in letras_adivinadas else '_' for letra in palabra])
    print("\n🔤 Progreso: ", progreso)
    return progreso

def jugar_ahorcado():
    nombre = solicitar_nombre_jugador()
    categoria, palabra_secreta = obtener_palabra_aleatoria()
    mostrar_categoria(categoria)

    letras_adivinadas = set()
    errores = 0
    longitud_palabra = len(palabra_secreta)
    max_intentos = longitud_palabra + 1

    while errores < max_intentos:
        mostrar_dibujo(longitud_palabra, errores)
        mostrar_intentos_restantes(max_intentos - errores, errores + 1)
        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)

        if "_" not in progreso_actual:
            mostrar_felicitaciones(nombre, palabra_secreta)
            break

        intento = input("\n🔡 Ingresa una letra: ").strip().upper()

        if len(intento) != 1 or not intento.isalpha():
            print("⚠️ Solo puedes ingresar una letra válida.")
            continue

        if intento in letras_adivinadas:
            print("⚠️ Ya intentaste esa letra. Prueba otra.")
            continue

        letras_adivinadas.add(intento)

        if intento not in palabra_secreta:
            errores += 1
            print("❌ ¡Letra incorrecta!")

    else:
        mostrar_dibujo(longitud_palabra, errores)
        mostrar_palabra_correcta(nombre, palabra_secreta)

if __name__ == "__main__":
    jugar_ahorcado()

