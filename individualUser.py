import tools
import sulkusers_data.creador as data 
import sulkusers_credits.creaUsuario as credits

#Para data
aplicacion = "astroblend"
usuario = "javier"
contrasena = "12345"
#Para credits
ambiente = "prod"
creditos = 100

usuario_creado, contrasena = data.nuevoUsuario(aplicacion, usuario, contrasena)
credits.crear_usuario(usuario_creado, ambiente, creditos)