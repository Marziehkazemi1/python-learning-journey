import matplotlib.pyplot as plt
plt.style.use('ggplot')

# loc = [100, 200, 300, 400, 500, 600]
# bugs = [2, 3, 5, 4, 8, 10]

# #s : size of points
# plt.scatter(loc, bugs, color='red', s=100, marker='*', edgecolor='black', linewidth=1.5)

# plt.title('LOC vs Bugs')
# plt.xlabel('Lines of Code')
# plt.ylabel('Number of Bugs')

# plt.show()



healthy_loc = [100, 150, 200, 250, 300]
healthy_complexity = [5, 7, 8, 10, 12]

defective_loc = [250, 350, 400, 500, 600]
defective_complexity = [15, 20, 22, 28, 35]

plt.scatter(
    healthy_loc,
    healthy_complexity,
    color='green',
    label='Healthy'
)

plt.scatter(
    defective_loc,
    defective_complexity,
    color='red',
    label='Defective'
)

plt.xlabel('LOC')
plt.ylabel('Complexity')
plt.title('Healthy vs Defective Modules')

plt.legend()
plt.show()