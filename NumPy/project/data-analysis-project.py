import numpy as np

data = np.array([
    [10, 2, 120, 1],
    [20, 5, 250, 0],
    [15, 3, 180, 1],
    [30, 8, 400, 1],
    [12, 2, 150, 0],
    [25, 6, 320, 1]
], dtype=float)

#shape
print("shape:", data.shape)

#data type
print("data type:", data.dtype)

#slice
x = data[:, 0:3]
print("result:", x)

#mean
result_mean = np.mean(x, axis=0)
print("result count change code:", np.round(result_mean[0]))
print("result count complexity code:", np.round(result_mean[1]))
print("result count line code:", np.round(result_mean[2]))


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


#find module defect
result_module_defect = data[data[:,3] == 1]
print("result module defect:", result_module_defect)


#Missing values
result_missing_values = np.isnan(data)
print("result missing values:", result_missing_values)


#Normalization
feature0 = x[:, 0]
min_value0 = np.min(feature0)
max_value0 = np.max(feature0)
normalized_feature0 = (feature0 - min_value0) / (max_value0 - min_value0)
print("normalized_feature0: ",normalized_feature0)

feature1 = x[:, 1]
min_value1 = np.min(feature1)
max_value1 = np.max(feature1)
normalized_feature1 = (feature1 - min_value1) / (max_value1 - min_value1)
print("normalized_feature1: ",normalized_feature1)

feature2 = x[:, 2]
min_value2 = np.min(feature2)
max_value2 = np.max(feature2)
normalized_feature2 = (feature2 - min_value2) / (max_value2 - min_value2)
print("normalized_feature2: ",normalized_feature2)


#replace data
rng = np.random.default_rng(42)
print("replace data:", rng.permutation(data))

