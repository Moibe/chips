import fireWhale

quota_actual = fireWhale.obtenDato("quota", "quota", "segundos")
quota_nueva = round((quota_actual + 5.2),2)
print(f"Quota: {quota_actual} -> {quota_nueva}.")

#No se puede pasar de 1500.
if quota_nueva >= 1500:
    quota_nueva = 1500

fireWhale.editaDato("quota", "quota", "segundos", quota_nueva)
