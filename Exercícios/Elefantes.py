def incomodam(n):
    if ( n <= 0):
        return ""
    else:
        return "incomodam " + incomodam(n-1)


def monta_frases(n):
    if (n == 2):
        frase = "Um elefante incomoda muita gente \n2 elefantes incomodam incomodam muito mais" 
    else:
        frase = "\n{0} elefantes incomodam muita gente \n{1} elefantes {2}muito mais".format(n-1, n, incomodam(n))
        
    return frase

def elefantes(n):
    if ( n <= 1):
        return ""
    else:
        return elefantes(n-1) + monta_frases(n)

