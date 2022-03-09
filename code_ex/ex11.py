
# Autor: Alberto García
# version: 0.0.1
# date: 09/03/2022


def calculaPrecioConIVA(precio):
    precio = float(precio)
    precioConIVA = precio + precio * float(valorIVA) / 100
    print('El precio con IVA es de', precioConIVA)


valorIVA = 21

if __name__ == '__main__':
    precio = input('Por favor introduce el precio del producto:')
    calculaPrecioConIVA(precio)
