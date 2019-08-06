def maiusculas(frase):
    palavra = " "
    for _ in frase:
        if ord(_) >= 65 and ord(_) <= 90:
               palavra = palavra + _
    palavra = palavra.replace( " ", "")
    return palavra

