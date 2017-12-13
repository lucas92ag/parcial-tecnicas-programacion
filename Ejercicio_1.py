def rotaCaracteresDeUnaPalabra(palabra):

    lista = []
    if len(palabra) > 0 and "  " not in palabra:
        lista.append(palabra)

        for letra in range(len(palabra)-1):

            palabra = palabra[1:] + palabra[0]
            lista.append(palabra)
        return lista

    else:
        return lista
