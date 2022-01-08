def test_es_palabra():
    palabra = "hola"
    assert isinstance(palabra, str)


def test_es_numero():
    numintento = 2
    assert float(numintento)


def test_numintentos_es_mayor_a_0():
    numintentos = 10
    assert numintentos > 0


def test_adivinar_num_letras():
    palabra = "hola"
    num_letras = len(palabra)
    assert palabra > num_letras


def test_letra_adivinada():
    palabra = "hola"
    letraadivinar = "h"
    listaLetras = list(palabra)
    longPalabra = len(listaLetras)
    acierto = False
    for e in range(longPalabra):
        if listaLetras[e] == letraadivinar:
            acierto = True
    assert acierto


def test_palabra_adivinada():
    palabra = "hola"
    palabraAdivinar = "hola"
    listaLetras = []
    listaLetrasPalabrasIntroducidas = []
    acierto = False
    for u in palabra:
        listaLetras.append(u)
    for r in palabraAdivinar:
        listaLetrasPalabrasIntroducidas.append(r)
    if set(listaLetrasPalabrasIntroducidas) == set(listaLetras):
        acierto = True
    assert acierto


def test_palabra_comparar_es_palabra():
    palabracomparar = "hola"
    assert isinstance(palabracomparar, str)


def test_num_opcion_juego_es_numero():
    numopcion = 2
    assert float(numopcion)


def test_letra_no_adivinada():
    palabra = "hola"
    letraadivinar = "n"
    listaLetras = list(palabra)
    longPalabra = len(listaLetras)
    acierto = False
    for e in range(longPalabra):
        if listaLetras[e] == letraadivinar:
            acierto = False
        else:
            acierto = True, "La letra no esta en la palabra"
    assert acierto


def test_palabra_no_adivinada():
    palabra = "hola"
    palabraAdivinar = "pepe"
    listaLetras = []
    listaLetrasPalabrasIntroducidas = []
    acierto = False
    for u in palabra:
        listaLetras.append(u)
    for r in palabraAdivinar:
        listaLetrasPalabrasIntroducidas.append(r)
    if set(listaLetrasPalabrasIntroducidas) == set(listaLetras):
        acierto = False
    else:
        acierto = True
    assert acierto


def test_comprueba_tipo_juego():
    opcion = 1
    assert opcion == 1 | opcion == 0
