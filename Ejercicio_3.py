def tableroDePuntuacion(lista):

    tablero = {}

    for tupla in lista:

        if tupla[1] > tupla[3]:

            if tupla[0] in tablero:
                tablero[tupla[0]] += 2
            else:
                tablero[tupla[0]] = 2

        if tupla[1] < tupla[3]:

            if tupla[2] in tablero:
                tablero[tupla[2]] += 2
            else:
                tablero[tupla[2]] = 2

        if tupla[1] == tupla[3]:

            if tupla[0] in tablero:
                tablero[tupla[0]] += 1
            else:
                tablero[tupla[0]] = 1

            if tupla[2] in tablero:
                tablero[tupla[2]] += 1

            else:
                tablero[tupla[2]] = 1

    return tablero


def chequeaIgualdadDePuntos(dict):

    resultado = None
    point = list(dict.values())
    point1 = point[0]
    for score in point[1:]:
        if score == point1:
            resultado = False
        else:
            resultado = True
    return resultado


def determinaCampeonAlfabeticamente(dict):

    equipos = sorted(list(dict.keys()))
    return equipos[0]


def maximoPuntajeDelTorneo(dict):

    maximum = max(dict, key=dict.get)

    return maximum


def ganadorDelTorneo(list):
    if len(list) < 1:
        return ""
    tabla = tableroDePuntuacion(list)
    if chequeaIgualdadDePuntos(tabla) is False:
        return determinaCampeonAlfabeticamente(tabla)

    return maximoPuntajeDelTorneo(tabla)





