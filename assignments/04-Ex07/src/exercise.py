"""
Programa que solicite números enteros hasta que el número ingresado sea un número negativo.

El programa deberá de mostrar cuántos números ingresados fueron pares
"""

def main():
    numeros_pares = 0
    numero = int(input())

    while numero >= 0:
        if numero % 2 == 0:
            numeros_pares += 1
        numero = int(input())

    print(f"Total de pares= {numeros_pares}")

if __name__=='__main__':
    main()
