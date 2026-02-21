'''Escreva um programa que peça a idade do usuário e informe se ele é menor ou maior de idade.'''

idade = int(input('Qual o sua idade? '))
if idade < 18:
    print('\033[31mDesculpe mas este filme é apenas para maiores de 18 anos, e você só tem {} anos.\033[m'.format(idade))
else:
    print('\033[32mAproveite o filme! :D\033[m')
