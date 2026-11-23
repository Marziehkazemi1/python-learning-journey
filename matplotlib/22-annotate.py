import matplotlib.pyplot as plt
plt.style.use('ggplot')

#annotate : Used to add captions, text, arrows, and mark a specific point on the chart.
# plt.annotate(
#     text,
#     xy=(x, y),                     Coordinates of the desired point
#     xytext=(text_x, text_y),       location show text
#     arrowprops=dict(...)           Flash settings
# )

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 35, 25]

plt.plot(x, y, marker="o")

# plt.annotate(
#     "Maximum Value",
#     xy=(4, 35)
# )

plt.annotate(
    "Maximum Value",
    xy=(4, 35),
    xytext=(3, 40),
    arrowprops=dict(
        arrowstyle="->",
        color="blue",
        linewidth=2,
        connectionstyle="arc3,rad=0.2"
    ),
    bbox=dict(            #for show design text
        boxstyle="round",
        facecolor="yellow",
        edgecolor="black",
        alpha=0.8
    ),
)

plt.show()