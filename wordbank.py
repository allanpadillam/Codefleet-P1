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
