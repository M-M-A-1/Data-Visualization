import pygal
from die import Die

# Create a D6.
die1 = Die()

# Make some rolls, and store the results in a list.
results = [die1.roll() for _ in range(50000)]

# Analyze the results.
frequencies = [results.count(value) for value in range(1, die1.num_sides + 1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling a D6 50,000 times."
hist.x_labels = [str(value) for value in range(1, die1.num_sides + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')