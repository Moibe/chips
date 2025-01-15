import sulkusers_data.generador as generador
import sulkusers_data.herramientas as herramientas
import sys

def nuevoUsuario(aplicacion, usuario, contrasena): 

    print(f"Esto es usuario: {usuario} y éste es su tipo {type(usuario)}.")
    if usuario == "":
        usuario = generador.generar_usuario()
    if contrasena == "": 
        contrasena = generador.generar_contrasena(usuario)   
    
    # Formatear los datos como una tupla
    nueva_tupla = (usuario, contrasena)
    herramientas.escritor_tuplas(nueva_tupla, aplicacion, 'data')

    tupla_novelty = (usuario, "user")
    herramientas.escritor_tuplas(tupla_novelty, aplicacion, 'novelty')

    return usuario, contrasena

if __name__ == "__main__":
    print("Estoy aquí y len(sys.argv) es: ", len(sys.argv))
    if len(sys.argv) == 1: #Ésto sifnifica que se corrió sin argumentos.
        aplicacion = input("Ingrese el nombre de la aplicación: ")
        usuario = input("Ingrese el nombre del usuario: ")
        contrasena = input("Ingrese contraseña: ")
        nuevoUsuario(aplicacion, usuario, contrasena)