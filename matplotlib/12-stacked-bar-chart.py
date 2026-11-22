import matplotlib.pyplot as plt

countries = ['Germany', 'France', 'Italy', 'Spain']

housing = [800, 700, 600, 500]
food = [300, 250, 220, 200]
transport = [100, 90, 80, 70]

plt.bar(countries, housing, label='Housing')

plt.bar(
    countries,
    food,
    bottom=housing,
    label='Food'
)

plt.bar(
    countries,
    transport,
    bottom=[h + f for h, f in zip(housing, food)],
    label='Transport'
)

plt.xlabel('Countries')
plt.ylabel('Cost')

plt.title('Total Living Costs')

plt.legend()
plt.show()