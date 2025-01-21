import os, sys

def crear_usuario(nombre_usuario, carpeta="prod", creditos=11):
    """Crea un archivo y escribe el número de créditos si no existe.

    Args:
        nombre_usuario (str): El nombre de usuario.
        carpeta (str, optional): La carpeta donde buscar el archivo. Defaults to "prod".
        creditos (int, optional): El número de créditos a escribir. Defaults to 11.
    """

    ruta_archivo = os.path.join("sulkusers_credits\\" + carpeta, nombre_usuario + ".txt")

    if not os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'w') as archivo:
            archivo.write(str(creditos))
        print(f"Se han agregado {creditos} créditos al usuario {nombre_usuario}.")
        return nombre_usuario
    else:
        print(f"El archivo {ruta_archivo} ya existe.")
        return "Error 182: ya existe." 

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Si se ejecuta directamente, pedir los datos por teclado
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        carpeta = input("Ingrese la carpeta: ")
        while True:
            try:
                creditos = int(input("Ingrese el número de créditos: "))
                break
            except ValueError:
                print("Los créditos deben ser un número entero.")
    else:
        # Si se llama desde otra función, usar los argumentos proporcionados
        nombre_usuario, *resto = sys.argv[1:]
        carpeta = resto[0] if resto else "prod"
        creditos = int(resto[1]) if len(resto) > 1 else 11

    crear_usuario(nombre_usuario, carpeta, creditos)