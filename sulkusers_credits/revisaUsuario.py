import os

def revisa_usuario(nombre_usuario, ambiente="prod"):
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
            print(f"{nombre_usuario} en ambiente {ambiente}, tiene {creditos_actuales} créditos.")

if __name__ == "__main__":
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    ambiente = input("Ingresa el ambiente (presiona Enter para usar 'prod'): ") or "prod"
    revisa_usuario(nombre_usuario, ambiente)