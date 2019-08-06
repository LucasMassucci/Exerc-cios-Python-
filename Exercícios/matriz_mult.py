
def sao_multiplicaveis(m1, m2):
    NL1 = len(m1)
    NC1 = len(m1[0])
    NL2 = len(m2)
    NC2 = len(m2[0])

    if NC1 == NL2:
        print("true")
        return True
    else:
        print("false")
        return False

