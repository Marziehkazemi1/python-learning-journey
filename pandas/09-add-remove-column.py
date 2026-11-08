import pandas as pd
from pathlib import Path

base_path = Path(__file__).parent
data_path = base_path / "data" / "all-states-history.csv"

dpath = Path("../data")

df = pd.read_csv(dpath / data_path)

dth = (df["death"] / df["positive"]) * 100

#we want add dth column to df
# df["death_to_positive"]=dth      ===> change original data frame
#oruse assign() method
df = df.assign(death_to_positive=dth)   #not change original data fram and create one copy oringinal data frame then change it.
print(df["death_to_positive"].describe())

#we want create one column and if new column count of death more 100 return True 
def gt_100(data_frame):
    return data_frame["death"] >= 100

print("death gt 100: ",df.assign(death_gt_100 = gt_100))


#for remove column
#not change original data fram and create one copy oringinal data frame then change it.
#drop()
print("remove:", df.drop("date", axis="columns"))