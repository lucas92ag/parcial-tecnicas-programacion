def esMapaValido(mapa):

    if len(mapa) < 1 or type(mapa) != list:
        return False

    for j in range(len(mapa)):

        if len(mapa[0]) != len(mapa[j]):
            return False

    for cadena in mapa:

        centinela = ""
        if len(cadena) <= 0 or " " in cadena:
            centinela += "*"

        if "b" and "." not in cadena:
            centinela += "*"

        if "*" in centinela:
            return False

    return True




def TraduceMapaABool(mapa):

    mapaLista = []
    listaDeListas = []

    for cadena in mapa:

        for elemento in cadena:

            if elemento == ".":
                mapaLista.append(False)

            elif elemento == "b":
                mapaLista.append(True)

    if len(mapa) > 0:
        lenCadena = len(mapa[0])

        for elemento in range(0, len(mapaLista), lenCadena):
            listaDeListas += [mapaLista[elemento:elemento + lenCadena]]

        return listaDeListas

    else:
        return listaDeListas


def ChequeaAciertoEnDisparos(mapa, disparos):

    #pre: Recibe el mapa (lista de listas en booleanos) y disparos (coordenadas expresadas en lista de tuplas)
    #post: Devuelve el mapa reemplazando los True acertados por False.

    for i in range(len(disparos)):

        x = disparos[i][0] - 1
        y = disparos[i][1] - 1

        if mapa[x][y] is True:

            mapa[x][y] = False

    return mapa


def devuelvePosicionNoAcertada(mapa):

    #pre: Recibe el mapa (lista de listas en booleanos).
    #post: Devuelve una lista de tuplas con las posiciones que no se acertaron.

    listaPosicionColumna = []

    for i in range(len(mapa)):

        for j in range(len(mapa[i])):

            if mapa[i][j] is True:

                tupla = (i + 1, j + 1)
                listaPosicionColumna.append(tupla)

    return listaPosicionColumna


def devuelveCoordenadasDeBarcosNoHundidos(mapa, disparos):

    if esMapaValido(mapa):
        mapa = TraduceMapaABool(mapa)
        return devuelvePosicionNoAcertada(ChequeaAciertoEnDisparos(mapa, disparos))

    return []



