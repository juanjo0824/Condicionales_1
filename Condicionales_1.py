cant_minutos= input("digite la cantidad de minutos: ")
cant_minutos= int(cant_minutos)

if cant_minutos <= 3:
    valor_llama =300


else:
    valor_llamada= 300+50*(cant_minutos-3)


    print("el valor de la llamada es " + str(valor_llamada))
