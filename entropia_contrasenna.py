def run():
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    simbolos = ['¿', '?', '¡', '!', '-', '_', ',', '.', '/', "'", '"', '$', '#', '%', '(', ')', '°', '´', '*', '+', '{', '}', '[', ']', '^', '<', '>']

    longitud = len(minusculas) + len(mayusculas) + len(numeros) + len(simbolos)

    print(longitud)


if __name__ == '__main__':
    run()