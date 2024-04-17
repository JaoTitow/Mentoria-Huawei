qtItems = [0, 0, 0, 0, 0, 0]
lista = [1.2, 1.3, 1.5, 1.2, 1.3, 1]
lista2 = [0, 0, 0, 0, 0, 0]
pedido = True

print("Olá!\nSeja bem vindo, a nossa lojinha!\nEscolha um dos nossos produtos pelo código:\nCachorro Quente -- 101 -- R$1,2\nBauru Simples -- 102 -- R$1,3\nBauru com Ovo -- 103 -- R$1,5\nHambúrger -- 104 -- R$1,2\nCheeseburger -- 105 -- R$1,3\nRefrigerante -- 106 -- R$1,0\n")

preço_total = 0
while pedido == True:
    cod = int(input("Informe o código do item desejado: \n"))    
    
    while cod < 101 and cod > 106:
        print("Código Inválido")
        cod = int(input("Informe o código do item desejado: \n"))
    
    qt = int(input("Quantos itens você deseja? \n"))
    
    if cod == 101:
        qtItems[0] += 1
        qtItems[0] = lista[0] * qt
        preço_total += 1.2 * qt
        
    elif cod == 102:
        qtItems[1] += 1
        qtItems[1] = lista[1] * qt
        preço_total += 1.3 * qt
        
    elif cod == 103:
        qtItems[2] += 1
        qtItems[2] = lista[2] * qt
        preço_total += 1.5 * qt
        
    elif cod == 104:
        qtItems[3] += 1
        qtItems[3]  = lista[3] * qt
        preço_total += 1.2 * qt
        
    elif cod == 105:
        qtItems[4] += 1
        qtItems[4] = lista[4] * qt
        preço_total += 1.3 * qt
        
    elif cod == 106:
        qtItems[5] += 1
        qtItems[5] = lista[5] 
        preço_total += 1 * qt    
    else:
         print("Item não existente")

    pedido = str(input("Você deseja pedir algo mais? S/N \n")).upper()
    if pedido == "S":
        pedido = True
    elif pedido == "N":
        continue
    
print("O valor total da compra foi de:",preço_total,"\n")
print("O valor de cada item foi de: Cachorro quente - R${} \nBauru Simples - R${} \nBauru com Ovo - R${} \nHambúrger - R${} \nCheeseburger - R${} \nRefrigerante - R${}".format(qtItems[0], qtItems[1], qtItems[2], qtItems[3], qtItems[4], qtItems[5]))
