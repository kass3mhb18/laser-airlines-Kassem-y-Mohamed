import os
import platform

def limpiar_consola():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

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
            limpiar_consola()
            print("Función comprar boleto aún no implementada.")
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