import matplotlib.pyplot as plt

#fill-between : Colors the space between the chart and the curves.
# plt.fill_between(
#     x,
#     y1,
#     y2=0,
#     where=None,
#     color=None,
#     alpha=None,
#     interpolate=False,
#     step=None             pre, post, mid
# )

months = [1, 2, 3, 4, 5, 6]
sales = [100, 150, 120, 200, 250, 300]

plt.plot(months, sales)

plt.fill_between(months, sales, where=[x > 150 for x in sales], interpolate=True)

plt.title('Monthly Sales')
plt.xlabel('Months')
plt.ylabel('Sales')

plt.show()