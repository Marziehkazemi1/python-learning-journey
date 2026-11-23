import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

# plt.plot(x, y)
# plt.grid(
#     True,
#     color="gray",
#     linestyle="--",
#     linewidth=0.8,
#     alpha=0.5
# )
# plt.show()



fig, ax = plt.subplots()

ax.plot(x, y)
ax.minorticks_on()    #We want to have side lines between them.

ax.grid(
    True,
    which="major",     #original lines
    color="black",
    linewidth=0.8
)

ax.grid(
    True,
    which="minor",   #subordinate lines
    color="gray",
    linestyle=":",
    alpha=0.5
)

plt.show()
