import os
import openpyxl

def actualizar_excel_con_creditos(ruta_excel, ruta_carpeta_prod):
    """
    Actualiza un archivo Excel con los créditos de los archivos .txt en una carpeta.

    Args:
        ruta_excel (str): Ruta al archivo Excel 'usuarios-ronda1.xlsx'.
        ruta_carpeta_prod (str): Ruta a la carpeta 'sulkusers_credits/prod'.
    """

    print("Entré a actualizar_excel_con_creditos...")
    try:
        # Carga el libro de Excel
        libro_excel = openpyxl.load_workbook(ruta_excel)
        hoja = libro_excel.active

        # Crea un diccionario para almacenar los créditos de los archivos .txt
        creditos_por_archivo = {}
        for nombre_archivo in os.listdir(ruta_carpeta_prod):
            if nombre_archivo.endswith('.txt'):
                print("Nombre archivo era: ", nombre_archivo)
                nombre_sin_extension = nombre_archivo.removesuffix(".txt")
                ruta_archivo = os.path.join(ruta_carpeta_prod, nombre_archivo)
                print("Ésta es la ruta archivo: ", ruta_archivo)
                try:
                    with open(ruta_archivo, 'r') as archivo:
                        cantidad = int(archivo.read().strip())
                        print("Ésta es la cantidad: ", cantidad)
                    creditos_por_archivo[nombre_sin_extension] = cantidad
                except (FileNotFoundError, ValueError):
                    print(f"Error al procesar {nombre_archivo}")

        print("Así quedó créditos por archivo: ", creditos_por_archivo)

        # Escribe los créditos en la columna 'Update'
        hoja['D1'] = 'Update'  # Encabezado de la columna
        for fila in range(2, hoja.max_row + 1):
            print("Estoy en la fila: ", fila)
            nombre_archivo = hoja[f'A{fila}'].value
            print("Del segundo for, éste es cada nombre archivo: ", nombre_archivo)
            if nombre_archivo in creditos_por_archivo:
                print("Caí en el if que encontró un archivo...")
                hoja[f'D{fila}'] = creditos_por_archivo[nombre_archivo]

        # Guarda el libro de Excel actualizado
        libro_excel.save(ruta_excel)
        print(f"Archivo Excel '{ruta_excel}' actualizado exitosamente.")

    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta_excel} o {ruta_carpeta_prod}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejemplo de uso:
ruta_excel_usuarios = 'usuarios-ronda1.xlsx'
ruta_carpeta_prod_creditos = 'sulkusers_credits/prod'  # Reemplaza con la ruta correcta

actualizar_excel_con_creditos(ruta_excel_usuarios, ruta_carpeta_prod_creditos)