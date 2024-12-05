'''Em Campinas, cidade do interior de São Paulo, existem infintos galões de água de 1 litro, que custam a
 dinheiros, e infinitos galões de 2 litros, que custam b
 dinheiros, disponíveis para venda. Qual o menor número de dinheiros necessário para Fagundes comprar exatamente n
 litros de água?

Escreva uma função chamada dinheiros que recebe três parâmentros referentes ao número n
 de Litros desejado por Fagundes, o valor a
 de galões de 1L e o valor b
 de galões de 2L. A função deve imprime o pedido com menor valor.

Entrada
Os parâmetros da função são três inteiros n,a,b≥1
.

Saída 
Imprima um único inteiro com a menor quantidade de dinheiro que Fagundes precisa gastar.'''

def dinheiros(litros, valor_1_litro, valor_2_litro):
    preco_1 = (litros) * valor_1_litro
    preco_2 = (litros//2 * valor_2_litro) + (litros%2 )*valor_1_litro
 
    if preco_1 > preco_2:
        if preco_2==0:
            print(preco_1)
        else:
            print(preco_2)
    else:
        print(preco_1)
