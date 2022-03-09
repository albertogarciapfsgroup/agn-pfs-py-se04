
# Autor: Alberto García
# version: 0.0.1
# date: 09/03/2022


def muestraCienPrimerosNumerosWhile():
    contador = 1
    while int(contador) >= 1 and int(contador) <= 100:
        print(contador)
        contador += 1


if __name__ == '__main__':
    muestraCienPrimerosNumerosWhile()
