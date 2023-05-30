def get_ascii(caracter):

    return ord(caracter)

def get_binary(ascii_code):

    binario = ""
    while ascii_code > 0:
        residuo = ascii_code % 2
        binario = str(residuo) + binario
        ascii_code = ascii_code // 2
    return binario

def get_result(palabra):

    resultado = []
    for caracter in palabra:
        ascii_code = get_ascii(caracter)
        binario = get_binary(ascii_code)
        resultado.append(("El caracter es:", caracter,", El código Ascii es: ", ascii_code,", El binario es:", binario))
    return resultado