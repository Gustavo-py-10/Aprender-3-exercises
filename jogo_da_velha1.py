'''Ajude a escrever funções para o Jogo da Velha. 

Neste exercício, o jogo sempre começará com o jogador (X) e ambos os jogadores devem efetuar seus lances de forma alternada. Após cada lance, o tabuleiro deve ser atualizado. Ajude a construir esse jogo implementado somente as seguintes funções:

 Funcao que imprime o tabuleiro na tela 
def imprimeJogo(matriz):
 Funcao que armazena uma jogada e retorna o tabuleiro atualizado 
def atualizaMatriz(matriz, lin, col, tipo):



Entrada
Não há entrada. O parâmetro da função imprimeJogo é uma matriz de caracteres representando o tabuleiro e suas jogadas e os parâmetros da função atualizaMatriz são uma matriz de caracteres representando o tabuleiro e suas jogada, a linha, coluna e tipo que receberão uma nova jogada.



Saída
A matriz contendo o estado do tabuleiro deverá ser impressa na tela de forma que cada item da matriz seja precedido e sucedido por um espaço em branco. 


Observação
A matriz inicial vazia deverá ser preenchida com o símbolo hífen (-) e impressa desta forma:

 -  -  - 
 -  -  - 
 -  -  - 
Durante a atualização do tabuleiro, a matriz deverá ser populada com as letras X (xis maiúsculo) e O (o maiúsculo), e impressa como neste exemplo:

 X  O  X 
 O  X  O 
 X  -  X

For example:

Test	Result
matriz = [[' - ', ' - ', ' - '], 
          [' - ', ' - ', ' - '], 
          [' - ', ' - ', ' - ']]
imprimeJogo(matriz)
 -  -  -
 -  -  -
 -  -  -
matriz = [[' - ', ' X ', ' - '], 
          [' - ', ' O ', ' - '], 
          [' - ', ' X ', ' - ']]
imprimeJogo(matriz)
 -  X  -
 -  O  -
 -  X  -
matriz = [[' - ', ' - ', ' - '], 
          [' - ', ' - ', ' - '], 
          [' - ', ' - ', ' - ']]
imprimeJogo(atualizaMatriz(matriz, 0, 1, ' X '))
 -  X  -
 -  -  -
 -  -  - '''



def imprimeJogo(matriz):
  for linha in matriz:
    print(''.join(linha))
    
def atualizaMatriz(matriz, lin, col, tipo):
  lin, col = map(int, [lin, col])
  matriz[lin][col] = tipo
  return matriz
