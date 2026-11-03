import numpy as np
#Checks whether each array element is equal to positive infinity (+inf) or negative infinity (-inf).
#output is boolean
#true for element is infinity   
#false for element is not infinity

a = np.array([10, np.inf, 25, -np.inf, 50])
result = np.isinf(a)
print(result)


b = np.array([np.nan, np.inf, -np.inf, 10])
print(np.isnan(b))
print(np.isinf(b))
print(np.isinf(b).sum())



#isfinite() ==>  Checks whether the elements of an array have a finite numerical value.
c = np.array([10, 20, np.nan, np.inf, -np.inf, 30])
result = np.isfinite(c)
print("c:",result)