import pandas as pd

df = pd.DataFrame({
    "module": ["Login", "Payment", "UserProfile", "login_page", "Dashboard"],
    "project": ["Web App", "Mobile App", "Web App", "Web App", "Mobile App"],
    "status": ["Bug Found", "Clean", "Bug Found", "Clean", "Bug Found"]
})

print(df)

#contains() : To check if a specific phrase or character exists in the text.
#case : for ignore latter and lower case
print(df[df["module"].str.contains("login", case=False)])

#lower() : for convart all of latter word to lower word
df["module"] = df["module"].str.lower()
print(df)

#replace() : for replace section of text to another text
#df["column"].str.replace("old", "new")
df["project"] = df["project"].str.replace(" ", "_")
df["module"] = df["module"].str.replace("login", "authentication")
print(df)


df["project"] = (
    df["project"]
    .str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
)
print(df)
