import os

print("UNIDAD 1 FUNDAMENTOS DE PROGRAMACION ORIENTADA  A OBJETOS")
def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'TECNICAS DE PROGRAMACION/ABSTRACCION.py',
        '2': 'TECNICAS DE PROGRAMACION/ENCAPSULACION.py',
        '3': 'TECNICAS DE PROGRAMACION/HERENCIA.py',
        '4': 'TECNICAS DE PROGRAMACION/POLIMORFISMO.py',
        '5': 'CALCULO DE TEMPERATURAS/PROGRAMACION ORIENTADA A OBJETOS.py',
        '6': 'CALCULO DE TEMPERATURAS/FORMA TRADICIONAL.py',
        '7': 'EJEMPLOSMUNDOREAL/CENTROCOMERCIAL.py',
        '8': 'EJEMPLOSMUNDOREAL/RESTAURANTEE.py',
        '9': 'EJEMPLOSMUNDOREAL/TURNOSPARAHOSPITAL.py',
        '10':'PROGRAMA DE IDENTIFICADORES/promedios.py',
        '11':'SEMANA 6 APLICACION DE CONCEPTOS DE POO/CONCEPTOS_POO.py',
        '12':'SEMANA 7 CONSTRUCTORES_DESTRUCTORES/CONSTRUCTORES_DESTRUCTORES.py',




        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - DEBERES DE PROGRAMACION ORIENTADA  A OBJETOS")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()