import matplotlib.pyplot as plt

#subplots : To create multiple charts on one page

# fig, ax = plt.subplots()
# ax.plot([1, 2, 3, 4], [10, 20, 15, 30])
# ax.set_title("My First Plot")
# ax.set_xlabel("X")
# ax.set_ylabel("Y")
# plt.show()


##########exam 2###############
#With the nrows and ncols arguments, we specify how many rows and columns to have.
# fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 4))

# #axes[0]: first chart
# axes[0].plot([1, 2, 3], [10, 20, 30])
# axes[0].set_title("Line Plot")

# #axes[0]: second chart
# axes[1].bar(["A", "B", "C"], [10, 20, 30])
# axes[1].set_title("Bar Plot")

# #axes[0]: third chart
# axes[2].scatter([1, 2, 3], [10, 20, 30])
# axes[2].set_title("Scatter Plot")

# plt.tight_layout()
# plt.show()



##########exam 3###############
# fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# axes[0, 0].plot([1, 2, 3], [10, 20, 30])
# axes[0, 0].set_title("Line Plot")

# axes[0, 1].bar(["A", "B", "C"], [5, 10, 15])
# axes[0, 1].set_title("Bar Plot")

# axes[1, 0].hist([10, 20, 20, 30, 30, 30])
# axes[1, 0].set_title("Histogram")

# axes[1, 1].scatter([1, 2, 3], [5, 10, 15])
# axes[1, 1].set_title("Scatter Plot")

# plt.tight_layout()
# plt.show()



##########exam 4###############
fig, axes = plt.subplots(
    2, 1,
    figsize=(8, 6),
    sharex=True      #Both X-axis ranges and scales have the same
    # sharey=True
)

axes[0].plot([1, 2, 3, 4], [10, 20, 30, 40])
axes[0].set_title("Chart 1")

axes[1].plot([1, 2, 3, 4], [5, 15, 25, 35])
axes[1].set_title("Chart 2")

plt.tight_layout()
plt.show()