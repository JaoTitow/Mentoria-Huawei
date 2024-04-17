item1 = 1.2
item2 = 1.3
item3 = 1.5
item4 = 1.2
item5 = 1.3
item6 = 1.0

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


preço_total = 0
while pedido == True:
    cod = int(input("Informe o código do item desejado: \n"))
    
    if cod > 106 and item < 101:
        print("Item não existente")
    
    if cod == 101:
        qt = int(input("Quantos itens você deseja?: \n"))
        item1 += 1
        preço_total += 1.2 * qt
    elif cod == 102:
        qt = int(input("Quantos itens você deseja?: \n"))
        item2 += 1
        preço_total += 1.3 * qt
    elif cod == 103:
        qt = int(input("Quantos itens você deseja?: \n"))
        cod += 1
        preço_total += 1.5 * qt
    elif item3 == 104:
        qt = int(input("Quantos itens você deseja?: \n"))
        item4 += 1
        preço_total += 1.2 * qt
    elif cod == 105:
        qt = int(input("Quantos itens você deseja?: \n"))
        item5 += 1
        preço_total += 1.3 * qt
    elif cod == 106:
        qt = int(input("Quantos itens você deseja?: \n"))
        item6 += 1
        preço_total += 1 * qt
        
    else:
         print("Item não existente")

    pedido = str(input("Você deseja pedir algo mais? S/N \n")).upper()
    if pedido == "S":
        pedido = True
    elif pedido == "N":
        continue
print("O valor total da compra foi de: ",preço_total)
    
    