"""Convertir a Mayusculas"""

texto = "La UAM es la peor univerisad"
print(texto)

texto_mayus = texto.upper()
print(texto_mayus)

texto_minus = input("Ingresa un texto: ").lower()
print(texto_minus)

nombre = "josh diddy"
nombre = nombre.capitalize()
print(nombre)

nombre = "lesperm james"
nombre = nombre.title()
print(nombre)

texto = "Hola Mundo Python"
texto = texto.replace("C#", "Python")
print(texto)

#Eliminar espacios en blanco

texto = "    Hola Mundo Python    "
print(texto)
texto = texto.strip()
print(texto)

#Formato de numero

numero = 10
print(numero)
numero = "{:,}".format(numero)
print(numero)

#Formato denumero decimal
numero_decimal = 1500.50
print(numero_decimal)
numero_decimal = "{:.2f}".format(numero_decimal)
print(numero_decimal)