import pandas as pd
import matplotlib.pyplot as plt

# Create a fictional climate dataset
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Temperature': [10, 12, 15, 18, 22, 25, 28, 26, 23, 20, 15, 12],
    'Precipitation': [70, 40, 60, 30, 20, 10, 5, 8, 15, 25, 45, 55]
}

climate_data = pd.DataFrame(data)

# Display the climate data
print('Climate Data:')
print(climate_data)

# Plot temperature and precipitation trends over the months
plt.figure(figsize=(10, 6))

# Temperature plot
plt.subplot(2, 1, 1)
plt.plot(climate_data['Month'], climate_data['Temperature'], marker='o', color='orange')
plt.title('Temperature Trend Over Months')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')

# Precipitation plot
plt.subplot(2, 1, 2)
plt.plot(climate_data['Month'], climate_data['Precipitation'], marker='o', color='blue')
plt.title('Precipitation Trend Over Months')
plt.xlabel('Month')
plt.ylabel('Precipitation (mm)')

plt.tight_layout()
plt.show()
