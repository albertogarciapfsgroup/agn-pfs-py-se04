
# Autor: Alberto García
# version: 0.0.1
# date: 09/03/2022

import math


def calculaAreaCirculo(radio):
    if radio:
        radio = float(radio)
        resultado = math.pi * pow(radio, 2)
        print('El área del círculo con radio', radio, 'es', resultado)


if __name__ == '__main__':
    radio = input('Por favor introduce el valor del radio:')
    calculaAreaCirculo(radio)
