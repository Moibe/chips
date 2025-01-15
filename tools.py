import openpyxl

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

   