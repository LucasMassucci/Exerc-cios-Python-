def encontra_impares(lista):
    
    if (len(lista) <= 0):
        return []
    else:
        
        if (lista[0] % 2 > 0):
            a = [lista[0]]
        else:
            a = []

        return a + encontra_impares(lista[1:])
