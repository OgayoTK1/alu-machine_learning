#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

# Plot stacked bar chart of fruit quantities per person
people = ['Farrah', 'Fred', 'Felicia']
fruits = ['apples', 'bananas', 'oranges', 'peaches']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

x_pos = np.arange(len(people))

bottom = np.zeros(len(people))
for i in range(len(fruits)):
    plt.bar(x_pos, fruit[i, :], width=0.5, bottom=bottom,
            color=colors[i], label=fruits[i])
    bottom += fruit[i, :]

plt.xticks(x_pos, people)
plt.ylabel('Quantity of Fruit')
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))
plt.title('Number of Fruit per Person')
plt.legend()
plt.show()