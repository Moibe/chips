import random
import string
import sulkusers_data.herramientas as herramientas

def generar_usuario():
    """Genera un nombre de superhéroe aleatorio único y lo guarda en un archivo."""

    # Abrimos el archivo de superhéroes en modo lectura
    with open('supers.txt', 'r') as archivo:
        superheroes = archivo.readlines()

    # Eliminamos los saltos de línea de cada nombre
    superheroes = [nombre.strip() for nombre in superheroes]

    # Creamos un conjunto para almacenar los nombres generados anteriormente
    nombres_generados = set()

    # Abrimos el archivo de resultados en modo lectura para cargar los nombres existentes
    with open('allUsers.txt', 'r') as archivo_resultados:
        for linea in archivo_resultados:
            nombres_generados.add(linea.strip())

    while True:
        # Seleccionamos un nombre al azar y generamos un número aleatorio
        nombre_aleatorio = random.choice(superheroes)
        numero_aleatorio = str(random.randint(0, 999)).zfill(3)
        nombre_final = nombre_aleatorio + numero_aleatorio

        # Verificamos si el nombre ya existe
        if nombre_final not in nombres_generados:
            break

    
    # Abrimos el archivo en modo append, creando el archivo si no existe
    with open('allUsers.txt', 'a') as archivo:
        # Escribimos el contenido de la variable en una nueva línea
        archivo.write(f"\n{nombre_final}")

    return nombre_final

def generar_contrasena(nombre_heroe):
    """Genera una contraseña basada en los primeros 4 caracteres del nombre y un número secuencial."""

    # Convertir a minúsculas y eliminar caracteres especiales
    nombre_limpio = ''.join(c for c in nombre_heroe.lower() if c in string.ascii_lowercase + string.digits)

    letras, numeros = herramientas.separar_letras_numeros(nombre_limpio)
    nombre_revuelto = herramientas.revolver_letras(letras)
    numeros_finales = herramientas.sumar_numeros_finales(nombre_limpio)

    # Generar la contraseña
    contrasena = nombre_revuelto + str(numeros_finales)

    return contrasena