def busca(lista,elemento):
    i = 0
    if lista.count(elemento) > 0:
        for _ in lista:
            if _ != elemento:
                i = i + 1
            else:
                return i
    else:
        return False
