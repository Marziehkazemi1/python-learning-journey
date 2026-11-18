import pandas as pd

#strip() : for delete space or word of text
text = " Login "
result = text.rstrip()
result = text.lstrip()
result = text.strip()
print(result)

text = "###Login###"
result = text.strip("#")
print(result)


data = {
    "module_info": [
        "Login_101",
        "Payment_205",
        "Dashboard_310",
        "User_415"
    ]
}

df = pd.DataFrame(data)

df["module_info"] = df["module_info"].str.strip()

df["module_id"] = df["module_info"].str.extract(r"(\d+)")
print(df)

df["module_name"] = df["module_info"].str.extract(r"([A-Za-z]+)")
print(df)

df[["module_name", "module_id"]] = (
    df["module_info"].str.extract(r"^([A-Za-z]+)_(\d+)$")
)
print(df)
