
# Autor: Alberto García
# version: 0.0.1
# date: 09/03/2022

def cualEsMayor(valorA, valorB):
    if valorA > valorB:
        print('El primer valor es mayor que el segundo')
    elif valorB > valorA:
        print('El segundo valor es mayor que el primero')
    else:
        print('Los dos valores son iguales')


valorA = 5
valorB = 10

if __name__ == '__main__':
    cualEsMayor(valorA, valorB)
    cualEsMayor(valorB, valorA)
    cualEsMayor(valorA, valorA)
    cualEsMayor(valorB, valorB)
