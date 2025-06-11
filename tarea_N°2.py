# Elias Amaru Carreño Arriagada 22.382.218-5
# Joaquin Alejandro Alarcon Jara 22.241.272-2
# Benedick Anthony Mamani Mamani 27.608.499-2

import matplotlib.pyplot as plt

libros = []
personas = []

class Libro:
    def __init__(self, isbn, titulo, especialidad, autor, editorial, edicion, anio, costo):
        self.isbn = isbn
        self.titulo = titulo
        self.especialidad = especialidad
        self.autor = autor
        self.editorial = editorial
        self.edicion = edicion
        self.anio = anio
        self.costo = costo

    def mostrar(self):
        print(f"\nISBN: {self.isbn}")
        print(f"Titulo: {self.titulo}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Autor: {self.autor}")
        print(f"Editorial: {self.editorial}")
        print(f"Edicion: {self.edicion}")
        print(f"Anio: {self.anio}")
        print(f"Costo: {self.costo}")

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

def interfaz_menu():
    print("""\nSISTEMA DE PRESTAMOS DE LIBROS\n
1. Ingresar datos de los libros prestados
2. Ingresar datos de las personas que prestan
3. Visualizar datos de los libros prestados
4. Visualizar datos de las personas que prestan
5. Visualizar grafico del ingreso monto a pagar de las personas que prestaron libros
6. Salir del programa\n""")

def ingresar_libros():
    print("\nDatos del libro a prestar")
    isbn = input("ISBN: ")
    titulo = input("Titulo: ")
    especialidad = input("Especialidad: ")
    autor = input("Autor: ")
    editorial = input("Editorial: ")
    edicion = input("Edicion: ")
    anio = input("Anio: ")

    while True:
        try:
            costo = int(input("Costo: "))
            if costo > 3000:
                print("Advertencia: El costo no puede exceder de $3000.")
            else:
                break
        except ValueError:
            print("Debes ingresar un numero valido.")

    libro = Libro(isbn, titulo, especialidad, autor, editorial, edicion, anio, costo)
    libros.append(libro)

def ingresar_personas():
    print("\nIngresar datos de la persona que presta el libro")
    rut = input("Rut: ")
    nombre1 = input("Primer nombre: ")
    nombre2 = input("Segundo nombre: ")
    apellido1 = input("Apellido paterno: ")
    apellido2 = input("Apellido materno: ")
    telefono = input("Telefono: ")
    email = input("Email: ")
    nacimiento = input("Fecha de nacimiento: ")

    if libros:
        monto = libros[-1].costo
        print(f"Monto a pagar: ${monto}")
    else:
        monto = 0
        print("No hay libros registrados, el monto sera $0")

    persona = Persona(rut, nombre1, nombre2, apellido1, apellido2, telefono, email, nacimiento, monto)
    personas.append(persona)

def datos_libros():
    if not libros:
        print("\nNo hay libros registrados")
    else:
        for libro in libros:
            libro.mostrar()

def datos_personas():
    if not personas:
        print("\nNo hay personas registradas")
    else:
        for persona in personas:
            persona.mostrar()

def visualizar_grafico():
    if not personas:
        print("\nNo hay datos de personas para mostrar el grafico.")
        return

    nombres = [f"{p.nombre1} {p.apellido1}" for p in personas]
    montos = [p.monto for p in personas]

    plt.figure(figsize=(10, 5))
    plt.bar(nombres, montos, color='skyblue')
    plt.title('Monto a pagar por persona')
    plt.xlabel('Personas')
    plt.ylabel('Monto ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

while True:
    try:
        interfaz_menu()
        opcion = int(input("Seleccione su opcion: "))

        if opcion == 1:
            ingresar_libros()
        elif opcion == 2:
            if not libros:
                print("\nPrimero debes ingresar los datos de un libro antes de registrar una persona.")
            else:
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
