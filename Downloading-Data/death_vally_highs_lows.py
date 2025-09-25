from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('Downloading-Data/weather_data/death_valley_2021_simple.csv')
try:
    lines = path.read_text().splitlines()
except FileNotFoundError:
    print(f"Error: The file at {path} was not found.")
    exit()

reader = csv.reader(lines)
header_row = next(reader)

# Determine indexes using header labels.
date_index = header_row.index("DATE")
tmax_index = header_row.index("TMAX")
tmin_index = header_row.index("TMIN")
name_index = header_row.index("NAME")

dates, highs, lows = [], [], []

# Process the first row to capture the station name.
try:
    first_row = next(reader)
    station_name = first_row[name_index]
    current_date = datetime.strptime(first_row[date_index], '%Y-%m-%d')
    high = int(first_row[tmax_index])
    low = int(first_row[tmin_index])
except ValueError:
    print(f"Missing or invalid data for {first_row[date_index]}")
else:
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Process remaining rows.
for row in reader:
    try:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        high = int(row[tmax_index])
        low = int(row[tmin_index])
    except ValueError:
        print(f"Missing data for {row[date_index]}")
        continue
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = f"Daily High and Low Temperatures - 2021\n{station_name}"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
ax.set_ylim(20, 130)  # Fixed y-axis range for direct comparison

plt.show()

