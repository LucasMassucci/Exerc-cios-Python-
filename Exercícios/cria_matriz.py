def cria_matriz(NL,NC,valor):
    matriz = []

    for i in range(NL):
        linha = []
        for j in range(NC):
            linha.append(valor)



        matriz.append(linha)
    
    return matriz


cria_matriz(5,5,0)
