
# Autor: Alberto García
# version: 0.0.1
# date: 09/03/2022


def esDivisibleEntreDos(numero):
    if int(numero) % 2 == 0:
        print('El número', numero, 'es divisible entre 2')
    else:
        print('El número', numero, 'no es divisible entre 2')


if __name__ == '__main__':
    numero = input('Por favor introduce el número:')
    esDivisibleEntreDos(numero)
