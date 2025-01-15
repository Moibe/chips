import time
import tools
import sulkusers_data.creador as data 
import sulkusers_credits.creaUsuario as credits

#¿Cuantos?:
usuarios = 50
creditos = 10
aplicacion = "superheroes"
ambiente = "prod"

archivo_excel = "usuarios-ronda1.xlsx"

workbook, sheet = tools.manageExcel(archivo_excel)
 # Obtener la última fila con datos
last_row = sheet.max_row

for i in range(usuarios):
    #Alta de Nuevo Usuario dentro de Sulkusers_Data
    #Solo aplicación si es un superheroe-random, aplicacion, usuario y contraseña si es un usuario específico.
    usuario_creado, contrasena = data.nuevoUsuario(aplicacion, "", "")
    print(f"Usuario {usuario_creado} listo.")
    #Alta o Recarga de Créditos dentro de Sulkusers_Credits
    #Aquí le tendrás que decir el usuario que creaste previamente en sulkusers_data
    credits.crear_usuario(usuario_creado, ambiente, creditos)
    sheet.append([usuario_creado, contrasena, creditos])

#Future, poner salvaguarda por si tienes abierto el excel como en batcher.
# Guardar el archivo de Excel
workbook.save(archivo_excel)