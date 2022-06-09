import matplotlib.pyplot as plt; plt.rcdefaults()
labels = 'Títulos',
Ano = ('Jan/22' , 'Fev/22' , 'Mar/22', 'Abr/22', 'Mai/22')
Títulos = [1, 0, 0, 2, 3]

plt.plot(Ano, Títulos, color='#f9585d')
plt.ylabel('Quantidade de títulos')
plt.title('Títulos dos Santos FC')
plt.legend(labels, loc='upper right')
plt.show()