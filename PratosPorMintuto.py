'''O jovem Viníulus é o responsável por preparar o almoço para seus pais em tempos de pandemia. Ultimamente, Viníulus esta bastante estressado por ter que cuidar de todos os almoços e os pratos estão cada dia mais simplificados. Viníulus recebeu algumas reclamações de seus pais e agora pretende organizar melhor seu tempo. Construa um programa que estima o tempo que ele irá levar para preparar o almoço sabendo que cada prato leva em média de 5 à 15 minutos para ser preparado.

Entrada
A entrada consiste do número de pratos (0<pratos

) para serem preparados

Saída
Apresente, em uma linha, a quantidade de horas gastas no melhor e pior caso, com precisão de duas casas decimais.

For example:
Input 	Result

2    Entre 0.17 e 0.50.    

3    
Entre 0.25 e 0.75.   
'''

pratos = int(input())

tempo_minimo_minutos = pratos*5
tempo_maximo_minutos = pratos*15

print(f'Entre {(tempo_minimo_minutos/60):.2f} e {(tempo_maximo_minutos/60):.2f}.')
