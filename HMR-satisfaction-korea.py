import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('satisfaction_data.csv')

# Sort the DataFrame by rank for better visualization
df_sorted = df.sort_values('Rank')

# Create a figure with multiple subplots
fig, axes = plt.subplots(nrows=3, figsize=(10, 15))

# Plot Mean Satisfaction Scores
df_sorted.plot(kind='barh', x='Attribute', y='Mean', ax=axes[0], color='skyblue', edgecolor='black')
axes[0].set_title('Mean Satisfaction Scores')
axes[0].set_xlabel('Score')

# Plot Standard Deviations
df_sorted.plot(kind='barh', x='Attribute', y='Standard_Deviation', ax=axes[1], color='lightgreen', edgecolor='black')
axes[1].set_title('Standard Deviations of Satisfaction Scores')
axes[1].set_xlabel('Score')

# Plot Mean Satisfaction Scores vs Standard Deviations
df_sorted.plot(kind='scatter', x='Standard_Deviation', y='Mean', ax=axes[2], color='darkred')
axes[2].set_title('Mean Satisfaction Scores vs Standard Deviations')
axes[2].set_xlabel('Standard Deviation')
axes[2].set_ylabel('Mean Score')

# Adjust layout for better spacing
plt.tight_layout()

plt.show()
