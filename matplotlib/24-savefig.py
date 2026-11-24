import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y, marker="o")

plt.title("My Chart")
plt.xlabel("X")
plt.ylabel("Y")

#dpi : Determines the resolution of the saved image.
#bbox_inches : remove space white
#pad_inches : Adjust the spacing around the image.
#transparent : Transparent chart background

plt.savefig("my_chart.png", 
            dpi=300, 
            bbox_inches="tight", 
            pad_inches=0.2, 
            transparent=True,
            facecolor="lightblue",
            edgecolor="black"
)

plt.show()