
# Autor: Alberto García
# version: 0.0.1
# date: 09/03/2022


def calculaPrecioConIVA(precio):
    precio = float(precio)
    precioConIVA = precio + precio * float(valorIVA) / 100
    print('El precio con IVA es de', precioConIVA)


contadorVentas = 0
numeroVentas = 0
precioTotal = 0

if __name__ == '__main__':
    numeroVentas = input('Por favor introduce el número de ventas:')
    numeroVentas = int(numeroVentas)

    while int(contadorVentas) < int(numeroVentas):
        precioVenta = input('Por favor introduce el importe de la venta:')
        precioTotal += float(precioVenta)
        contadorVentas += 1

    print('El precio total de las ventas es de', precioTotal, 'euros')