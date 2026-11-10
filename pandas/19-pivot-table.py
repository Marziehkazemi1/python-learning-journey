import pandas as pd
from pathlib import Path

base_path = Path(__file__).parent
data_path = base_path / "data" / "students.csv"

dpath = Path("../data")

students = pd.read_csv(dpath / data_path)

#pivot_table()  ==> data:recive data frame  , index,  values: On what parameters should the interview be conducted
pivot1 = pd.pivot_table(data=students, index="Gender", values="Height(CM)")
print("pivot1", pivot1)

pivot2 = pd.pivot_table(data=students, index="Gender", values="Height(CM)", columns="Department")
print("pivot2:", pivot2)

target_column = 'salary expectation'
#aggfunc  ==> when want aggration which function call
pivot3 = pd.pivot_table(data=students, 
                index='Gender',
                values=target_column, 
                columns='Department',
                aggfunc=['mean', 'sum'],
                margins=True,
                margins_name='total' )
print('pivot3:', pivot3.T.head())