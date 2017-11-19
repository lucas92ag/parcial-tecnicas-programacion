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

print(rotaCaracteresDeUnaPalabra("Lucas"))


def ejercicio1(var1):
    return rotaCaracteresDeUnaPalabra(var1)

assert (ejercicio1("") == [])
assert (ejercicio1("     ") == [])
assert (ejercicio1("a") == ['a'])
assert (ejercicio1("ab") == ['ab','ba'])
assert (ejercicio1("paz") == ['paz','azp','zpa'])
assert (ejercicio1("so l") == ['so l','o ls',' lso','lso '])
assert (ejercicio1("rotar") == ['rotar','otarr','tarro','arrot','rrota'])