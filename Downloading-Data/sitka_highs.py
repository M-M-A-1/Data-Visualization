from pathlib import Path
import csv

path = Path('weather_data/sitka_weather_07-2021_simple.csv')

try:
    lines = path.read_text().splitlines()
except FileNotFoundError:
    print(f"Error: The file at {path} was not found.")
    exit()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)