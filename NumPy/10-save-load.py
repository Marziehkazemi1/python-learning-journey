import numpy as np

x = np.arange(10)
y = x ** 2
print(x , y)

np.savez("x_y-squared.npz", x_arr=x, y_arr=y)

del x,y

load_xy = np.load("x_y-squared.npz")
print(load_xy)

#for access datas
x = load_xy["x_arr"]
y = load_xy["y_arr"]
print(x,y)

# create csv file
# we can add one dimension with use np.newaxis
array_2d = np.block([x[:, np.newaxis], y[:, np.newaxis]])
print(array_2d)

np.savetxt("x_y-squared.csv", X=array_2d, header="x,y", delimiter=",")
del x,y

load_xy = np.loadtxt("x_y-squared.csv", delimiter=",")
x = load_xy[:, 0]
y = load_xy[:, 1]
print(x,y)