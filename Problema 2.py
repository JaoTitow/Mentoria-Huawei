qtItems = [0, 0, 0, 0, 0, 0]
lista = [1.2, 1.3, 1.5, 1.2, 1.3, 1]
lista2 = [0, 0, 0, 0, 0, 0]

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
    qt = int(input("Quantos itens você deseja?: \n"))
    
    if cod > 106 and cod < 101:
        print("Item não existente")
    
    if cod == 101:
        qtItems[0] += 1
        lista2[0] = lista[0] * 1.2
        preço_total += 1.2 * qt
        
    elif cod == 102:
        qtItems[1] += 1
        lista2[1] = lista[1] * 1.3
        preço_total += 1.3 * qt
        
    elif cod == 103:
        qtItems[2] += 1
        lista2[2] = lista[2] * 1.5
        preço_total += 1.5 * qt
        
    elif cod == 104:
        qtItems[3] += 1
        lista2[3] = lista[3] * 1.2
        preço_total += 1.2 * qt
        
    elif cod == 105:
        qtItems[4] += 1
        lista2[4] = lista[4] * 1.3
        preço_total += 1.3 * qt
        
    elif cod == 106:
        qtItems[5] += 1
        lista2[5] = lista[5] 
        preço_total += 1 * qt
        
        
    else:
         print("Item não existente")

    pedido = str(input("Você deseja pedir algo mais? S/N \n")).upper()
    if pedido == "S":
        pedido = True
    elif pedido == "N":
        continue
    
    
print("O valor total da compra foi de:",preço_total)
print("O valor de cada item foi de:")
    