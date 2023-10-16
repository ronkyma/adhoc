import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the weather data from a CSV file
file_path = 'weather_data.csv'
weather_data = pd.read_csv(file_path)

# Display basic statistics of the dataset
print(weather_data.describe())

# Visualize temperature trends over time

plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Temperature', data=weather_data)
plt.title('Temperature Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (Celsius)')
plt.xticks(rotation=45)
plt.show()

# Visualize correlation between variables
plt.figure(figsize=(10, 8))
sns.heatmap(weather_data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()
