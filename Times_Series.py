import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic time series data
np.random.seed(42)
date_rng = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
time_series_data = pd.DataFrame(date_rng, columns=['date'])
time_series_data['temperature'] = np.random.randint(10, 30, size=(len(date_rng)))

# Display the first few rows of the time series data
print('Time Series Data:')
print(time_series_data.head())

# Plot the time series data
plt.figure(figsize=(10, 6))
plt.plot(time_series_data['date'], time_series_data['temperature'], label='Temperature', color='blue')
plt.title('Temperature Time Series')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.show()

# Basic time series analysis
average_temperature = time_series_data['temperature'].mean()
max_temperature_date = time_series_data['date'][time_series_data['temperature'].idxmax()]

print('\nBasic Time Series Analysis:')
print(f'Average Temperature: {average_temperature:.2f}°C')
print(f'Max Temperature Date: {max_temperature_date.date()}')
