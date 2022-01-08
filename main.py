if __name__ == '__main__':
    palabra = input("Introduzca palabra: ")
    intentosPermitidos = int(input("Introduzca intentos: "))
    numLetras = 0
    listaLetras = []
    listaLetrasIntentos = []
    listaIntentoNumeros = []
    listaIntentoPalabras = []
    listaLetrasPalabrasIntroducidas = []
    listaPalabrasCompletasIntentos = []
    listaLetrasAsteriscos = []
    ListaIntentoNumeros = []
    i = 0

    while i != intentosPermitidos:
        numLetras = len(palabra)
        adivinaNumLetras = int(
            input("Adivine el numero de letras de la palabra"))
        listaIntentoNumeros.append(adivinaNumLetras)
        if adivinaNumLetras < numLetras:
            intentosPermitidos -= 1
            print("Intento erróneo. El numero a adivinar es mayor",
                  intentosPermitidos, " intentos permitidos")
        elif adivinaNumLetras > numLetras:
            intentosPermitidos -= 1
            print("Intento erróneo. El numero a adivinar es menor",
                  intentosPermitidos, " intentos permitidos")
        else:
            print("Ha acertado el numero! la palabra tiene ",
                  numLetras, " letras")
            break
    print("Adivine letra introducida 1: ")
    print("Adivine palabra introducida 0: ")
    opciones = int(input("Elija una opción: "))
    if opciones == 1:
        listaLetras = list(palabra)
        longPalabra = len(listaLetras)
        listaLetrasAsteriscos = ['*' for _ in range(longPalabra)]
        while intentosPermitidos > 0:
            letraAdivinar = input("Adivine letra: ")
            letraCorrecta = False
            listaLetrasIntentos.append(letraAdivinar)
            for e in range(longPalabra):
                if listaLetras[e] == letraAdivinar:
                    listaLetrasAsteriscos[e] = letraAdivinar
                    letraCorrecta = True
            if letraCorrecta:
                print("Intento correcto. Existe la letra. ",
                      listaLetrasAsteriscos, ".",
                      intentosPermitidos, " intentos disponibles")
                if set(listaLetras) == set(listaLetrasAsteriscos):
                    break
            else:
                intentosPermitidos -= 1
                print("Intento erróneo. Noexiste la letra. ",
                      listaLetrasAsteriscos, ".",
                      intentosPermitidos, "intentos disponibles")
                if intentosPermitidos <= 0:
                    break
    elif opciones == 0:
        while i != intentosPermitidos:
            palabraAdivinar = input("Adivine la palabra completa")
            listaPalabrasCompletasIntentos.append(palabraAdivinar)
            for u in palabra:
                listaLetras.append(u)
            for r in palabraAdivinar:
                listaLetrasPalabrasIntroducidas.append(r)
            if set(listaLetrasPalabrasIntroducidas) == set(listaLetras):
                print("Ha acertado la palabra!!")
                break
            else:
                intentosPermitidos -= 1
                print("No ha adivinado la palabra, le quedan ",
                      intentosPermitidos, "intentos")
    print("Los intentos de numeros de letras fueron los siguientes: ",
          listaIntentoNumeros)
    print("Los intentos de letras fueron los siguientes: ",
          listaLetrasIntentos)
    print("Los intentos de palabras fueron: ",
          listaPalabrasCompletasIntentos)
