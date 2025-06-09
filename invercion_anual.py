"""Escribir un programa que le prefunte al usuario una cantidad a invertir, el interes anual y el de años, y muestre por pantalla 
el capital obtenido en la inversion cada año que dura la invercion. Finalmente muestre el capital total de su inversion inicial"""

invercion = float(input("Ingresa la cantidad de dinero que quiera invertir: "))
interes_anual = float(input("Ingrese cuanto interes anual desea (solo coloque el numero no el %): "))
años = int(input("Ingrese el numero de años a invertir: "))
i = 0
capital = invercion

while i <= años:   
    capital += capital * (interes_anual / 100)
    i = i + 1
print(f"Invercion inicial: {invercion}, con un interes anual de {interes_anual}% y por ${años} años")
(print(f"El capital final es {capital}"))