'''Estou de folga e quero maratonar uma sequência de filmes. Decidi criar um programa
onde listo algumas sequências que estou a fim, e ele sorteia uma pra mim assistir.'''

from random import choice
quantidade = int(input('\033[1;35mQuantos filmes (ou sequências) você quer sortear?\033[m '))
list_filmes = []
for i in range(quantidade):
    filme = input(f'Digite o nome do filme {i+1}: ')
    list_filmes.append(filme)
if len(list_filmes) > 0:
    print('\033[36mO filme sorteado foi: {}\033[m'.format(choice(list_filmes)))
else:
    print('Nenhum filme foi adicionado')
