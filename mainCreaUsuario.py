import time
import sulkusers_data.creador as data 
import sulkusers_credits.creaUsuario as credits_crea
import sulkusers_credits.recargaUsuario as credits_recarga
#Elimína ésta redundancia poniendo ambas funciones en el mismo py.

#Para data
aplicaciones = ["astroblend", "observa", "palette", "sampler", "superheroes"]
usuario = "sergiojimenez90"
contrasena = "12345"
novelty = "new_user"
#Para credits
ambiente = "prod" #dev o prod solo afectan a crédits, puesto que las apps tienen nombres propios.
creditos = 1 #Como los créditos son generales fijate de no agregarle más y más cada q lo incluyes en una nueva app.

print("Iniciando proceso para cargar en sulkusers-data")
#El for para hacer varias apps, debería empezar aquí.
for aplicacion in aplicaciones: 
    print("Cargando en app: ", aplicacion)
    data.nuevoUsuario(aplicacion, usuario, contrasena, novelty)
    resultado_crear_creditos = credits_crea.crear_usuario(usuario, ambiente, creditos)
    print("Proceso finalizado")
    print("-------------------------------------------------------------")
    print("Iniciando proceso para cargar créditos.")
    if "ya existe" in resultado_crear_creditos:
        #Si el usuario existe ya en credits, entonces recargará los créditos indicados.
        print("Como el usuario ya existe recargaré ese ya existente:")
        credits_recarga.recarga_usuario(usuario, ambiente, creditos)
    print("Proceso finalizado.")

print("For terminado.")

print("Todas las operaciones completadas, gracias.")