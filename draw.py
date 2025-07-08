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
    
    indice_dibujo = min(errores, max_dibujos - 1)

    print(DIBUJOS[indice_dibujo])