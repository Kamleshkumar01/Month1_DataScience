import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

np.random.seed(42)
data = pd.DataFrame({
    'Feature1': np.random.randint(10, 100, 50),
    'Feature2': np.random.randint(20, 80, 50),
    'Category': np.random.choice(['A', 'B'], 50)
})

plt.scatter(data['Feature1'], data['Feature2'], c='blue')
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Scatter Plot")
plt.show()

corr = data.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Heatmap of Features")
plt.show()

sns.pairplot(data, hue="Category")
plt.show()
