#Almacenar 10 numeros

list_numbers = list()

def addnumber():
    for i in range(10):
        number = int(input(f"{i+1} de 10 | Ingrese un numero inpar mayor a 18: "))
        if number % 2 != 0 and number > 18:
            list_numbers.append(number)
        else:
            print("Ingrese un numero valido")
    

addnumber()
print(list_numbers)





 

