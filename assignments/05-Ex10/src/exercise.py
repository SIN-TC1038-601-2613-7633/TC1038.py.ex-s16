"""
Escribe un programa que pida al usuario un número y valide que se encuentre entre 1 y 100. 
Es decir, si el número tecleado no cae en el rango, el programa lo debe volver a pedir tantas veces como el número no esté en el rango. 
Cuando el número esté en el rango deberá mandar un mensaje que indique que el número es correcto.
"""

def main():
    numero = int(input())

    while numero < 1 or numero > 100:
        print("Error, vuelve a teclear")
        numero = int(input())

    print("Número correcto")

if __name__=='__main__':
    main()
