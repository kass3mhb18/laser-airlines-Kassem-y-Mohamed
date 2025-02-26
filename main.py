import os

def mostrar_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nMenú de Opciones:")
        print("1. Comprar boleto")
        print("2. Ver panel de control")
        print("3. Salir")
        print("\nSeleccione una opción:")
        opcion = input("→ ")
        
        if opcion == "1":
            print("Función comprar boleto aún no implementada.")
        elif opcion == "2":
            print("Función ver panel de control aún no implementada.")
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        
        print("\nPresiona Enter para continuar...")
        input("")

mostrar_menu()