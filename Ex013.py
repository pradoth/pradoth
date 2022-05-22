salário = float(input('Qual o salário do programador? R$'))
novo = salário + (salário * 15/100)
print('O programador que recebia o salário de R${:.2f}, com o aumento de 15% vai passar a receber R${:.2f}'.format(salário, novo))