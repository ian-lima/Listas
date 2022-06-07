# Podemos criar um loop que busca um elemento em um array;
# A ideia é: percorrer todos os índices e verificar se o elemento é igual ao elemento do índice;
# Ex:
# While condicao
#    if lista[i] == elemento:
#           print("Encontrado!")

l = ["Sofá", "Televisão", "Rádio", "AC", "Poltrona"]

i = 0

item_procurado = input("O que deseja buscar na casa? ")
achou = False

while i < len(l):
    if l[i] == item_procurado:
        print("Encontramos um(a) %s!" % item_procurado)
        achou = True
    i =  i + 1

if achou == False:
    print("Não encontramos o(a) %s" % item_procurado)
