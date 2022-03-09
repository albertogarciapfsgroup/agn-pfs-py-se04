
# Autor: Alberto García
# version: 0.0.1
# date: 09/03/2022

# import pyautogui
# sudo apt install python-tk python3-tk
# 3from tkinter import messagebox

def calculadora(operandoA, operandoB, operacion):
    if operacion == '+':
        print(operandoA + operandoB)
        # pyautogui.alert(operandoA + operandoB, 'Resultado')
        # messagebox.showinfo('Resultado', operandoA + operandoB)
    elif operacion == '-':
        print(operandoA - operandoB)
    elif operacion == '*':
        print(operandoA * operandoB)
    elif operacion == '/':
        print(operandoA / operandoB)
    elif operacion == '^':
        print(pow(operandoA, operandoB))
    elif operacion == '%':
        print(operandoA % operandoB)
    else:
        print('Operación no válida')


if __name__ == '__main__':
    operandoA = input('Por favor introduce el valor del primer operando: ')
    operandoB = input('Por favor introduce el valor del segundo operando: ')
    operacion = input('Por favor introduce la operación a realizar (+,-,*,/,^,%): ')

    calculadora(float(operandoA), float(operandoB), operacion)
