import matplotlib.pyplot as plt
# To rotate the text 

countries = ['Germany', 'France', 'Netherlands', 'Switzerland']
costs = [1200, 1000, 1100, 1400]

plt.plot(countries, costs, marker='o')

plt.xticks(rotation=45, ha='left')
plt.yticks(rotation=45)

plt.show()