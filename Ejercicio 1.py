def rotaCaracteresDeUnaCadena(cadena):
    lista = []
    if type(cadena) == str and cadena != "" and cadena != "     ":
        lista.append(cadena)
        for letra in range(len(cadena)-1):
            cadena = cadena[1:] + cadena[0]
            lista.append(cadena)
        return lista
    else:
        return lista

print(rotaCaracteresDeUnaCadena("Arnol"))


def ejercicio1(var1):
    return rotaCaracteresDeUnaCadena(var1)

assert (ejercicio1("") == [])
assert (ejercicio1("     ") == [])
assert (ejercicio1("a") == ['a'])
assert (ejercicio1("ab") == ['ab','ba'])
assert (ejercicio1("paz") == ['paz','azp','zpa'])
assert (ejercicio1("so l") == ['so l','o ls',' lso','lso '])
assert (ejercicio1("rotar") == ['rotar','otarr','tarro','arrot','rrota'])