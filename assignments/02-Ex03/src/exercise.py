"""
Programa que lee la clave del artículo que va a comprar (nota que es letra mayúscula) o X 
si ya no quiere comprar más artículos. El programa debe capturar el precio correspondiente
a cada artículo pedido, el programa debe repetirse mientras el usuario no teclee la clave X, 
cuando el usuario teclee la clave X el programa debe mostrar en la pantalla el total 
de la compra del cliente.
"""

def main():
    total = 0
    clave = input().upper()

    while clave != 'X':
        precio = float(input())

        total += precio

        clave = input().upper()
    print(f'{total:.0f}')

if __name__=='__main__':
    main()
