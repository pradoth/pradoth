frase = str(input('Digite uma frase: ')).upper()
print('A letra A aparace {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A aparaceu na posição {}'.format(frase.rfind('A')+1))