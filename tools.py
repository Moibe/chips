import openpyxl
import importlib
import os

def manageExcel(archivo_excel):
    #Especificaciones Excel: 
    # Comprobar si el archivo existe
    try:
        workbook = openpyxl.load_workbook(archivo_excel)
        sheet = workbook.active
        
    #Se va al Except si no existe y es la primera vez.
    except FileNotFoundError:
        # Si no existe, crear un nuevo libro y hoja
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Usuarios"
        # Agregar los encabezados (si es la primera vez)
        sheet['A1'] = 'Usuario'
        sheet['B1'] = 'Contraseña'
        sheet['C1'] = 'Créditos'

        #Estilo
        # Crear un estilo de fuente en negrita
        bold_font = openpyxl.styles.Font(bold=True)
        # Aplicar el estilo a la fila de los encabezados

        for cell in sheet[1:1]:  # Selecciona todas las celdas de la primera fila
            cell.font = bold_font
        # Ajustar el ancho de la columna A a 20 unidades
        sheet.column_dimensions['A'].auto_size = True
        sheet.column_dimensions['B'].auto_size = True
        sheet.column_dimensions['C'].auto_size = True

    return workbook, sheet

def usuarioExiste(aplicacion, usuario):
    """Obtiene los datos de un usuario a partir del archivo data.py de la aplicación.

    Args:
        aplicacion (str): Nombre de la aplicación.
        usuario (str): Nombre de usuario a buscar.

    Returns:
        list: Lista de tuplas con los datos del usuario, o None si no se encuentra.
    """
    set = "data" #Porque la existencia de los usuarios la revisa en data.py no en novelty.py

    with open('sulkusers_data' + '/' + aplicacion + '/' + set + '.py', 'r') as f:
        datos_existentes = eval(f.read())
    
    for tupla in datos_existentes:
        if tupla[0] == usuario:
                return "Error 183: Usuario ya existe."
    
    