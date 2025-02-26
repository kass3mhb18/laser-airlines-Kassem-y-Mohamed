import os
import platform

def limpiar_consola():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def calcular_precio(edad, clase, tipo_boleto, origen, destino, es_vuelta=False):
    # Precios de boletos por vuelo (ida y vuelta)
    precios_nacionales = {
        "Porlamar": 50, "Puerto Ordaz": 45, "Maracaibo": 80,
        "El Vigia": 75, "Barcelona": 30, "La Fria": 60
    }
    precios_internacionales = {
        "Bogota": 499, "Curazao": 400, "Santo Domingo": 700, "La Romana": 650
    }

    if tipo_boleto == "n":
        # Obtener el precio del vuelo nacional según origen y destino
        if origen in precios_nacionales and destino == "Caracas":
            precio = precios_nacionales[origen]
        elif destino in precios_nacionales and origen == "Caracas":
            precio = precios_nacionales[destino]
        else:
            print("Origen o destino inválido para vuelos nacionales.")
            return 0
    else:
        # Obtener el precio del vuelo internacional según origen y destino
        if origen in precios_internacionales and destino == "Caracas":
            precio = precios_internacionales[origen]
        elif destino in precios_internacionales and origen == "Caracas":
            precio = precios_internacionales[destino]
        else:
            print("Origen o destino inválido para vuelos internacionales.")
            return 0

    # Aplicar descuento para niños menores de 18 años y personas mayores de 60
    if edad < 18 or edad > 60:
        descuento = 0.10  # 10% descuento
    else:
        descuento = 0.0

    # Si es boleto de ida y vuelta, multiplicamos el precio por 2
    if es_vuelta:
        precio_total = precio * 2 * (1 - descuento)
    else:
        precio_total = precio * (1 - descuento)

    return precio_total


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
        clase = input("Ingrese opción (1/2/3): ")
        
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
            print("|========================== Vuelos Internacionales Disponibles ==============================|")
            print("| Origen          | Destino         | Precio  | Origen          | Destino         | Precio   |")
            print("|-----------------|-----------------|---------|-----------------|-----------------|----------|")
            print("| Bogota          | Caracas         |  499$   | Caracas         | Bogota          |  499$    |")
            print("| Curazao         | Caracas         |  400$   | Caracas         | Curazao         |  400$    |")
            print("| Santo Domingo   | Caracas         |  700$   | Caracas         | Santo Domingo   |  700$    |")
            print("| La Romana       | Caracas         |  650$   | Caracas         | La Romana       |  650$    |")
            print("|============================================================================================|")
            
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

        # Preguntar si es ida y vuelta
        es_vuelta = input("¿Desea boleto de vuelta? (S/N): ").lower() == "s"
        
        # Calcular el precio total, incluyendo descuento y si es vuelta
        precio = calcular_precio(edad, clase, tipo_boleto, origen, destino, es_vuelta)
        
        print(f"Precio del boleto: {precio:.2f} USD")
        
        # Solicitar el pago
        while True:
            pago = float(input(f"Debe abonar {precio:.2f} USD. Ingrese el monto a pagar: "))
            if pago >= precio:
                cambio = pago - precio
                print(f"Pago recibido: {pago} USD. Su cambio es: {cambio:.2f} USD.")
                break
            else:
                print(f"El monto ingresado es insuficiente. Debe abonar al menos {precio:.2f} USD.")
        
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

