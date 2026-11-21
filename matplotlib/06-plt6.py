import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

slices = [8, 5, 3, 2, 0.5, 0.2]

labels = ['sleeping', 'studing', 'laughing', 'working', 'meditaion', 'cooking']

colors = ['blue', 'red', 'pink', 'green', 'yellow', 'purple']

#explod: To make that item come out of the circle a little.
explode = [0, 0, 0, 0.1, 0, 0.5]

#wedgeprops :  For color coding across borders 
#autopct : for show percent of 100%
plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor' : 'black'}, explode=explode, autopct='%1.1f')
plt.show()
