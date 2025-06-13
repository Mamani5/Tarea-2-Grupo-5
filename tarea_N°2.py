# Elias Amaru Carreño Arriagada 22.382.218-5
# Joaquin Alejandro Alarcon Jara 22.241.272-2
# Benedick Anthony Mamani Mamani 27.608.499-2

import matplotlib.pyplot as grafico

libros = []
personas = []

# Clase que representa un libro con sus atributos
class Libro:
    def __init__(self, isbn, titulo, especialidad, autor, editorial, edicion, año, costo):
        self.isbn = isbn
        self.titulo = titulo
        self.especialidad = especialidad
        self.autor = autor
        self.editorial = editorial
        self.edicion = edicion
        self.año = año
        self.costo = costo

    def mostrar(self):
        print(f"\nISBN: {self.isbn}")
        print(f"Titulo: {self.titulo}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Autor: {self.autor}")
        print(f"Editorial: {self.editorial}")
        print(f"Edicion: {self.edicion}")
        print(f"Año: {self.año}")
        print(f"Costo: {self.costo}")

# Clase que representa una persona con sus atributos
class Persona:
    def __init__(self, rut, nombre1, nombre2, apellido1, apellido2, telefono, email, nacimiento, monto):
        self.rut = rut
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.telefono = telefono
        self.email = email
        self.nacimiento = nacimiento
        self.monto = monto

    def mostrar(self):
        print(f"\nRut: {self.rut}")
        print(f"Primer nombre: {self.nombre1}")
        print(f"Segundo nombre: {self.nombre2}")
        print(f"Apellido paterno: {self.apellido1}")
        print(f"Apellido materno: {self.apellido2}")
        print(f"Telefono: {self.telefono}")
        print(f"Email: {self.email}")
        print(f"Fecha de nacimiento: {self.nacimiento}")
        print(f"Monto a pagar: ${self.monto}")

# Funcion que muestra el menu principal
def interfaz_menu():
    print("""\nSISTEMA DE PRESTAMOS DE LIBROS\n
1. Ingresar datos de los libros prestados
2. Ingresar datos de las personas que prestan
3. Visualizar datos de los libros prestados
4. Visualizar datos de las personas que prestan
5. Visualizar grafico del ingreso monto a pagar de las personas que prestaron libros
6. Salir del programa\n""")

# Funcion para ingresar los datos de un nuevo libro
def ingresar_libros():
    print("\nDatos del libro a prestar")
    isbn = input("ISBN: ")
    titulo = input("Titulo: ")
    especialidad = input("Especialidad: ")
    autor = input("Autor: ")
    editorial = input("Editorial: ")
    edicion = input("Edicion: ")
    
    while True:
        try:
            año = int(input("Año: "))
            if año <=0:
                print("El año debe ser positivo y mayor a 0")
            else:
                break
        except ValueError:
            print("Debes ingresar numeros")

    while True:
        try:
            costo = int(input("Costo: "))
            if costo > 3000:
                print("El costo no puede ser mayor que $3000")
            elif costo <= 0:
                print("El costo no puede ser negativo ni 0")
            else:
                break
        except ValueError:
            print("Debes ingresar un numero valido.")

    libro = Libro(isbn, titulo, especialidad, autor, editorial, edicion, año, costo)
    libros.append(libro)

# Funcion para ingresar los datos de una persona que presta libros
def ingresar_personas():
    if not libros:
        print("\nPrimero debes ingresar los datos de un libro antes de registrar una persona.")
        return
    else:
        print("\nIngresar datos de la persona que presta el libro")
        rut = input("Rut: ")
        nombre1 = input("Primer nombre: ")
        nombre2 = input("Segundo nombre: ")
        apellido1 = input("Apellido paterno: ")
        apellido2 = input("Apellido materno: ")
        while True:
            try:
                telefono = int(input("Telefono: "))
                if telefono <= 0:
                    print("El telefono no puede ser nagativo")
                else:
                    break
            except ValueError:
                print("Debes ingresar valores validos")
        email = input("Email: ")
        nacimiento = input("Fecha de nacimiento: ")
        monto = libros[-1].costo
        print(f"Monto a pagar: ${monto}")

    persona = Persona(rut, nombre1, nombre2, apellido1, apellido2, telefono, email, nacimiento, monto)
    personas.append(persona)

# Funcion para mostrar todos los libros registrados
def datos_libros():
    if not libros:
        print("\nNo hay libros registrados")
    else:
        for libro in libros:
            libro.mostrar()

# Funcion para mostrar todas las personas registradas
def datos_personas():
    if not personas:
        print("\nNo hay personas registradas")
    else:
        for persona in personas:
            persona.mostrar()

# Funcion para generar un grafico de barras del monto a pagar por persona
def visualizar_grafico():
    if not personas:
        print("\nNo hay datos de personas para mostrar el grafico.")
        return

    nombres = [f"{i.nombre1}" for i in personas]
    montos = [i.monto for i in personas]

    grafico.figure(figsize=(10, 5))
    grafico.bar(nombres, montos, color='skyblue')
    grafico.title('Monto a pagar por persona')
    grafico.xlabel('Personas')
    grafico.ylabel('Monto ($)')
    grafico.tight_layout()
    grafico.show()

# Bucle principal del programa
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
            print("El programa ha finalizado.")
            break
        else:
            print("\nLa opcion es invalida, intentelo de nuevo.")
    except ValueError:
        print("\nDebes ingresar un numero valido.")