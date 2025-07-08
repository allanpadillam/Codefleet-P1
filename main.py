from wordbank import obtener_palabra_aleatoria
from pr_console import (
    solicitar_nombre_jugador,
    mostrar_categoria,
    mostrar_intentos_restantes,
    mostrar_felicitaciones,
    mostrar_palabra_correcta
)
from draw import mostrar_dibujo

def mostrar_progreso(palabra, letras_adivinadas):
    """
    Muestra el estado actual de la palabra con guiones bajos y letras acertadas.
    """
    progreso = ' '.join([letra if letra in letras_adivinadas else '_' for letra in palabra])
    print("\n Progreso: ", progreso)
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

        intento = input("\n Ingresa una letra: ").strip().upper()

        if len(intento) != 1 or not intento.isalpha():
            print(" Solo puedes ingresar una letra válida.")
            continue

        if intento in letras_adivinadas:
            print("Ya intentaste esa letra. Prueba otra.")
            continue

        letras_adivinadas.add(intento)

        if intento not in palabra_secreta:
            errores += 1
            print(" ¡Letra incorrecta!")

    else:
        mostrar_dibujo(longitud_palabra, errores)
        mostrar_palabra_correcta(nombre, palabra_secreta)

if __name__ == "__main__":
    jugar_ahorcado()
