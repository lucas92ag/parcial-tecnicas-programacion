def BatallaNaval(mapa, disparos):
    #post: Traduce el mapa a valores booleanos
    lista = []
    lista_de_listas = []

    if len(mapa[0]) == len(mapa[1]) == len(mapa[2]) == len(mapa[3]):

        for cadena in mapa:

            for elemento in cadena:

                if elemento == ".":
                    lista_de_listas.append(False)

                elif elemento == "b":
                    lista_de_listas.append(True)

        if len(mapa) > 0:
            len_cadena = len(mapa[0])

            for elemento in range(0, len(lista_de_listas), len_cadena):
                lista += [lista_de_listas[elemento:elemento + len_cadena]]

            for i in range(len(disparos)):
                x = disparos[i][0] - 1
                y = disparos[i][1] - 1
                if lista[x][y] is True:
                    lista[x][y] = False
            return lista

    else:
        return lista



def devuelve_columna(lista):
    lista_posicion_columna = []
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] is True:
                tupla = (i + 1, j + 1)
                lista_posicion_columna.append(tupla)
    return lista_posicion_columna

def main(varA,varB):
    return varA(varB)

#print(devuelve_columna((BatallaNaval(["b.b..","b...b",".....","....b"], [(1,1),(3,4),(1,3),(4,5)]))))

#print(BatallaNaval(["b.b..","b...b",".....","....b"], [(1,1),(3,4),(1,3),(4,5)]))

print(main(BatallaNaval(), devuelve_columna()))


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

