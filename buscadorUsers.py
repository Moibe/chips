
aplicacion = "astroblend"
set = "data"

with open('sulkusers_data' + '/' + aplicacion + '/' + set + '.py', 'r') as f:
        datos_existentes = eval(f.read())

#print(datos_existentes)

for tupla in datos_existentes: 
        print(tupla[0])
        if tupla[0] == "n_married":
                print("Encontré a n_married!")
                break