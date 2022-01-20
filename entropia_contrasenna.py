def run():
    min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    may = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    sim = ['¿', '?', '¡', '!', '-', '_', ',', '.', '/', "'", '"', '$', '#', '%', '(', ')', '°', '*', '+', '{', '}', '[', ']', '^', '<', '>']

    opciones = 0
    tmin = False
    tmay = False
    tnum = False
    tsim = False


    contrasenna = input( 'Ingresa una contraseña ' )

    for i in contrasenna: 
        if i in min:
            tmin = True
        elif i in may:
            tmay = True
        elif i in num:
            tnum = True
        elif i in sim:
            tsim = True
        
        if tmin and tmay and tnum and tsim: break

    if tmin: opciones += len( min )
    if tmay: opciones += len( may )
    if tnum: opciones += len( num )
    if taim: opciones += len( sim )

    print(opciones)
        


"""    longitud = len(minusculas) + len(mayusculas) + len(numeros) + len(simbolos)""" 


if __name__ == '__main__':
    run()