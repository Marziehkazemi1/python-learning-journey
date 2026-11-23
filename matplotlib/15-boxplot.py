import matplotlib.pyplot as plt

# plt.boxplot(
#     data,
#     vert=True,            Vertical or horizontal chart
#     patch_artist=False,   For color box
#     showmeans=False,      Show mean
#     showfliers=True,      Show outliers
#     notch=False,          Show Median Confidence Interval
#     widths=0.5
# )

complexity = [10, 12, 14, 15, 16, 18, 20, 22, 25, 60]

box = plt.boxplot(complexity, showmeans=True, patch_artist=True)

for item in box['boxes']:
    item.set_facecolor('lightblue')

for item in box['medians']:
    item.set_color('red')
    item.set_linewidth(2)

for item in box['whiskers']:
    item.set_color('green')

for item in box['caps']:
    item.set_color('black')

for item in box['means']:
    item.set_marker('D')
    item.set_markerfacecolor('orange')


plt.title('Code Complexity Distribution')
plt.ylabel('Complexity')

plt.show()