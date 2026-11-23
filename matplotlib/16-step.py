import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6]

product_a = [10, 10, 20, 20, 30, 40]
product_b = [5, 15, 15, 25, 25, 35]

plt.step(
    days,
    product_a,
    where='post',
    label='Product A',
    color='blue'
)

plt.step(
    days,
    product_b,
    where='post',
    label='Product B',
    color='red'
)

plt.xlabel('Days')
plt.ylabel('Sales')
plt.title('Product Sales Comparison')

plt.legend()
plt.grid(alpha=0.3)
plt.show()