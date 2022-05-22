real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 4.66
euro = real / 5.15
print('Com R${:.2f} você consegue comprar U${:.2f}'.format(real, dolar))
print('Com R${:.2f} você consegue comprar €{:.2f}'.format(real, euro))

