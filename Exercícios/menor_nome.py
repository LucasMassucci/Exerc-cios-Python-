def menor_nome(nomes):    
    lista_nova = []
    for _ in nomes:
        _ = _.replace(" ", "")
        lista_nova.append(_)

    menor = 9999
    for _ in lista_nova:
        if len(_) <  menor:
            menor = len(_)
            palavra = _

    return palavra.capitalize()

