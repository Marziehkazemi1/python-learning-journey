import numpy as np
#nanmean() ==> Calculates the average of the elements of an array, but ignores NaN values ​​in calculating the average.

a = np.array([10, 20, np.nan, 30, 40])

print(np.mean(a))   #becuase array have nan the result in mean() ==> nan
print(np.nanmean(a))  #ignore nan and calculste mean another number


b = np.array([
    [10, 20, np.nan],
    [30, np.nan, 50],
    [40, 60, 70]
])

print("b:", np.nanmean(b))
print("b axis0:",np.nanmean(b, axis=0))
print("b axis1:",np.nanmean(b, axis=1))



c = np.array([10, 20, 30, 40, np.nan])
result = np.nanmean(c, where=c > 15)
print("result c:", result)



#nanmedian() ==> Calculates the median and ignores NaN values.
d = np.array([10, 20, np.nan, 30, 100])
print("median d:", np.median(d))   #becuase array have nan the result in mean() ==> nan
print("nanmedian d:", np.nanmedian(d))  #ignore nan and calculste median another number


e = np.array([
    [10, np.nan, 30],
    [20, 40, np.nan],
    [30, 60, 90]
])
print("e axis0:", np.nanmedian(e, axis=0))
print("e axis1:", np.nanmedian(e, axis=1))
