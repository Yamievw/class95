# runs hillclimber
import pickle
import random
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import os

from hill_climber import *
from random_table import random_table

print "Beep beeep starting enginesssss!"
print " "
print "3..."
print "2..."
print "1..."
print "Prepare for some awesome hill climbing!!!"
print " "

N = 1
iterations = 10000


path = os.getcwd()
path += "\\Runs\\HC\\"
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

    scores_list.append(schedule.score())
    iterations_list.append(0)
    
    print "blocks"
    for i in range(1, iterations):
        schedule = hill_climber_activities(schedule, 1)
        iterations_list.append(i)
        scores_list.append(schedule.score())

    plt.plot(iterations_list, scores_list, label="Activities")
    iterations_list = []
    scores_list = []

    print "students"
    for i in range(iterations, 2*iterations):       
        schedule = hill_climber_students(schedule)
        iterations_list.append(i)
        scores_list.append(schedule.score())


    plt.plot(iterations_list, scores_list, label="Students")
    iterations_list = []
    scores_list = []

    print "rooms"
    for i in range(2*iterations , 3*iterations):        
        schedule = hill_climber_rooms(schedule)
        iterations_list.append(i)
        scores_list.append(schedule.score())


    plt.plot(iterations_list, scores_list, label="Rooms")


    plt.legend()
    plt.xlabel("Iterations")
    plt.ylabel("Score")
    plt.title("Hill Climber")


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
