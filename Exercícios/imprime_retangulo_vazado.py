L = int(input("Digite a largura: "))
A = int(input("Digite a altura: "))
C = "#"

print(C * L) 

for _ in range(A-2):
    V = (L - 2) * ' '
    print("%s%s%s" % (C, V, C)) 

print(C * L) 





