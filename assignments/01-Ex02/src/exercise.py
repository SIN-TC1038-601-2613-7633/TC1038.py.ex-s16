"""
Programa que sume los números enteros (positivos y negativos) que el usuario teclee y se detenga hasta que el usuario teclee un cero.
"""

def main():

    total = 0
    
    num = int(input())
    while num != 0:
        total += num
        num = int(input())
        
    print(total)

if __name__=='__main__':
    main()
