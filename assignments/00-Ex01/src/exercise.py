"""
Programa que lea un número positivo n, e imprima todos los números en orden desde el 1 hasta n. Cada uno de los números debe ser impreso en una linea por separado.
"""

def main():
    n = int(input())

    i = 1
    while i <= n:
        print(i)
        i += 1

if __name__=='__main__':
    main()
