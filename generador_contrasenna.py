import random
import alfabeto


def generar_contrasenna( numero ):
    contrasenna = ''

    for i in range( numero ):
        contrasenna += random.choice( alfabeto.todos )
    
    return contrasenna
          

def run():
    cantidad = input( '¿Cuántos caracteres quieres en tu contraseña? ' )
    cantidad = int( cantidad )

    contrasenna = generar_contrasenna( cantidad )

    print( 'Contraseña: ' + contrasenna )    


if __name__ == '__main__':
    run()