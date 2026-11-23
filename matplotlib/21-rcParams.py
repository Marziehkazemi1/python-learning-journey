import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.facecolor"] = "lightyellow"

plt.rcParams["font.size"] = 12
plt.rcParams["axes.titlesize"] = 16
plt.rcParams["axes.labelsize"] = 13

plt.rcParams["lines.linewidth"] = 2
plt.rcParams["lines.color"] = "blue"

plt.rcParams["axes.grid"] = True
plt.rcParams["grid.linestyle"] = "--"
plt.rcParams["grid.alpha"] = 0.5

plt.plot([1, 2, 3, 4], [10, 20, 15, 30])
plt.title("My Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()