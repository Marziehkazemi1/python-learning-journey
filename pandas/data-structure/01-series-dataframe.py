import pandas as pd

#series: one dimensional of data, eche value have index.
scores = pd.Series([18, 15, 20, 17])

print("scores:", scores)

scores1 = pd.Series(
    [18, 15, 20, 17],
    index=["Ali", "Sara", "Reza", "Mina"]
)

print("scores1:", scores1)
print(scores1["Sara"])
print("index:", scores1.index)    # show index
print("values:",scores1.values)   # show values
print("datatype:", scores1.dtype)    #  datatype
print("shape:", scores1.shape)    
print("size:", scores1.size)     
print("mean:", scores1.mean())  
print("max:", scores1.max())    
print("min:", scores1.min())    

#dataFrame : tow dimensional , keep datas columns and rows.
data = {
    "name": ["Ali", "Sara", "Reza", "Mina"],
    "age": [22, 24, 23, 25],
    "score": [18, 15, 20, 17]
}
df = pd.DataFrame(data)

print("df:", df)
print("name:", df["name"])   #for access to colmun name
print("loc0:", df.loc[0])
print("iloc:", df.iloc[0])
print("shape:",df.shape)
print("dtypes:", df.dtypes)
print("describe:", df.describe())