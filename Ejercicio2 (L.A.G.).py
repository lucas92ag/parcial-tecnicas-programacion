def TraduceMapaABool(mapa):

    #pre: Recibe una lista(mapa)
    #post: Traduce el mapa a valores booleanos

    mapaLista = []
    listaDeListas = []

    if len(mapa[0]) == len(mapa[1]) == len(mapa[2]) == len(mapa[3]):

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


def main(mapa,disparos):

    #if mapa and disp
    mapa = TraduceMapaABool(mapa)
    return devuelvePosicionNoAcertada(ChequeaAciertoEnDisparos(mapa, disparos))



print(main(["b.b..","b...b",".....","....b"], [(1,1),(3,4),(1,3),(4,5)]))





def ejercicio2(var1,var2):
    return main(var1,var2)

posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

assert (ejercicio2([],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2([""],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["      "],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["soy NO valido"],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["yo","tambien","soy","invalido"],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["b.b.","....","..bb","b.b"],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["b.b..","b...b",".....","....b"],posicionesDeDisparosDePrueba) == [(2,1),(2,5)])
assert (ejercicio2(["b..","...","..b"],[]) == [(1,1),(3,3)])

