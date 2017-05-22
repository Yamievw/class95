# runs hillclimber
import pickle
import random
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import os

from simulated_annealing import *
from random_table import random_table
from cooling import cool

print "Beep beeep starting up beep beep"
print " "
print "3..."
print "2..."
print "1..."
print ""
print "Prepare for some awesome annealing!!!"
print " "

N = 1
iterations = 10000
cooling_schedule = "expN"
T0 = 100
T = T0



path = os.getcwd()
path += "\\Runs\\SA\\"
path += str(datetime.now().date())
path += "\\"
time = str(datetime.now().time())
time = time.split(".")[0]
time = time.replace(":", " ")
path += time
path += "\\"


for n in range(N):
    # set up schedule and figure
    schedule = random_table()
    plt.figure(n)

    print "n = ", n + 1, "/", N, "performing", iterations, "iterations"
    
    

    # set up plotting lists. 
    iterations_list = []
    scores_list = []
    temperatures_list = [T0]

    scores_list.append(schedule.score())
    iterations_list.append(0)
    
    print "blocks"
    for i in range(1, iterations):
        schedule = SA_activities(schedule, cooling_schedule, T)
        T = cool(cooling_schedule, T0, Tn, iterations, i)

        
        iterations_list.append(i)
        scores_list.append(schedule.score())
        temperatures_list.append(T)

    plt.subplot(211)
    plt.plot(iterations_list, scores_list, label="Activities")
    plt.subplot(212)
    plt.plot(iterations_list, temperatures_list)
    iterations_list = []
    scores_list = []
    temperatures_list = []
    T = T0


    print "students"
    for i in range(iterations, 2*iterations):       
        schedule = SA_students(schedule, cooling_schedule, T)
        T = cool(cooling_schedule, T0, Tn, iterations, i-iterations)
        
        iterations_list.append(i)
        scores_list.append(schedule.score())
        temperatures_list.append(T)


    plt.subplot(211)
    plt.plot(iterations_list, scores_list, label="Students")
    plt.subplot(212)
    plt.plot(iterations_list, temperatures_list)
    iterations_list = []
    scores_list = []
    temperatures_list = []
    T = T0

    print "rooms"
    for i in range(2*iterations , 3*iterations):        
        schedule = SA_students(schedule, cooling_schedule, T)
        T = cool(cooling_schedule, T0, Tn, iterations, i-2*iterations)
        
        iterations_list.append(i)
        scores_list.append(schedule.score())
        temperatures_list.append(T)


    plt.subplot(211)
    plt.plot(iterations_list, scores_list, label="Rooms")
    plt.legend()
    plt.xlabel("Iterations")
    plt.ylabel("Score")
    plt.title("Simulated Annealing")
    plt.subplot(212)
    plt.xlabel("Iterations")
    plt.ylabel("Temperature")
    plt.plot(iterations_list, temperatures_list)
    iterations_list = []
    scores_list = []
    temperatures_list = []
    T = T0


    

    plt.tight_layout()
    filename = path + str(n) + " score="
    score_string = str(schedule.score()).split(".")[0]
    filename += score_string
    print filename
    try:
        os.makedirs(os.path.dirname(filename))
    except:
        pass
    plt.savefig(filename)
    filehandler = open(filename, 'w') 
    pickle.dump(schedule, filehandler)

    print " "
