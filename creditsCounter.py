import os
import openpyxl

def procesar_archivos_txt(ruta_carpeta, nombre_archivo_excel):
    """
    Procesa archivos .txt en una carpeta y escribe los resultados en un archivo Excel.

    Args:
        ruta_carpeta (str): Ruta a la carpeta que contiene los archivos .txt.
        nombre_archivo_excel (str): Nombre del archivo Excel a crear.
    """

    # Crea un nuevo libro de Excel
    libro_excel = openpyxl.Workbook()
    hoja = libro_excel.active

    # Escribe los encabezados de las columnas
    hoja['A1'] = 'Nombre del archivo'
    hoja['B1'] = 'Cantidad'

    # Itera sobre los archivos en la carpeta
    fila = 2  # Empezamos en la fila 2 para los datos
    for nombre_archivo in os.listdir(ruta_carpeta):
        if nombre_archivo.endswith('.txt'):
            ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
            try:
                with open(ruta_archivo, 'r') as archivo:
                    cantidad = int(archivo.read().strip())  # Lee la cantidad y la convierte a entero
                hoja[f'A{fila}'] = nombre_archivo
                hoja[f'B{fila}'] = cantidad
                fila += 1
            except FileNotFoundError:
                print(f"Archivo no encontrado: {ruta_archivo}")
            except ValueError:
                print(f"Contenido inválido en {ruta_archivo}: no se puede convertir a entero")

    # Guarda el archivo Excel
    libro_excel.save(nombre_archivo_excel)
    print(f"Archivo Excel '{nombre_archivo_excel}' creado exitosamente.")

# Ejemplo de uso:
ruta_carpeta_prod = 'sulkusers_credits/prod'  # Reemplaza con la ruta a tu carpeta 'prod'
nombre_archivo_excel = 'resultados.xlsx'
procesar_archivos_txt(ruta_carpeta_prod, nombre_archivo_excel)