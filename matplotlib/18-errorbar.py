import matplotlib.pyplot as plt
plt.style.use('ggplot')

# plt.errorbar(
#     x,
#     y,
#     yerr=None,
#     xerr=None,
#     fmt='',
#     ecolor=None,
#     elinewidth=None,
#     capsize=None,
#     capthick=None,
#     color=None,
#     label=None
# )

models = ['Model A', 'Model B', 'Model C']

accuracy = [85, 90, 88]
errors = [2, 3, 1.5]    #Error value for each value

plt.errorbar(
    models,
    accuracy,
    yerr=errors       #Error rate on the vertical axis
)

plt.title('Model Accuracy')
plt.xlabel('Models')
plt.ylabel('Accuracy (%)')

plt.show()