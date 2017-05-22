# runs hillclimber
import pickle
import random
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import os

from hill_climber import *
from random_table import random_table




N = 1
iterations = 1000


path = os.getcwd()
path += "\\Runs\\"
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
    
    

    # set up plotting lists. 
    iterations_list = []
    scores_list = []

    scores_list.append(schedule.score())
    iterations_list.append(0)
    
    print "blocks"
    for i in range(1, iterations):

        if i %1000 == 0:
            print i
        
        schedule = hill_climber_activities(schedule, 1)
        iterations_list.append(i)
        scores_list.append(schedule.score())

    plt.plot(iterations_list, scores_list, label="Activities")
    iterations_list = []
    scores_list = []

    print "students"
    for i in range(iterations, 2*iterations):

        if i %1000 == 0:
            print i
        
        
        schedule = hill_climber_students(schedule)
        iterations_list.append(i)
        scores_list.append(schedule.score())


    plt.plot(iterations_list, scores_list, label="Students")
    iterations_list = []
    scores_list = []

    print "rooms"
    for i in range(2*iterations , 3*iterations):

        if i %1000 == 0:
            print i
        
        schedule = hill_climber_rooms(schedule)
        iterations_list.append(i)
        scores_list.append(schedule.score())


    plt.plot(iterations_list, scores_list, label="Rooms")


    plt.legend()
    plt.xlabel("Iterations")
    plt.ylabel("Score")
    plt.title("Hill Climber")


    filename = path + str(n) + " score=" + str(schedule.score()) 
    print filename
    try:
        os.makedirs(os.path.dirname(filename))
    except:
        pass
    plt.savefig(filename)
    filehandler = open(filename, 'w') 
    pickle.dump(schedule, filehandler) 
        

    
