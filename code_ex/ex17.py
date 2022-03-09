
# Autor: Alberto García
# version: 0.0.1
# date: 09/03/2022


def compruebaPassword(passwordUsu):
    if passwordUsu == password:
        return True
    else:
        return False


password = 'admin'
maxIntentos = 3
numIntentos = 1

if __name__ == '__main__':
    while numIntentos <= maxIntentos:
        passwordUsu = input('Por favor introduce la contraseña: ')
        if compruebaPassword(passwordUsu):
            print('Bienvenido')
            break;
        else:
            numIntentos += 1

    if numIntentos > maxIntentos:
        print('Número máximo de intentos superado')
