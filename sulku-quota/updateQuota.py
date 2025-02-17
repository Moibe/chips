import fireWhale

quota_actual = fireWhale.obtenDato("quota", "quota", "segundos")
print("La quota actual que hay es: ", quota_actual)
quota_nueva = quota_actual + 5
print("La quota nueva es: ", quota_nueva)

#No se puede pasar de 1500.
if quota_nueva >= 1500:
    quota_nueva = 1500

fireWhale.editaDato("quota", "quota", "segundos", quota_nueva)