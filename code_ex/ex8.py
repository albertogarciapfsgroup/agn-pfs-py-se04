
# Autor: Alberto García
# version: 0.0.1
# date: 09/03/2022

def devuelveMensajeBienvenida(nombre):
    if nombre:
        print('Bienvenido', nombre)


if __name__ == '__main__':
    nombre = input('Por favor dime tu nombre:')
    devuelveMensajeBienvenida(nombre)
