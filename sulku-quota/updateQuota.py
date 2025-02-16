import fireWhale

quota_actual = fireWhale.obtenDato("quota", "quota", "segundos")
print("La quota actual que hay es: ", quota_actual)
quota_nueva = quota_actual + 5
print("La quota nueva es: ", quota_nueva)
fireWhale.editaDato("quota", "quota", "segundos", quota_nueva)