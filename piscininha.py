'''Agora que o Prof. Nerynho já construiu sua piscina, ele está testando um programa de localização pessoal que diz o que Nerynho está fazendo na área de sua piscina, 
baseado em uma representação cartesiana vista de um satélite!!!! Ajude o Prof Nerynho a desenvolver seu programa, escrevendo a função piscininha(x, y, w, h, a, b) 
cujas variáveis são:

As primeiras quatro variáveis, x,y,w,h | w,h≥2
 representam a piscina, que é um retângulo de altura h
 e largura w
, alinhado aos eixos cartesianos X e Y, cujo vértice inferior esquerdo está no ponto (x,y)
.
As duas ultimas variáveis,  a
 e b
, representam as coordenadas cartesianas (a,b)
 de onde o Prof Nerynho está.
Entrada
Os parâmetros da função são seis inteiros x,y,w,h,a,b
.

Saída
A saída depende da posição do Prof. Nerynho baseado em onde está sua piscina e:

Caso o professor esteja dentro da piscina, o programa deverá imprimir a frase Dando um tchibum;
Caso o professor esteja fora da piscina, o programa deverá imprimir a frase Tomando um solzin;
Caso o professor esteja na borda da piscina, o programa deverá imprimir a frase So com os pezin dentro da agua.'''

def piscininha(x, y, w, h, a, b):
    if x <= a and a<=(x+w):
        if y <= b and b<=(y+h):
            if y == b or x == a:
                print('So com os pezin dentro da agua')
            else:
                print('Dando um tchibum')
        else:
            print('Tomando um solzin')
    else:
        print('Tomando um solzin')
