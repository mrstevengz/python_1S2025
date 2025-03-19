cont = 1
number = int(input("Ingresa un numero: "))
print(f"Tabla de multiplicar del {number}")
print('='*13)
while cont <=12:
    print (f"{cont} * {number} * = {cont * number}")
    cont += 1
print("="*13)