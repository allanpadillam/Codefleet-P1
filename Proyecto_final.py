import random

palabras_por_categoria = {
    "frutas": [
        "frambuesas",
        "mandarinas",
        "granadillas",
        "maracuyaso",
        "higoschumbos"
    ],
    "paises": [
        "kazajistan",
        "uzbekistan",
        "australiana",
        "afganistan",
        "nicaraguans"
    ],
    "nombres": [
        "cristopher",
        "fernandito",
        "jacqueline",
        "alejandros",
        "franciscas"
    ],
    "continentes": [
        "sudamerica",
        "norteamerica",
        "antartidano",
        "oceaniafull",
        "europalinda"
    ],
    "animales": [
        "hipopotamo",
        "orangutanes",
        "cocodrilos",
        "camaleones",
        "chimpances"
    ]
}

dibujos_ahorcado = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

def elegir_palabra():
    categoria = random.choice(list(palabras_por_categoria.keys()))
    palabra = random.choice(palabras_por_categoria[categoria]).lower()
    return categoria, palabra

def mostrar_progreso(palabra, letras_usadas):
    progreso = ""
    for letra in palabra:
        if letra in letras_usadas:
            progreso += letra + " "
        else:
            progreso += "_ "
    print("\nPalabra: ", progreso.strip())
    return "_" in progreso

def mostrar_ahorcado(error_actual, errores_maximos):
    total_dibujos = len(dibujos_ahorcado)
    indice = int((error_actual / errores_maximos) * (total_dibujos - 1))
    indice = min(indice, total_dibujos - 1)
    print(dibujos_ahorcado[indice])

def pedir_letra(letras_usadas):
    while True:
        letra = input("Ingresa una letra: ").strip().lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, escribe solo una letra válida.")
        elif letra in letras_usadas:
            print("Ya escribiste esa letra. Intenta otra.")
        else:
            return letra

def jugar():
    print("Bienvenido al juego del ahorcado!")
    nombre = input("¿Cómo te llamás?: ").strip().title()

    categoria, palabra = elegir_palabra()
    print(f"\nHola {nombre}, la categoría de la palabra es: {categoria}")
    letras_usadas = []
    errores = 0
    intentos_maximos = len(palabra) + 1

    while errores < intentos_maximos:
        mostrar_ahorcado(errores, intentos_maximos)
        print(f"Intento {errores + 1} de {intentos_maximos}")
        quedan_letras = mostrar_progreso(palabra, letras_usadas)

        if not quedan_letras:
            print(f"\n¡Felicidades {nombre}! Adivinaste la palabra: {palabra}")
            break

        letra = pedir_letra(letras_usadas)
        letras_usadas.append(letra)

        if letra not in palabra:
            errores += 1
            print("Letra incorrecta.")
        else:
            print("¡Bien! Esa letra está en la palabra.")

    else:
        mostrar_ahorcado(intentos_maximos, intentos_maximos)
        print(f"\nLo siento {nombre}, te quedaste sin intentos.")
        print(f"La palabra correcta era: {palabra}")

if __name__ == "__main__":
    jugar()