'''Peça ao usuário um número inteiro e informe se ele é par ou ímpar.'''

n = int(input('Digite um número para saber se ele é Par ou Ímpar: '))
if n % 2 == 0:
    print('\033[34mO número {} É PAR!\033[m'.format(n))
else:
    print('\033[36mO número {} É ÍMPAR!\033[m'.format(n))
