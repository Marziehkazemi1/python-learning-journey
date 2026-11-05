import numpy as np

data = np.array([
    [10, 2, 120, 1],
    [20, 5, 250, 0],
    [15, 3, 180, 1],
    [30, 8, 400, 1],
    [12, 2, 150, 0],
    [25, 6, 320, 1],
    [18, 4, 210, 0],
    [35, 9, 500, 1]
], dtype=float)

#A
print("shape:", data.shape)
print("count row:", data.shape[0])
print("count column:", data.shape[1])
print("data type:", data.dtype)
x = data[:, 0:3]
print("x:", x)
y = data[:, -1]
print("y:", y)
result_module_defect = data[data[:,3] == 1]
print("result module defect:", result_module_defect)


#B
result_mean = np.mean(x, axis=0)
print("result mean count change code:", result_mean[0])
print("result mean count complexity code:", result_mean[1])
print("result mean count line code:", result_mean[2])

result_median = np.median(x, axis=0)
print("result median count change code:", result_median[0])
print("result median count complexity code:", result_median[1])
print("result median count line code:", result_median[2])

result_deviation = np.std(x, axis=0)
print("result deviation count change code:", result_deviation[0])
print("result deviation count complexity code:", result_deviation[1])
print("result deviation count line code:", result_deviation[2])

#max each feature
result_max_feature = np.max(x, axis=0)
print("result change code max:", result_max_feature[0])
print("result change complexity max:", result_max_feature[1])
print("result change line max:", result_max_feature[2])

#min ecah feature
result_min_feature = np.min(x, axis=0)
print("result change code min:", result_min_feature[0])
print("result change complexity min:", result_min_feature[1])
print("result change line min:", result_min_feature[2])

lines = data[:, 2]
find_argmax = np.argmax(lines)
print("find argmax:", find_argmax)


#C
new_arr = data.copy()
change_type = new_arr.astype(np.int64)
print("change type:", change_type.dtype)

data[1, 1] = np.nan
print("new data:", data)

find_nan = np.isnan(data)
print("find nan:", np.argwhere(find_nan))

column_mean = np.nanmean(data, axis=0)
print("column mean:", column_mean)

data[1, 1] = column_mean[1]

print("data after imputation:", data)


#D
defective_count = np.sum(y)
print("defective count:", defective_count)
non_defective_count = np.sum(y == 0)
print("non defective count:", non_defective_count)

unique_values = np.unique(y)
print("unique values", unique_values)

rng = np.random.default_rng(42)
print("replace data:", rng.permutation(data, axis=1))