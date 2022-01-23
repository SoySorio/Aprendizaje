import alfabeto
import math

def run():
    repetir = True
    

    while repetir:
        contrasenna = input( 'Ingresa una contraseña: ')

        entropia = calcular_entropia( contrasenna )
        entropia = str( entropia )

        print( 'Entropia: ' + entropia + '\n')

        otra_contrasenna = input( '¿Quieres probar otra contraseña? (S/n): ')

        if otra_contrasenna == 'n':
            print( 'Ok. ')
            repetir = False
        
        print( '\n' )


def calcular_entropia( contrasenna ):

    tmin = False
    tmay = False
    tnum = False
    tsim = False

    opciones = 0

    for i in contrasenna: 
        if i in alfabeto.min:
            tmin = True
        elif i in alfabeto.may:
            tmay = True
        elif i in alfabeto.num:
            tnum = True
        elif i in alfabeto.sim:
            tsim = True
        
        if tmin and tmay and tnum and tsim: break

    if tmin: opciones += len( alfabeto.min )
    if tmay: opciones += len( alfabeto.may )
    if tnum: opciones += len( alfabeto.num )
    if tsim: opciones += len( alfabeto.min )

    logaritmo = math.log( opciones,2 )

    entropia = logaritmo * len( contrasenna )
    entropia = round( entropia, 1)

    return entropia
        

if __name__ == '__main__':
    run()