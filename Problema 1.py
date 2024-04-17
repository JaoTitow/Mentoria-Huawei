cont1 = 0 #
cont2 = 0 #
cont3 = 0 #
cont4 = 0 #

#Listas
intervalo1 = []
i = 0
for i in range(0, 25):
    i += 1
    intervalo1.append(i)
print(intervalo1)

intervalo2 = []
z = 0
for z in range(25, 50):
    z += 1
    intervalo2.append(z)
print(intervalo2)

intervalo3 = []
f = 0
for f in range(50, 75):
    f += 1
    intervalo3.append(f)
print(intervalo3)

intervalo4 = []
h = 0
for h in range(75, 100):
    h += 1
    intervalo4.append(h)
print(intervalo4)

x = 1
#Repetição
while x >= 0:
    
    x = int(input("Digite um número inteiro positivo para iniciar, e um número negativo para parar: \n"))
    if x <= 25:
        cont1 += 1
    if x >= 26 and x <= 50:
        cont2 += 1
    if x >= 51 and x <= 75:
        cont3 += 1
    if x >= 76 and x <= 100:
        cont4 += 1
print("A quantidade de números no primeiro intervalo:", cont1)
print("A quantidade de números no segundo intervalo:", cont2)
print("A quantidade de números no terceiro intervalo:", cont3)
print("A quantiadde de números no Quarto intervalo:", cont4)
    

