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

N = 10
iterations = 50000
subdivision = 1000


path = os.getcwd()
path += "\\Runs\\HC\\"
path += str(datetime.now().date())
path += "\\"
time = str(datetime.now().time())
time = time.split(".")[0]
time = time.replace(":", " ")
path += time
path += "\\"

#import libraries
import progressbar as pb




def HC_activities(schedule, begin, end):
    iterations_list = []
    scores_list = []
    for i in range(begin, end):
        timer.update(i)
        schedule = hill_climber_activities(schedule, 1)
        iterations_list.append(i)
        scores_list.append(schedule.score())

    if begin < (3*subdivision):
        plt.plot(iterations_list, scores_list, label="Activities", color="b")
    else:
        plt.plot(iterations_list, scores_list, color="b")

    return schedule

def HC_students(schedule, begin, end):
    iterations_list = []
    scores_list = []
    for i in range(begin, end):
        timer.update(i)
        schedule = hill_climber_students(schedule)
        iterations_list.append(i)
        scores_list.append(schedule.score())

    if begin < (3*subdivision):
        plt.plot(iterations_list, scores_list, label="Students", color="g")
    else:
        plt.plot(iterations_list, scores_list, color="g")
        

    return schedule

def HC_rooms(schedule, begin, end):
    iterations_list = []
    scores_list = []
    for i in range(begin ,end):
        timer.update(i)
        schedule = hill_climber_rooms(schedule)
        iterations_list.append(i)
        scores_list.append(schedule.score())


    if begin < (3*subdivision):
        plt.plot(iterations_list, scores_list, label="Rooms", color="r")
    else:
        plt.plot(iterations_list, scores_list, color="r")

    
    return schedule

for n in range(N):
    # set up schedule and figure
    schedule = random_table()
    plt.figure(n)

    print "n = ", n + 1, "/", N, "performing", iterations, "iterations"
    
    

    #initialize widgets
    widgets = ['Hill Climber: ', pb.Percentage(), ' ',  
            pb.Bar(marker=pb.RotatingMarker()), ' ', pb.ETA()]
    #initialize timer
    timer = pb.ProgressBar(widgets=widgets, maxval=iterations).start()

            



    for j in range(iterations/(subdivision)):
        timer.update(j)
 
        begin = j*subdivision + 1
        end = (j+1)*subdivision

        if j%3 == 0:
            schedule = HC_activities(schedule, begin,end)            
        elif (j-1)%3 == 0:
            schedule = HC_students(schedule, begin, end)
        else:
            schedule = HC_rooms(schedule, begin, end)
        
        
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

    
    timer.finish()
    print " "

