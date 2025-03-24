#Listas 
#1. Pila
#2. Colas -Filas

#ueps
#LIFO
#FIFO
#PEPS

#Pila

stack = []

def push(val):
    if len(stack) < 5:
        stack.append(val)
    else:
        print("Stack overflow")

def pop():
    if len(stack) > 0:
        return stack.pop()
    else: 
        print("Stack underflow")

def menu():
    print("1. Push")
    print("2. Pop")
    print("3. Exit")
    return int(input("Escoge una opcion: "))

while True:
    option = menu()
    if option == 1:
        push(int(input("Ingresa un numero: ")))
    elif option == 2:
        print(pop())
    elif option == 3:
        break
    else:
        print("Opcion invalida")

print("odio esta carrera ")
