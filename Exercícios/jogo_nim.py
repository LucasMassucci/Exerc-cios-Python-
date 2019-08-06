def menu():
    global partida_isolada
    
    print("Bem vindo ao jogo do NIM! Escolha:")
    print('')
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    print("")

    Escolha = input()

    while not str.isnumeric(Escolha)or Escolha != "1" and Escolha != "2":
        Escolha = input("Opção inválida, por favor digite novamente: ")
             
    if str.isnumeric(Escolha):
        Escolha = int(Escolha)

    if Escolha == 1:
        print("Você escolheu uma partida isolada!")
        print("")
        partida()
 
    if Escolha == 2:
        print("Você escolheu um campeonato!")
        print("")
        campeonato()



def computador_escolhe_jogada(n, m):
    j = 0

    if n <= m:
        j = n
        return j

    elif n % (m + 1) != 0: 
        while n % (m + 1) != 0 and j <= m and n != 0:
            n = n - 1
            j = j + 1

            if n % (m + 1) == 0:
                return j

    elif n % (m + 1) == 0 and j <= m and n != 0: 
        n = n - 1
        j = j + 1

        if j >= m:
            j = m
            return j
        
        while n % (m + 1) != 0 and j < m and n != 0:
            n = n - 1
            j = j + 1

            if n % (m + 1) == 0:
                return j

            else:
                j = m
                return j



def usuario_escolhe_jogada(n, m):
    
    j = input("\nQuantas peças você vai tirar?\n ")

     
    while not str.isnumeric(j) or not 1 <= int(j) <= m:
        print("\nOops! Jogada inválida! Tente de novo.\n")
        j = input("Quantas peças você vai tirar? \n")
    return int(j)



def partida():
    
    vez = 0  
    


    n = input("Quantas peças? ")
    m = input("Limite de peças por jogada? ")


    while not str.isnumeric(n) or not str.isnumeric(m) or n == 0 or m == 0 or n == m:
        print("")
        print("Oops! Jogada inválida! Tente de novo")
        print("")
        n = input("Quantas peças? ")
        m = input("Limite de peças por jogada? ")

    n = int(n)
    m = int(m)

    
    
    if n % (m + 1) == 0:
        vez = 1
        print("")
        print("Você começa!")
        print("")
        

    if n % (m + 1) != 0:
        vez = 2
        print("")
        print("Computador começa!")
        print("")



    while n > 0:
        if vez == 2 and vez != 1 and n != 0:
            j = int(computador_escolhe_jogada(n, m))            
            vez = 1

            if j == 1:
                print("O Computador tirou uma peça")

            else:
                print("O Computador tirou",j,"peças")

            n = n - j
        
            if n == 1:
              print("Agora resta apenas uma peça no tabuleiro")

            elif n == 0:
                pass
        
            elif n > 1:
                print("Agora restam",n,"peças no tabuleiro")
                print("")


        if vez == 1 and vez != 2 and n != 0:
            j = int(usuario_escolhe_jogada(n, m))
            vez = 2

            if j == 1:
                print("Você tirou uma peça")

            else:
                print("Você tirou",j,"peças")
            
            n = n - j
        
            if n == 1:
              print("Agora resta apenas uma peça no tabuleiro")
              print("")

            elif n == 0:
                pass
        
            elif n > 1:
                print("Agora restam",n,"peças no tabuleiro")
                print("")


    if vez == 2:
        print("você ganhou!")
        return 2

    if vez == 1:
        print("Fim do jogo! O computador ganhou!")
        return 1

def campeonato():
    win = 0
    U = 0
    C = 0
    R = 1

    for _ in range(3):
        print("")
        print("**** Rodada", R ,"****")
        print("")
        R = R + 1
        win = partida()
        
        
        
        if win == 2:
            U = U + 1

        if win == 1:
            C = C + 1
    print("")
    print("Placar: Você",U,"X",C, "Computador")

menu()

