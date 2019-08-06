def imprime_matriz(matriz):
    x = 0
    for linha in range(len(matriz)):
        for colunas in range(len(matriz[0])):

            print(matriz[x], end= "\n")
            x = x + 1

