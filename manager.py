import sulkusers_data.creador as creador_data 
import sulkusers_credits.creaUsuario as creador_credits


#Alta de Nuevo Usuario dentro de Sulkusers_Data
#Solo aplicación si es un superheroe-random, aplicacion, usuario y contraseña si es un usuario específico.
usuario_creado = creador_data.nuevoUsuario("astroblend-dev", "", "")
print("Éste es el usuario creado: ", usuario_creado)

#Alta o Recarga de Créditos dentro de Sulkusers_Credits
#Aquí le tendrás que decir el usuario que creaste previamente en sulkusers_data
creador_credits.crear_usuario(usuario_creado, "prod", 14)