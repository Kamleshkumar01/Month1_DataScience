import numpy as np
import pandas as pd

arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Squared:", arr ** 2)

data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Score': [85, np.nan, 90, 88],
    'Age': [20, 21, np.nan, 23]
}
df = pd.DataFrame(data)
print("\nOriginal DataFrame:\n", df)

df_clean = df.dropna()
print("\nAfter Removing Missing Values:\n", df_clean)

avg_score = df['Score'].mean()
print("\nAverage Score:", avg_score)

df_grouped = df.groupby('Age').mean(numeric_only=True)
print("\nGrouped Data:\n", df_grouped)
