from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('Downloading-data/weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# Extract dates and rainfall.
dates, rainfall = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        rain = float(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
        continue
    else:
        dates.append(current_date)
        rainfall.append(rain)

# Plot the rainfall.
plt.style.use('seaborn-v0_8-notebook')
fig, ax = plt.subplots()
ax.bar(dates, rainfall, color='blue', alpha=0.5)
# ax.plot(dates, rainfall, color='blue', alpha=0.5)
ax.fill_between(dates, rainfall, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title("Daily Rainfall - 2021\nSitka, AK", fontsize=20)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Rainfall (inches)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()