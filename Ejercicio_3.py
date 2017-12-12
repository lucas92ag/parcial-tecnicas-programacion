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

def determinaCampeon(dict):

    equipos = sorted(list(dict.keys()))
    return equipos[0]

def ganadorDelTorneo(dict):

    maximum = max(dict, key=dict.get)

    return maximum

def main(list):
    if len(list) < 1:
        return ""
    tabla = tableroDePuntuacion(list)
    if chequeaIgualdadDePuntos(tabla) == False:
        return determinaCampeon(tabla)

    return ganadorDelTorneo(tabla)




#print(ganadorDelTorneo(tableroDePuntuacion([("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)])))

#print(main([("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]))

#print(ganadorDelTorneo(tableroDePuntuacion([("a", 1, "b", 0), ("a", 1, "b", 0), ("c", 3, "a", 2)])))






def ejercicio3(var1):
    return main(var1)


assert (ejercicio3([]) == "")
assert (ejercicio3([("a", 1, "b", 0)]) == "a")
assert (ejercicio3([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]) == "c")
assert (ejercicio3([("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]) == "Almagro")
assert (ejercicio3([("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]) == "a")
