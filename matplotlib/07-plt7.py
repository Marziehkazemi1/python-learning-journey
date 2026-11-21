import matplotlib.pyplot as plt
import numpy as np

###example 1
# plt.style.use("ggplot")

# weeks = [1,2,3,4,5,6,7,8,9,10]

# ALi = [15,85,40,24,40,16,25,34,50,69]
# Sara = [25,70,20,26,23,50,60,63,20,25]
# Mohammad = [20,24,150,100,40,60,20,20,65,54]

# labels = ['ALi', 'Sara', 'Mohammad']
# colors = ['pink','green', 'purple']

# plt.stackplot(weeks, ALi, Sara, Mohammad, labels=labels, colors=colors)
# plt.legend()
# plt.show()


###example 2
years = [2013,2014,2015,2016,2017,2018,2019,2020,2021]
coin_1 = np.array([15,85,40,24,4000,16.5,25,34,2158]) / 1000
coin_2 = np.array([25,1587,2000,26,23.5,1000,60.2,63,20]) / 1000
coin_3 = np.array([20,24,150.6,1215,40.5,60,20,20,65]) / 1000

labels = ['Coni 1', 'Coin 2', 'Coin 3']
colors = ['pink','khaki','purple']

plt.stackplot(years, coin_1, coin_2, coin_3, labels=labels, colors=colors)
plt.legend(loc=(0.05, 0.75))
plt.xlabel('Years')
plt.ylabel('Price')
plt.show()
