C101 = 1.2
C102 = 1.3
C103 = 1.5
C104 = 1.2
C105 = 1.3
C106 = 1.0

pedido = True

Mensagem  = """
Olá!
Seja bem vindo, a nossa lojinha!
Escolha um dos nossos produtos pelo codigo:
Cachorro Quente -- 101 -- R$1,2
Bauru Simples -- 102 -- R$1,3
Bauru com Ovo -- 103 -- R$1,5
Hambúrger -- 104 -- R$1,2
Cheeseburger -- 105 -- R$1,3
Refrigerante -- 106 -- R$1,0
"""

print(Mensagem)

while pedido == True:
    item = int(input("Informe o código do item desejado: \n"))
    
    if item > 106 and item < 101:
        print("Item não existente")
    
    if item == 101:
        qt = int(input("Quantos itens você deseja?: \n"))
        C101 += 1
    elif item == 102:
        qt = int(input("Quantos itens você deseja?: \n"))
        C102 += 1
    elif item == 103:
        qt = int(input("Quantos itens você deseja?: \n"))
        C103 += 1
    elif item == 104:
        qt = int(input("Quantos itens você deseja?: \n"))
        C104 += 1
    elif item == 105:
        qt = int(input("Quantos itens você deseja?: \n"))
        C105 += 1
    elif item == 106:
        qt = int(input("Quantos itens você deseja?: \n"))
        C106 += 1
    else:
         print("Item não existente")

    
    pedido = str(input("Você deseja pedir algo mais? S/N \n")).upper()
    if pedido == "S":
        pedido = True
    elif pedido == "N":
        break
    
    
    