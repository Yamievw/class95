from random_table import *
from evolution import evolve
from genetic_utils import *

import matplotlib.pyplot as plt


population = []
population_size = 20
iteration = 1000

iterations = []
maxima = []
averages = []
sdevs = []

def Assess(population):
    N = float(len(population))

    # sanity check: population size. 
    if N != population_size:
        return None

    
    max_score = score_sort(population)[0].score()

    tot_score = 0
    for schedule in population:
        tot_score += schedule.score()
    ave_score = tot_score/N

    sdev = 0
    for schedule in population:
        sdev += (ave_score - schedule.score())**2
        
    
    try:
        sdev = math.sqrt(sdev/N)
    except ValueError:
        sdev = 0

    return max_score, ave_score, sdev



for i in range(population_size):
    table = random_table()
    population.append(table)

for i in range(2):
    if i%100 == 0:
        print i

    iterations.append(i)
    values = Assess(population)
    maxima.append(values[0])
    averages.append(values[1])
    sdevs.append(values[2])
    population = evolve(population, .5)



plt.subplot(211)
plt.plot(iterations, maxima)
plt.xlabel("Generation")
plt.ylabel("Score")
plt.title("Maximum scores per generation")

plt.subplot(212)
plt.plot(iterations, averages)
plt.errorbar(iterations, averages, sdevs)
plt.xlabel("Generation")
plt.ylabel("Score")
plt.title("Average scores per generation")

plt.tight_layout()

plt.show()


    

    
