import sulkusers_data.generador as generador
import sulkusers_data.herramientas as herramientas
import sys
import tools
import time

def nuevoUsuario(aplicacion, usuario, contrasena, novelty): 

    if usuario == "":
        usuario = generador.generar_usuario()
    if contrasena == "": 
        contrasena = generador.generar_contrasena(usuario)   

    #Antes de crear la tupla, asegurate de que ese Usuario no exista en Esa aplicación, ya q estarías sobreescribiendo.
    if tools.usuarioExiste(aplicacion, usuario):
        print("Usuario ya existe, no crearé uno nuevo.")
        
    else:
        print("Usuario no existe, adelante...")

        # Formatear los datos como una tupla
        nueva_tupla = (usuario, contrasena)
        herramientas.escritor_tuplas(nueva_tupla, aplicacion, 'data')

        tupla_novelty = (usuario, novelty)
        herramientas.escritor_tuplas(tupla_novelty, aplicacion, 'novelty')



if __name__ == "__main__":
    print("Estoy aquí y len(sys.argv) es: ", len(sys.argv))
    if len(sys.argv) == 1: #Ésto sifnifica que se corrió sin argumentos.
        aplicacion = input("Ingrese el nombre de la aplicación: ")
        usuario = input("Ingrese el nombre del usuario: ")
        contrasena = input("Ingrese contraseña: ")
        nuevoUsuario(aplicacion, usuario, contrasena)