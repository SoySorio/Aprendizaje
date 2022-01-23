import alfabeto
import math

def run():
    repetir = True
    
    print( alfabeto.MIN )

    """while repetir:
        contrasenna = input( 'Ingresa una contraseña: ')

        entropia = calcular_entropia( contrasenna )
        entropia = str( entropia )

        print( 'Entropia: ' + entropia + '\n')

        otra_contrasenna = input( '¿Quieres probar otra contraseña? (S/n): ')

        if otra_contrasenna == 'n':
            print( 'Ok. ')
            repetir = False
        
        print( '\n' )"""


def calcular_entropia( contrasenna ):
    MIN = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    MAY = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    NUM = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    SIM = ['¿', '?', '¡', '!', '-', '_', ',', '.', '/', "'", '"', '$', '#', '%', '(', ')', '°', '*', '+', '{', '}', '[', ']', '^', '<', '>']

    opciones = 0
    tmin = False
    tmay = False
    tnum = False
    tsim = False

    for i in contrasenna: 
        if i in MIN:
            tmin = True
        elif i in MAY:
            tmay = True
        elif i in NUM:
            tnum = True
        elif i in SIM:
            tsim = True
        
        if tmin and tmay and tnum and tsim: break

    if tmin: opciones += len( MIN )
    if tmay: opciones += len( MAY )
    if tnum: opciones += len( NUM )
    if tsim: opciones += len( SIM )

    logaritmo = math.log( opciones,2 )

    entropia = logaritmo * len( contrasenna )
    entropia = round( entropia, 1)

    return entropia
        

if __name__ == '__main__':
    run()