import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

data = {
    "project": [f"P{i}" for i in range(1, 21)],
    "loc": np.random.randint(100, 2000, 20),
    "complexity": np.random.randint(5, 100, 20),
    "changes": np.random.randint(1, 50, 20),
    "defects": np.random.randint(0, 30, 20)
}

df = pd.DataFrame(data)

df["defect_rate"] = df["defects"] / df["loc"] * 100

print(df.head())

##ex1
loc = df["loc"].to_numpy()
mean_loc = loc.mean()
print(mean_loc)

defects = df["defects"].to_numpy()
projects = df["project"].to_numpy()

mean_defects = defects.mean()
mask = defects > 15
result_projects = projects[mask]
result_defects = defects[mask]

print("Mean defects:", mean_defects)
print("Projects with more than 15 defects:", result_projects)
print("Number of defects:", result_defects)


##ex2
filter_project_loc =  df["loc"] > 1000
filter_project_defects = df["defects"] > 10
filtered_df = df[
    (df["loc"] > 1000) &
    (df["defects"] > 10)
]
print(filtered_df)


plt.style.use("ggplot")

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Chart 1: Scatter
axes[0].scatter(
    loc,
    defects,
    color="blue",
    alpha=0.6
)
axes[0].set_title("LOC vs Defects")
axes[0].set_xlabel("LOC")
axes[0].set_ylabel("Defects")

# Chart 2: Bar
complexity_mask = df["complexity"] > 50
filtered_df = df[complexity_mask]

axes[1].bar(
    filtered_df["project"],
    filtered_df["defects"],
    color="orange"
)
axes[1].set_title("High Complexity Projects")
axes[1].set_xlabel("Projects")
axes[1].set_ylabel("Defects")
axes[1].tick_params(axis="x", rotation=45)

# Chart 3: Histogram
changes_mask = df["changes"] > 20
filtered_changes = df[changes_mask]

axes[2].hist(
    filtered_changes["defect_rate"],
    bins=8,
    color="green",
    edgecolor="black"
)
axes[2].set_title("Defect Rate Distribution")
axes[2].set_xlabel("Defect Rate")
axes[2].set_ylabel("Frequency")

plt.tight_layout()
plt.show()



