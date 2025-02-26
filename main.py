import os
import platform

def limpiar_consola():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def comprar_boleto():
    limpiar_consola()
    cantidad = int(input("Ingrese la cantidad de boletos a comprar: "))
    
    for i in range(cantidad):
        print(f"\nBoleto {i+1}:")
        nombre = input("Nombre del pasajero: ")
        cedula = input("Cédula de identidad (V/E): ")
        edad = int(input("Edad del pasajero: "))

        limpiar_consola()
        print("Seleccione la clase de boleto:")
        print("1. Primera Clase")
        print("2. Segunda Clase")
        print("3. Tercera Clase")
        clase = input("Ingrese opción: ")
        
        limpiar_consola()
        print("Seleccione el tipo de boleto:")
        print("N. Nacional")
        print("I. Internacional")
        tipo_boleto = input("Ingrese opción (N/I): ")
        
        limpiar_consola()
        if tipo_boleto.upper() == "N":
            print("Seleccione el origen:")
            print("1. Porlamar")
            print("2. Puerto Ordaz")
            print("3. Maracaibo")
            print("4. El Vigia")
            print("5. Barcelona")
            print("6. La Fria")
            origen = input("Ingrese número del origen: ")
            
            print("Seleccione el destino:")
            destino = input("Ingrese número del destino: ")
        else:
            limpiar_consola()
            print("Seleccione el origen:")
            print("1. Bogota")
            print("2. Curazao")
            print("3. Santo Domingo")
            print("4. La Romana")
            origen = input("Ingrese número del origen: ")
            
            print("Seleccione el destino:")
            destino = input("Ingrese número del destino: ")
        
        limpiar_consola()
        servicios = input("¿Requiere servicios adicionales? (S/N): ")
        
        print("Boleto registrado con éxito.")
    
    print("\nPresiona Enter para continuar...")
    input("")

def mostrar_menu():
    while True:
        limpiar_consola()
        print("|====  Aerolínea LASER ====|")
        print("                            ")
        print("|==== Menú de Opciones ====|")
        print("|1. Comprar boleto         |")
        print("|2. Ver panel de control   |")
        print("|3. Salir                  |")
        print("|==========================|")
        print("\nSeleccione una opción:")
        opcion = input("→ ")
        
        if opcion == "1":
            comprar_boleto()
        elif opcion == "2":
            limpiar_consola()
            print("Función ver panel de control aún no implementada.")
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        
        print("\nPresiona Enter para continuar...")
        input("")

mostrar_menu()
