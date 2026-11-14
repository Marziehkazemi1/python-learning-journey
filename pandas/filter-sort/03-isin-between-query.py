import pandas as pd
#useing for filtering data in pandas

data = {
    "changes": [10, 15, 20, 8, 30, 12, 25, 18],
    "complexity": [5, 8, 10, 3, 15, 6, 12, 9],
    "lines": [100, 150, 200, 80, 300, 120, 250, 180],
    "defects": [0, 1, 1, 0, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

#between() : to select values ​​within a range.
print(df[df["complexity"].between(5, 12)])
print(df[df["complexity"].between(5, 12, inclusive="both")])    #Both limits are included.
print(df[df["complexity"].between(5, 12, inclusive="neither")])   #Neither of the two limits are included.
print(df[df["complexity"].between(5, 12, inclusive="left")])    #just limit left
print(df[df["complexity"].between(5, 12, inclusive="right")])    #just limit right


#isin() : to select values ​​that are in a given set.
print(df[df["complexity"].isin([5, 10])])    #return just columns includes 5 and 10
print(df[~df["complexity"].isin([5, 10, 15])])


#query() : to write filter conditions in the form of a more readable, textual expression.
print(df.query("complexity > 10"))
print(df.query(
    "complexity > 10 and lines > 200"
))
print(df.query(
    "changes > 20 or defects == 1"
))
print(df.query("not defects == 1"))

min_lines = 150
max_complexity = 12
print(df.query(
    "lines >= @min_lines and complexity <= @max_complexity"
))    #when coming value out of program  use @

