nombre = "Mike"
apellido = "Goat"

nombre_completo = nombre + " " + apellido
print(nombre_completo)

nombre_C = f"{nombre} {apellido}"
print(nombre_C)

nombre_completo = " ".join([nombre, apellido])
print(nombre_completo)

#Lista y concatenar

lista = []
lista.append(nombre)
lista.append(apellido)
nombre_completo = " ".join(lista)
print(nombre_completo) 
