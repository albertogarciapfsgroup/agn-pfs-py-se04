
# Autor: Alberto García
# version: 0.0.1
# date: 09/03/2022


def muestraCienPrimerosNumerosDivisiblesDosTres():
    for contador in range(1, 101):
        if contador % 2 == 0 or contador % 3 == 0:
            print(contador)
        

if __name__ == '__main__':
    muestraCienPrimerosNumerosDivisiblesDosTres()
