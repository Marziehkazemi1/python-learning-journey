import matplotlib.pyplot as plt
import numpy as np

#plt.style.use("ggplot")   #when we want using the style
plt.style.use("ggplot") 

# plt.xkcd()

x = np.linspace(-5,5, 10)
fx = x ** 2
fx2 = x ** 3

#When a graph is drawn, there are a series of points that are marked and called markers.
plt.plot(x, fx, color="red", linewidth=2, linestyle="-", marker="*", markersize=6, label="x**2")
plt.plot(x, fx2, color="blue", linewidth=2.5, label="x**4")

#for title
plt.title("first_figure")
plt.xlabel("x")
plt.ylabel("our answers")
# plt.legend()

plt.savefig('final_figure2.png')  #for save chart: pdf, svg, png,...

#plt.grid()    #for grid in background chart
print(plt.style.available)
#for show
plt.show()
