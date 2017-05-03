from simulated_annealing import *
from random_table import *

from cooling import cool # for testing.

import matplotlib.pyplot as plt
import seaborn as sns

iterations = []
scores = []
temperature = []

schedule = random_table()

T0 = 300

# activities test
T = T0
for i in range(1000):
    iterations.append(i)  
    scores.append(schedule.score())
    temperature.append(T)
    
    schedule = SA_activities(schedule, "lin", T)
    T = cool("exp", T0, i)

plt.figure()
plt.subplot(211)    
plt.plot(iterations, scores)
plt.xlabel("Iterations")
plt.ylabel("Score")
plt.title("Simulated Annealing Activities")

plt.subplot(212)
plt.plot(iterations, temperature)
plt.xlabel("Iterations")
plt.ylabel("Temperature")
plt.title("Temperature")






# students test
iterations = []
scores = []
temperature = []
T = T0
for i in range(1000):
    iterations.append(i)  
    scores.append(schedule.score())
    temperature.append(T)
    
    schedule = SA_students(schedule, "lin", T)
    T = cool("exp", T0, i)


plt.figure()
plt.subplot(211)
plt.plot(iterations, scores)
plt.xlabel("Iterations")
plt.ylabel("Score")
plt.title("Simulated Annealing Students")

plt.subplot(212)
plt.plot(iterations, temperature)
plt.xlabel("Iterations")
plt.ylabel("Temperature")
plt.title("Temperature")
plt.show()


