import pygal
from die import Die

# Create two D20s.
die1 = Die(20)
die2 = Die(20)

# Make some rolls, and store the results in a list.
results = [die1.roll() + die2.roll() for _ in range(50000)]

# Analyze the results.
max_result = die1.num_sides + die2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 50,000 times."
hist.x_labels = [str(value) for value in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')