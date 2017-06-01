from SA_simulated_annealing import *
from random_table import *

from SA_cooling import cool # for testing.

import matplotlib.pyplot as plt
import seaborn as sns

iterations = []
scores = []
temperature = []

schedule = random_table()

T0 = 2000
N = 1000

# activities test
T = T0
for i in range(N):
    iterations.append(i)  
    scores.append(schedule.score())
    temperature.append(T)
    
    schedule = SA_activities(schedule, "exp", T)
    T = cool("linN", T0, Tn, N, i)
    if i % 500 ==0:
        print i


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



print "--------------------------"

# students test
iterations = []
scores = []
temperature = []

T = T0
for i in range(N):
    iterations.append(i)  
    scores.append(schedule.score())
    temperature.append(T)
    
    schedule = SA_students(schedule, "exp", T)
    T = cool("linN", T0, Tn, N,  i)
    if i % 500 ==0:
        print i


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


