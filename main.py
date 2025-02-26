import os
import platform

# Variables globales para el panel de control
total_boletos_vendidos = 0
ingresos_clase = {"1": 0, "2": 0, "3": 0}  # Ingresos por clase
ingresos_tipo_boleto = {"n": 0, "i": 0}  # Ingresos por tipo de boleto
ingresos_ruta = {}  # Ingresos por ruta de viaje
servicios_adicionales = 0  # Número de servicios adicionales


def limpiar_consola():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def actualizar_panel_de_control(precio_total, clase, tipo_boleto, origen, destino, servicios):
    global total_boletos_vendidos, ingresos_clase, ingresos_tipo_boleto, ingresos_ruta, servicios_adicionales

    
    # Actualizar ingresos por clase
    ingresos_clase[clase] += precio_total

    # Actualizar ingresos por tipo de boleto
    ingresos_tipo_boleto[tipo_boleto] += precio_total

    # Actualizar ingresos por ruta de viaje
    ruta = f"{origen} -> {destino}"
    if ruta not in ingresos_ruta:
        ingresos_ruta[ruta] = 0
    ingresos_ruta[ruta] += precio_total

    # Si es ida y vuelta, sumar también la ruta de vuelta
    if tipo_boleto.lower() == 'i':  # Si el boleto es internacional (ida y vuelta)
        ruta_vuelta = f"{destino} -> {origen}"
        if ruta_vuelta not in ingresos_ruta:
            ingresos_ruta[ruta_vuelta] = 0
        ingresos_ruta[ruta_vuelta] += precio_total

    # Actualizar el número de servicios adicionales
    if servicios:
        servicios_adicionales += 1


        

def mostrar_panel_de_control():
    limpiar_consola()
    print("Panel de Control")
    print(f"Total de boletos vendidos: {total_boletos_vendidos}")
    print(f"\nTotal de ingresos por clase:")
    print(f"Primera Clase: {ingresos_clase['1']:.2f} USD")
    print(f"Segunda Clase: {ingresos_clase['2']:.2f} USD")
    print(f"Tercera Clase: {ingresos_clase['3']:.2f} USD")

    print(f"\nTotal de ingresos por tipo de boleto:")
    print(f"Nacional: {ingresos_tipo_boleto['n']:.2f} USD")
    print(f"Internacional: {ingresos_tipo_boleto['i']:.2f} USD")

    print(f"\nDetalle de ingresos por ruta de viaje:")
    for ruta, ingresos in ingresos_ruta.items():
        print(f"{ruta}: {ingresos:.2f} USD")

    print(f"\nNúmero de servicios adicionales solicitados: {servicios_adicionales}")

    input("\nPresione Enter para regresar al menú principal...")


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

    # Aplicar descuento para niños menores de 12 años y personas mayores de 60
    if edad < 12 or edad > 60:
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
    global total_boletos_vendidos  # Indica que usaremos la variable global

    limpiar_consola()
    cantidad = int(input("Ingrese la cantidad de boletos a comprar: "))

    if cantidad <= 0:
        print("Debe comprar al menos un boleto.")
        return
    
    boletos = []
    mayor_de_edad_comprado = False  

    for i in range(cantidad):
        print(f"\nBoleto {i+1}:")
        nombre = input("Nombre del pasajero: ")
        cedula = input("Cédula de identidad (V/E): ")
        edad = int(input("Edad del pasajero: "))

        if i == 0 and edad < 18:
            print("El primer boleto debe ser comprado por una persona mayor de edad (18+). Intente de nuevo.")
            return  

        if edad >= 18:
            mayor_de_edad_comprado = True  

        while True:
            limpiar_consola()
            print("Seleccione la clase de boleto:")
            print("1. Primera Clase (Cargo adicional de 50$)")
            print("2. Segunda Clase (Cargo adicional de 30$)")
            print("3. Tercera Clase (Cargo adicional de 10$)")

            clase = input("Ingrese opción (1/2/3): ")

            if clase not in ["1", "2", "3"]:
                print("Opción no válida. Intente de nuevo.")
                input("Presione Enter para continuar...")
                continue  

            if clase == "3" and edad >= 60:
                print("Los pasajeros mayores de 60 años no pueden comprar boletos de tercera clase. Seleccione otra clase.")
                input("Presione Enter para continuar...")
                continue  
            else:
                break  

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

        es_vuelta = input("¿Desea boleto de vuelta? (S/N): ").lower() == "s"

        precio_total, precio_ida_y_vuelta, precio_base = calcular_precio(edad, clase, tipo_boleto, origen, destino, es_vuelta, servicios)
        
        if es_vuelta:
            precio_total = precio_ida_y_vuelta
            total_boletos_vendidos += 2  
        else:
            total_boletos_vendidos += 1  

        print(f"\nDetalles del pago para {nombre} ({cedula}):")
        print(f"Clase seleccionada: {'Primera' if clase == '1' else 'Segunda' if clase == '2' else 'Tercera'}")
        print(f"Precio de la clase: {'50$' if clase == '1' else '30$' if clase == '2' else '10$'}")
        print(f"Tipo de boleto: {'Ida y vuelta' if es_vuelta else 'Solo ida'}")
        
        if es_vuelta:
            print(f"Precio de ida y vuelta (si aplica): {precio_ida_y_vuelta:.2f}$")
        else:
            print(f"Precio de solo ida: {precio_base:.2f}$")
        
        print(f"Servicios adicionales: {'Sí' if servicios else 'No'}")
        print(f"Precio de servicios adicionales: {'20$' if servicios else '0$'}")
        print(f"Precio total del boleto: {precio_total:.2f} USD")

        actualizar_panel_de_control(precio_total, clase, tipo_boleto, origen, destino, servicios)

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
            mostrar_panel_de_control()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        
        print("\nPresiona Enter para continuar...")
        input("")

mostrar_menu()


