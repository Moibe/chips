import os

def recarga_usuario(nombre_usuario, ambiente="prod", creditos=10):
    """Recarga los créditos de un usuario.

    Args:
        nombre_usuario (str): El nombre de usuario.
        aplicacion (str, optional): La carpeta donde se encuentran los archivos de usuario. Defaults to "usuarios".
        creditos (int, optional): El número de créditos a agregar. Defaults to 10.
    """
    #ruta_archivo = os.path.join(ambiente, nombre_usuario + ".txt")
    ruta_archivo = os.path.join("sulkusers_credits\\" + ambiente, nombre_usuario + ".txt")

    if not os.path.exists(ruta_archivo):
        print(f"El usuario {nombre_usuario} no existe en {ambiente}.")
    else:
        with open(ruta_archivo, 'r') as archivo:
            creditos_actuales = int(archivo.read())
        nuevos_creditos = creditos_actuales + creditos
        with open(ruta_archivo, 'w') as archivo:
            archivo.write(str(nuevos_creditos))
        print(f"Se han recargado {creditos} créditos al usuario {nombre_usuario}. Nuevo total: {nuevos_creditos}")

if __name__ == "__main__":
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    aplicacion = input("Ingresa el ambiente (presiona Enter para usar 'prod'): ") or "prod"
    while True:
        try:
            creditos = int(input("Ingrese el número de créditos a recargar: "))
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    recarga_usuario(nombre_usuario, aplicacion, creditos)