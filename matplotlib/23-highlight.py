import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6]
y = [10, 20, 15, 40, 25, 12]

max_index = y.index(max(y))
min_index = y.index(min(y))

plt.plot(x, y, marker="o")

#show max value
plt.scatter(
    x[max_index],
    y[max_index],
    color="red",
    s=150,
    label="Maximum"
)

# show min value
plt.scatter(
    x[min_index],
    y[min_index],
    color="green",
    s=150,
    label="Minimum"
)

plt.legend()
plt.grid(alpha=0.3)
plt.show()