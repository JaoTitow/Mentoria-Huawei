#Variaveis // Listas
qtItems = [0, 0, 0, 0, 0, 0]
lista = [1.2, 1.3, 1.5, 1.2, 1.3, 1]
pedido = True
preço_total = 0

#Mensagem
print("Olá!\nSeja bem vindo, a nossa lojinha!\nEscolha um dos nossos produtos pelo código:\nCachorro Quente -- 101 -- R$1,2\nBauru Simples -- 102 -- R$1,3\nBauru com Ovo -- 103 -- R$1,5\nHambúrger -- 104 -- R$1,2\nCheeseburger -- 105 -- R$1,3\nRefrigerante -- 106 -- R$1,0\n ---------------------")

#Pegando pedido
while pedido == True:
    cod = int(input("Informe o código do item desejado: \n"))    
    
    #Verificação de código
    while cod < 101 or cod > 106:
        print("\nCódigo Inválido")
        cod = int(input("Informe o código do item desejado: \n"))
    
    qt = int(input("Quantos itens você deseja? \n"))
    
    #Calculo de preços // Quantidade de itens
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
        qtItems[5] = lista[5] * qt
        preço_total += 1 * qt    

    #Repetição ou finalização
    pedido = str(input("Você deseja pedir algo mais? S/N \n")).upper()
    if pedido == "S":
        pedido = True
    elif pedido == "N":
        continue

#Exibindo resultado    
print("O valor total da compra foi de:",preço_total,"\n")
print("O valor de cada item foi de: \nCachorro quente - R${} \nBauru Simples - R${} \nBauru com Ovo - R${} \nHambúrger - R${} \nCheeseburger - R${} \nRefrigerante - R${}".format(qtItems[0], qtItems[1], qtItems[2], qtItems[3], qtItems[4], qtItems[5]))
