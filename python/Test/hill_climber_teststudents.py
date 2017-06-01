from HC_hill_climber import *
from random_table import *

import matplotlib.pyplot as plt
# import seaborn as sns

iterations = []
scores = []

schedule = random_table()

for i in range(10):
    iterations.append(i)
    scores.append(schedule.score())
    schedule = hill_climber_students(schedule)

plt.plot(iterations, scores)
plt.xlabel("Iterations")
plt.ylabel("Score")
plt.title("Hill Climber Students")
plt.show()
