'''O prof. Fagundes comprou uma caixa com m pacotes de bolacha recheada para distribuí-los igualmente entre os n alunos da sua turma de Estruturas de Dados na Universidade de Brasília (UnB). Apesar de que os alunos tenham adorado essa surpresa, cada um consegue comer no máximo k

pacotes de bolacha, portanto, alguns desses pacotes entregues por aluno podem sobrar. A generosa ideia do querido professor consiste em pegar esses pacotes restantes e entregá-los aos funcionários do Departamento de Ciência da Computação  (CIC) da UnB.

Sabendo-se que cada aluno sempre recebe e come ao menos um pacote de bolacha, elabore uma função chamada  pacotesDeBolacha que receba os três números inteiros m
, n e k

como parâmetros e imprime a quantidade mínima de pacotes de bolacha que serão entregues aos funcionários do CIC.

Entrada
Não há entrada de dados. A função é chamada para valores arbitrários definidos nos casos de teste que são três números inteiros m
, n e k  (1≤n≤104,n≤m≤104,1≤k≤104

) associados ao número total de pacotes de bolacha, a quantidade de alunos da turma e o quantos pacotes de bolacha cada aluno dessa turma consegue comer, respectivamente.

Saída
A função pacotesDeBolacha deve imprimir a quantidade mínima de pacotes de bolacha que serão entregues aos funcionários do CIC.

For example:

Test 	                     Result

pacotesDeBolacha(4,4,1)    0

pacotesDeBolacha(13,5,2)   3

pacotesDeBolacha(10,9,2)   1
'''

def pacotesDeBolacha(qtd_pacotes, consegue_comer, n_alunos):
    n_alunos = min(n_alunos, qtd_pacotes // consegue_comer)
    distribuido = consegue_comer * n_alunos
    sobra = qtd_pacotes - distribuido
    print(sobra)
