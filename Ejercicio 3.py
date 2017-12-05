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

def ganadorDelTorneo(dict):

    for key in dict:
        if dict[key] ==

    maximum = max(dict, key=dict.get)

    return maximum







print(ganadorDelTorneo(tableroDePuntuacion([("Boca", 0, "Belgrano", 0), ("Boca", 0, "Almagro", 1), ("Almagro", 1, "Belgrano", 2)])))

print(tableroDePuntuacion([("Boca", 0, "Belgrano", 1), ("Boca", 0, "Almagro", 1), ("Almagro", 1, "Belgrano", 2)]))

print(tableroDePuntuacion([("a", 1, "b", 0), ("a", 1, "b", 0), ("c", 1, "a", 2)]))






"""def ejercicio3(var1):
    return suFuncion(var1)


assert (ejercicio3([]) == "")
assert (ejercicio3([("a", 1, "b", 0)]) == "a")
assert (ejercicio3([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]) == "c")
assert (ejercicio3([("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]) == "Almagro")
assert (ejercicio3([("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]) == "a")"""
