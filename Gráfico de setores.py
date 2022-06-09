import matplotlib.pyplot as plt
labels = ['Volume útil - 70.87%' , 'Volume total - 54.82%' , 'Reserva técnica - 41.59%']
vals = [70.87 , 54.82, 41.59]
colors = ['#1560c2', '#c22d2d', '#e87d31']
fig , ax = plt.subplots (figsize=(12,5))
explode = (0.1, 0, 0)
ax.pie(vals, labels=labels, shadow=True, explode= explode, colors=colors)
ax.set_title('Nível de água hoje no sistema Cantareira' , fontsize=16)
plt.show()