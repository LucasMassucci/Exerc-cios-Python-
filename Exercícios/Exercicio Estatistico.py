CodMun = ["4100202","4100400","4103107","4104006","4105201","4105805","4106902","4128633","4107652","4111258","4114302",
          "4119152","4119509","4120804","4122206","4127882"]
          
Mun = ["ADRIANÓPOLIS","ALMIRANTE TAMANDARÉ","BOCAIUVA DO SUL","CAMPINA GRANDE DO SUL","CERRO AZUL","COLOMBO",
      "CURITIBA","DOUTOR ULYSSES","FAZENDA RIO GRANDE","ITAPERUÇU","MANDIRITUBA","PINHAIS","PIRAQUARA","QUATRO BARRAS",
      "RIO BRANCO DO SUL","TUNAS DO PARANÁ"]
      
VPass = [1693,40230,4363,17168,4171,93710,1141183,879,37456,9309,9569,61090,31488,11211,12008,1750]

ATV = [4,60,3,33,4,263,4631,6,81,21,5,216,58,20,24,0]

def menu():

    print()
    print()
    print("*************************************")
    print("Bem vindo ao programa de estatística")
    print('')
    print("1 - Maior e menor índice de acidentes")
    print("2 - Média de veículos de passeio")
    print("3 - Média de acidentes de transito")
    print("")
    print()
    print("*     *****     *****     *****     *")
    print("Fontes:")
    print("http://www.detran.pr.gov.br/wp-content/uploads/2018/12/Anuario_Estatistico_2017.pdf","||Amostra de Ciretrans Curitiba||")
    print("https://ibge.gov.br/")
    print("Carros de passeio: Frota tipo - Automovél, Caminhoneta, Caminhonete, Motor Casa, Utilitário") 
    print("*************************************")

    Escolha = input()

    while not str.isnumeric(Escolha)or Escolha != "1" and Escolha != "2" and Escolha != "3":
        Escolha = input("Opção inválida, por favor digite novamente: ")
             
    if str.isnumeric(Escolha):
        Escolha = int(Escolha)

    if Escolha == 1:
        Maior_e_Menor_indice()

    if Escolha == 2:
        Média_de_Veículos()

    if Escolha == 3:
        Média_Acidentes_Transito()




def Maior_e_Menor_indice():

    print("Maior e Menor índices de acidentes:")
    print()
    print(" O Maior índice é de",max(ATV),"acidentes de trânsito com vítima, pertencentes a",Mun[ATV.index(max(ATV))],"código do município:",CodMun[ATV.index(max(ATV))])
    print()
    print(" O Menor índice é de",min(ATV),"acidentes de trânsito com vítima, pertencentes a",Mun[ATV.index(min(ATV))],"código do município:",CodMun[ATV.index(min(ATV))])
    print()
    menu()



def Média_de_Veículos():

    print("Média de veículos de passeio:")
    print()
    print("Média de veículos de passeio nas cidades juntas:", "%.1f" % (sum(VPass)/(len(VPass))))
    print()
    menu()
    
def Média_Acidentes_Transito():

    lista = []
    Local = []
    COD = []
    
    X = 2000

    for _ in VPass:
        if _ < X:

            lista.append(_)
            Local.append(Mun[VPass.index(_)])
            COD.append(CodMun[VPass.index(_)])
    print("Média de acidentes de transito:")
    print()
    print("Média de acidentes de trânsito nas cidades com menos de",X,"veículos de passeio:","%.1f" % (sum(lista)/(len(lista))))
    print()
    print("Cidades incorporadas:",Local)
    print("Seus respectivos códigos IBGE:",COD)

    menu()

    
    



menu()
