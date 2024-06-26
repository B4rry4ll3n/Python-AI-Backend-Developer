

consumo = float(input())

def recomendar_plano(consumo):

    lista = ["Plano Essencial Fibra - 50Mbps","Plano Prata Fibra - 100Mbps", "Plano Premium Fibra - 300Mbps" ]
     
    if consumo <= 10:
        return lista[0]
    elif consumo > 10 and consumo <= 20:
         return lista[1]
    elif consumo >= 21:
            return lista[2]
    else:
         print("Acabou o programa!")
    
    


    
print(recomendar_plano(consumo))