import pygal
from die import Die

# Create a D100 and D100.
die1 = Die()
die2 = Die()
die3 = Die()

# Make some rolls, and store the results in a list.
results = []
for roll_num in range(50000):
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die1.num_sides + die2.num_sides + die3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling three dice 50,000 times."
hist.x_labels = ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                 '13', '14', '15', '16', '17', '18']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')