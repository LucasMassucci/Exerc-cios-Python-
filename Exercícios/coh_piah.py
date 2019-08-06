import re

def le_assinatura():
  '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''

  print("Bem-vindo ao detector automático de COH-PIAH.")
  print()
  print()
  wal = float(input("Entre o tamanho medio de palavra:"))
  ttr = float(input("Entre a relação Type-Token:"))
  hlr = float(input("Entre a Razão Hapax Legomana:"))
  sal = float(input("Entre o tamanho médio de sentença:"))
  sac = float(input("Entre a complexidade média da sentença:"))
  pal = float(input("Entre o tamanho medio de frase:"))
  return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    x = 0
    lista_diferença = []
    for _ in range(6):

        diferença = (as_a[x] - as_b[x])
        lista_diferença.append(abs(diferença))
        x = x + 1

    Sab = sum(lista_diferença)/6
    return Sab

def calcula_assinatura(texto):
    lista_frases = []
    lista_palavras = []
    lista_sentencas = []
    for _ in separa_sentencas(texto):
        lista_sentencas.append(_)
        sentenca = _
        frase = separa_frases(sentenca)
        for _ in frase:
            lista_frases.append(_)
            frase = _
            for _ in separa_palavras(frase):
                palavra = _
                lista_palavras.append(palavra)

    NS = len(lista_sentencas)
    NF = len(lista_frases)
    NP = len(lista_palavras)


#TMP
    soma = 0
    for _ in lista_palavras:
        caracteres = int(len(_))
        soma = soma + caracteres
    TMP = (soma / NP)

#TMS
    soma = 0
    for _ in lista_sentencas:
        caracteres = int(len(_))
        soma = soma + (caracteres - lista_sentencas.count(" ") - lista_sentencas.count(",") )
    TMS = (soma / NS)
    
#TMF
    soma = 0
    for _ in lista_frases:
        caracteres = int(len(_))
        soma = soma + (caracteres - lista_frases.count(" ") - lista_frases.count(",") )
    TMF = (soma / NF)

#RTT
    RTT = n_palavras_diferentes(lista_palavras) / NP
# RHL
    RHL = n_palavras_unicas(lista_palavras) / NP
# CMS
    CMS = NF / NS

    as_b = [TMP, RTT, RHL, TMS, CMS, TMF]

    return as_b


def avalia_textos(textos, ass_cp):
    as_a = ass_cp
    apuração = []
    for _ in textos:
        texto = _
        as_b = calcula_assinatura(texto)
        Sab = compara_assinatura(as_a, as_b)
        apuração.append(Sab)

    maior_probabilidade = (apuração.index(min(apuração)) + 1)

    print()
    print("O autor do texto", maior_probabilidade, "está infectado com COH-PIAH")
    return maior_probabilidade

def menu():
    as_a = ass_cp = le_assinatura()
    print()
    print()
    textos = le_textos()
    avalia_textos(textos, ass_cp)







    



