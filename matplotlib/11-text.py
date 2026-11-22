import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y = [10, 20, 30, 40]

# plt.bar(x, y)

# plt.text(1, 10, '10')   #The number 10 is displayed at coordinates (1, 10).
# plt.text(3, 30, "30")

# plt.show()


countries = ['Germany', 'France', 'Italy', 'Spain']
costs = [1200, 1000, 900, 800]

plt.bar(countries, costs)

for i in range(len(costs)):
  plt.text(
    i,
    costs[i] + 20,
    str(costs[i]),
    ha='center',
    va='bottom',
    fontsize=12,
    color='red',
    fontweight='bold'
)

plt.show()