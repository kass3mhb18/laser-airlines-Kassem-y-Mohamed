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
        print("Primera Clase")
        print("Segunda Clase")
        print("Tercera Clase")
        clase = input("Ingrese opción: ")
        
        limpiar_consola()
        print("Seleccione el tipo de boleto:")
        print("Nacional")
        print("Internacional")
        tipo_boleto = input("Ingrese opción (N/I): ")
        
        limpiar_consola()
        if tipo_boleto.lower() == "n":
            print("|========================== Vuelos Nacionales Disponibles ==============================|")
            print("| Origen         | Destino         | Precio | Origen         | Destino         | Precio |")
            print("|----------------|-----------------|--------|----------------|-----------------|--------|")
            print("| Porlamar       | Caracas         |  50$   | Caracas        | Porlamar        |  50$   |")
            print("| Puerto Ordaz   | Caracas         |  45$   | Caracas        | Puerto Ordaz    |  45$   |")
            print("| Maracaibo      | Caracas         |  80$   | Caracas        | Maracaibo       |  80$   |")
            print("| El Vigia       | Caracas         |  75$   | Caracas        | El Vigia        |  75$   |")
            print("| Barcelona      | Caracas         |  30$   | Caracas        | Barcelona       |  30$   |")
            print("| La Fria        | Caracas         |  60$   | Caracas        | La Fria         |  60$   |")
            print("|=======================================================================================|")
            
            while True:
                origen = input("Ingrese el origen: ")
                destino = input("Ingrese el destino: ")
                if origen != destino and origen in ["Porlamar", "Puerto Ordaz", "Maracaibo", "El Vigia", "Barcelona", "La Fria"] and destino == "Caracas":
                    break
                elif destino != origen and destino in ["Porlamar", "Puerto Ordaz", "Maracaibo", "El Vigia", "Barcelona", "La Fria"] and origen == "Caracas":
                    break
                else:
                    print("Origen o destino inválido, o son iguales. Intente de nuevo.")
        else:
            limpiar_consola()
            print("Vuelos internacionales disponibles:")
            print("Bogota - Caracas")
            print("Curazao - Caracas")
            print("Santo Domingo - Caracas")
            print("La Romana - Caracas")
            
            while True:
                origen = input("Ingrese el origen: ")
                destino = input("Ingrese el destino: ")
                if origen != destino and origen in ["Bogota", "Curazao", "Santo Domingo", "La Romana"] and destino == "Caracas":
                    break
                elif destino != origen and destino in ["Bogota", "Curazao", "Santo Domingo", "La Romana"] and origen == "Caracas":
                    break
                else:
                    print("Origen o destino inválido, o son iguales. Intente de nuevo.")
        
        limpiar_consola()
        servicios = input("¿Requiere servicios adicionales? (S/N): ")
        
        print("Boleto registrado con éxito. Presiona Enter para continuar") 
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
