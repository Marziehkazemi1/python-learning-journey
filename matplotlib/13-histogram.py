import matplotlib.pyplot as plt

# scores = [12, 15, 18, 10, 14, 16, 19, 11, 13, 17, 15, 18]

# #bins specifies how many bins the data should be divided into.

# plt.hist(
#     scores,
#     bins=10,
#     # bins=[0, 5, 10, 15, 20]
#     color='skyblue',
#     edgecolor='black',  
#     alpha=0.5,
# )

# plt.show()


class_a = [12, 14, 15, 16, 17, 18, 19, 15, 16]
class_b = [8, 9, 10, 12, 13, 14, 15, 11, 12]

plt.hist(
    class_a,
    bins=5,
    alpha=0.5,
    label='Class A',
    color='blue'
)

plt.hist(
    class_b,
    bins=5,
    alpha=0.5,
    label='Class B',
    color='red'
)
 
plt.legend()
plt.xlabel('Scores')
plt.ylabel('Frequency')
plt.title('Score Distribution')

plt.show()