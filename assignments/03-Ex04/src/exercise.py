"""
El dueño de una papelería necesita un programa para calcular el pago de cada uno de sus clientes.

El programa debe preguntar

Precio del artículo 
Cantidad a comprar 
Desea comprar otro artículo (S/N)
si el usuario teclea S se deberá preguntar de nuevo el precio del artículo y la cantidad a comprar;

cuando el usuario teclea N se deberá mostrar los siguientes mensajes:

Número de artículos comprados  =   ______
Total a pagar =    _______
"""

def main():
    total = 0
    cantidad_articulos = 0

    respuesta = 'S'

    while respuesta == 'S':
        precio = float(input("Precio del artículo?"))
        cantidad = int(input("Cantidad a comprar?"))

        print(f"El total del artículo es ${precio * cantidad:.0f}")
    
        total += precio * cantidad
        cantidad_articulos += cantidad

        respuesta = input("Desea comprar otro artículo (S/N)?").upper()
        
    print(f'Número de artículos comprados  =   {cantidad_articulos}')
    print(f'Total a pagar =    {total:.0f}')

if __name__=='__main__':
    main()
