#Agregar los nombres de x cantidad de estudiantes

list_students = list()
def add_student():
    student = input("Ingrese el nombre de estudiante: Ste")
    list_students.append(student)

def show_students():
    print("Lista de estudiantes: ")
    for student in list_students:
        print(student)

while True:
    add_student()
    show_students()
    if input("Deseas agregar a otro estudiante? (s/n): ").lower() != "s":
        break

print("Gracias por usar el programa")
