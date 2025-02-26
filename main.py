import os
import platform

def limpiar_consola():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def calcular_precio(edad, clase, tipo_boleto, origen, destino, es_vuelta=False, servicios=False):
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

    # Calcular el precio base con descuento
    precio_base = precio * (1 - descuento)

    # Si es boleto de ida y vuelta, multiplicamos el precio base por 2
    if es_vuelta:
        precio_ida_y_vuelta = precio_base * 2
    else:
        precio_ida_y_vuelta = precio_base

    # Cargo adicional por la clase de boleto
    if clase == "1":  # Primera Clase
        precio_total = precio_ida_y_vuelta + 50
    elif clase == "2":  # Segunda Clase
        precio_total = precio_ida_y_vuelta + 30
    elif clase == "3":  # Tercera Clase
        precio_total = precio_ida_y_vuelta + 10
    else:
        print("Clase no válida. Se cobrará el precio base.")
        precio_total = precio_ida_y_vuelta

    # Cargo adicional por servicios
    if servicios:
        precio_total += 20  

    return precio_total, precio_ida_y_vuelta, precio_base


def comprar_boleto():
    limpiar_consola()
    cantidad = int(input("Ingrese la cantidad de boletos a comprar: "))

    if cantidad <= 0:
        print("Debe comprar al menos un boleto.")
        return
    
    boletos = []
    mayor_de_edad_comprado = False  # Bandera para validar el primer comprador
    
    for i in range(cantidad):
        print(f"\nBoleto {i+1}:")
        nombre = input("Nombre del pasajero: ")
        cedula = input("Cédula de identidad (V/E): ")
        edad = int(input("Edad del pasajero: "))

        if i == 0 and edad < 18:
            print("El primer boleto debe ser comprado por una persona mayor de edad (18+). Intente de nuevo.")
            return  # Detiene la compra si el primer pasajero no es mayor de edad

        if edad >= 18:
            mayor_de_edad_comprado = True  # Se marca que ya compró un adulto
        
        limpiar_consola()
        print("Seleccione la clase de boleto:")
        print("1. Primera Clase (Cargo adicional de 50$)")
        print("2. Segunda Clase (Cargo adicional de 30$)")
        print("3. Tercera Clase (Cargo adicional de 10$)")
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
        servicios = input("¿Requiere servicios adicionales? (S/N): ").lower() == "s"

        # Preguntar si es ida y vuelta
        es_vuelta = input("¿Desea boleto de vuelta? (S/N): ").lower() == "s"
        
        # Calcular el precio total, incluyendo descuento y si es vuelta
        precio_total, precio_ida_y_vuelta, precio_base = calcular_precio(edad, clase, tipo_boleto, origen, destino, es_vuelta, servicios)
        
        # Ahora sumamos todo al final
        print(f"\nDetalles del pago para {nombre} ({cedula}):")
        print(f"Clase seleccionada: {'Primera' if clase == '1' else 'Segunda' if clase == '2' else 'Tercera'}")
        print(f"Precio de la clase: {'50$' if clase == '1' else '30$' if clase == '2' else '10$'}")
        print(f"Tipo de boleto: {'Ida y vuelta' if es_vuelta else 'Solo ida'}")
        
        # Mostrar el precio de ida o ida y vuelta correctamente
        if es_vuelta:
            print(f"Precio de ida y vuelta (si aplica): {precio_ida_y_vuelta:.2f}$")
        else:
            print(f"Precio de solo ida: {precio_base:.2f}$")
        
        print(f"Servicios adicionales: {'Sí' if servicios else 'No'}")
        print(f"Precio de servicios adicionales: {'20$' if servicios else '0$'}")
        print(f"Precio total del boleto: {precio_total:.2f} USD")

        # Solicitar el pago
        while True:
            pago = float(input(f"Debe abonar {precio_total:.2f} USD. Ingrese el monto a pagar: "))
            if pago >= precio_total:
                cambio = pago - precio_total
                print(f"Pago recibido: {pago} USD. Su cambio es: {cambio:.2f} USD.")
                break
            else:
                print(f"El monto ingresado es insuficiente. Debe abonar al menos {precio_total:.2f} USD.")
        
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


