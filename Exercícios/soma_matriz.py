def soma_matrizes(m1, m2):
    NL1 = len(m1)
    NC1 = len(m1[0])
    NL2 = len(m2)
    NC2 = len(m2[0])

    if NL1 != NL2 or NC1 != NC2:
        return False
    else:
        matriz = []
        for i in range(NL1):
            linha = []
            for j in range(NC1):
                linha.append(0)
            matriz.append(linha)

        
        for linha in range(NL1):
           for coluna in range(NC1):
               matriz[linha][coluna] = m1[linha][coluna] + m2[linha][coluna]
        return matriz
