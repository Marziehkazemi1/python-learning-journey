import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5, 100)
fx = x ** 2
fx2 = x ** 3

plt.plot(x, fx, color="red")
plt.plot(x, fx2, color="blue")

#for title
plt.title("first_figure")
plt.xlabel("x")
plt.ylabel("our answers")
plt.legend(["x**2", "x**3"])

#for show
plt.show()
