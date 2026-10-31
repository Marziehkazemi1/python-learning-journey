import numpy as np;

height_mean = 170
height_std = 5

heights = np.random.normal(height_mean, height_std, size=(3, 4))
print(heights)

scores = np.random.uniform(low=10, high=20, size=50)
print(scores)