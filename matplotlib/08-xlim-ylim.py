import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [10, 20, 15, 30, 25, 40, 35, 50]

plt.plot(x, y)

# plt.xlim(2, 6)
# plt.ylim(10, 40)

#for choose min and max
plt.xlim(left=0)
plt.ylim(bottom=0)

plt.show()