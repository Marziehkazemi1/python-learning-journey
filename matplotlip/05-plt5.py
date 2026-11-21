import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# base_path = Path(__file__).parent
# data_path = base_path / "data" / "sample.csv"

# dataset = pd.read_csv(data_path)

# students = dataset['students']
# living_costs = dataset['living_costs']

# plt.style.use('ggplot')
# plt.bar(students, living_costs)
# plt.show()



######big dataset ##########
base_path = Path(__file__).parent
data_path = base_path / "data" / "all-states-history.csv"

dataset = pd.read_csv(data_path)

dataset_state = dataset['state']
orders = dataset_state.value_counts()

orders = orders.to_dict()

cities = list(orders.keys())
amount = list(orders.values())



plt.style.use('ggplot')
plt.bar(cities, amount)
plt.show()