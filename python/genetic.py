from random_table import *
from evolution import evolve
from genetic_utils import *

import matplotlib.pyplot as plt


population = []
population_size = 20
iteration = 700
plot = False
plot2 = True

iterations = []
maxima = []
averages = []
sdevs = []

maxima1 = []
averages1 = []
sdevs1 = []

maxima2 = []
averages2 = []
sdevs2 = []


for i in range(population_size):
    table = random_table()
    population.append(table)

for i in range(iteration):
    #if i%100 == 0:
    print "Iteration number " + str(i)

    iterations.append(i)
    values = assess(population, population_size)

    values1 = assess(population[:10], population_size/2.)
    values2 = assess(population[10:], population_size/2)

    maxima1.append(values1[0])
    averages1.append(values1[1])
    sdevs1.append(values1[2])
    maxima2.append(values2[0])
    averages2.append(values2[1])
    sdevs2.append(values2[2])

     
    maxima.append(values[0])
    averages.append(values[1])
    sdevs.append(values[2])
    population = evolve(population, .5)

    


if plot:
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

if plot2:
    plt.figure(1)
    plt.subplot(211)
    plt.plot(iterations, maxima1)
    plt.xlabel("Generation")
    plt.ylabel("Score")
    plt.title("Maximum Mutation")
    plt.subplot(212)
    plt.plot(iterations, maxima2)
    plt.xlabel("Generation")
    plt.ylabel("Score")
    plt.title("Maximum Cross")

    plt.figure(2)
    plt.subplot(211)
    plt.plot(iterations, averages1)
    plt.errorbar(iterations, averages1, sdevs1)
    plt.xlabel("Generation")
    plt.ylabel("Score")
    plt.title("Average Mutation")
    plt.subplot(212)
    plt.plot(iterations, averages2)
    plt.errorbar(iterations, averages2, sdevs2)
    plt.xlabel("Generation")
    plt.ylabel("Score")
    plt.title("Average Cross")

    plt.tight_layout()
    plt.show()

    
    
    

    

    
