import pandas as pd

# Load the data from a CSV file
file_path = 'population_data.csv'
population_data = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print(population_data.head())

# Get basic statistics of the population column
population_stats = population_data['population'].describe()
print('\nPopulation Statistics:')
print(population_stats)

# Plot a histogram of the population distribution
import matplotlib.pyplot as plt

plt.hist(population_data['population'], bins=20, color='blue', edgecolor='black')
plt.title('Population Distribution')
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.show()
