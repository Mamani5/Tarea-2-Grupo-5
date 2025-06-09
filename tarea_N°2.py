# Elias Amaru Carreño Arriagada 22.382.218-5
# Joaquin Alejandro Alarcon Jara 22.241.272-2
# Benedick Anthony Mamani Mamani 27.608.499-2

def interfaz_menu():
    print("""\nSISTEMA DE PRESTAMOS DE LIBROS\n
1. Ingresar datos de los libros prestados
2. Ingresar datos de las personas que prestan
3. Visualizar datos de los libros prestados
4. Visualizar datos de las personas que prestan
5. Visualizar gráfico del ingreso monto a pagar de las personas que prestaron libros
6. Salir del programa\n""")
    pass

def ingresar_libros():
    pass

def ingresar_personas():
    pass

def datos_libros():
    pass

def datos_personas():
    pass

def visualizar_grafico():
    pass

while True:
    try:
        interfaz_menu()
        opcion = int(input("Seleccione su opcion: "))
        
        if opcion == 1:
            ingresar_libros()
        elif opcion == 2:
            ingresar_personas()
        elif opcion == 3:
            datos_libros()
        elif opcion == 4:
            datos_personas()
        elif opcion == 5:
            visualizar_grafico()
        elif opcion == 6:
            print("El codigo finalizo")
            break
        else:
            print("\nLa Opcion es Invalida, intentelo denuevo.")
    except ValueError:
        print("\nDebes ingresas un numero valido.")