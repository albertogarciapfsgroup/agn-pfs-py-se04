
# Autor: Alberto García
# version: 0.0.1
# date: 09/03/2022


def compruebaDiaLaboral(diaSemana):
    if diaSemana == 'lunes' or diaSemana == 'martes' or diaSemana == 'miercoles' or diaSemana == 'jueves' or diaSemana == 'viernes':
        print('El día es laboral')
    elif diaSemana == 'sabado' or diaSemana == 'domingo':
        print('El día no es laboral')
    else:
        print('El día no es válido')

if __name__ == '__main__':
    diaSemana = input('Por favor introduce un día de la semana: ')
    compruebaDiaLaboral(diaSemana.lower())
