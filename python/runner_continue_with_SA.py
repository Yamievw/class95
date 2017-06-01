import pickle
import os

import random
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import progressbar as pb

from simulated_annealing import *
from random_table import random_table
from cooling import cool

##ttype = "HC"
##date = "2017-05-29"
##time = "17 27 10"
##filename = "1 score=1232"

print "Beep beeep starting up the continued SA!"
print " "
print "3..."
print "2..."
print "1..."
print ""
print "Prepare for some awesome annealing!!!"
print " "

ttype = "HC"
date = "2017-06-01"
time = "01 01 33"
filename = "0 score=1274"

dirname = os.getcwd()
dirname += "\\Runs\\"
dirname += ttype
dirname += "\\"
dirname += date
dirname += "\\"
dirname += time
dirname += "\\"
dirname += filename


file_pi2 = open(dirname, 'r') 
schedule = pickle.load(file_pi2)

iterations = 100000
subdivision = 1000

cooling_schedule = "log"
T0 = 3.
T = T0


path = os.getcwd()
path += "\\Runs\\SA_continued\\"
path += str(datetime.now().date())
path += "\\"
time = str(datetime.now().time())
time = time.split(".")[0]
time = time.replace(":", " ")
path += time
path += "\\"

N = 1
n = 0

print "n = ", n + 1, "/", N, "performing", iterations, "iterations"

#initialize widgets
widgets = ['Simulated Annealing: ', pb.Percentage(), ' ',  
        pb.Bar(marker=pb.RotatingMarker()), ' ', pb.ETA()]
#initialize timer
timer = pb.ProgressBar(widgets=widgets, maxval=iterations).start()




for j in range(iterations/subdivision):
    
    begin = j*subdivision 
    end = (j+1)*subdivision

    

    if j%3==0:
        iterations_list = []
        scores_list = []
        temperatures_list = []
        for i in range(begin, end):
            timer.update(i)
            schedule = SA_activities(schedule, cooling_schedule, T)
            T = cool(cooling_schedule, T0, Tn, iterations, i)
            
            iterations_list.append(i)
            scores_list.append(schedule.score())
            temperatures_list.append(T)

        plt.subplot(211)
        if begin < (subdivision*3):
            plt.plot(iterations_list, scores_list, label="Activities", color="b")
            plt.xlabel("Iterations")
            plt.ylabel("Score")
            plt.title("Simulated Annealing")
            
            plt.subplot(212)
            plt.xlabel("Iterations")
            plt.ylabel("Temperature")
        else:
            plt.plot(iterations_list, scores_list, color="b")
            plt.subplot(212)

        plt.plot(iterations_list, temperatures_list, color="b")
       


    elif (j-1)%3==0:
        iterations_list = []
        scores_list = []
        temperatures_list = []
        
        for i in range(begin, end):
            timer.update(i)
            schedule = SA_students(schedule, cooling_schedule, T)
            T = cool(cooling_schedule, T0, Tn, iterations, i)

            iterations_list.append(i)
            scores_list.append(schedule.score())
            temperatures_list.append(T)


        plt.subplot(211)
        if begin < (subdivision*3):
            plt.plot(iterations_list, scores_list, label="Students", color="g")
        else:
            plt.plot(iterations_list, scores_list, color="g")

        plt.subplot(212)
        plt.plot(iterations_list, temperatures_list, color="g")
       

    else:
        iterations_list = []
        scores_list = []
        temperatures_list = []
        for i in range(begin, end):
            timer.update(i)
            schedule = SA_students(schedule, cooling_schedule, T)
            T = cool(cooling_schedule, T0, Tn, iterations, i)
            
            iterations_list.append(i)
            scores_list.append(schedule.score())
            temperatures_list.append(T)


        plt.subplot(211)
        if begin < (subdivision*3):
            plt.plot(iterations_list, scores_list, label="Rooms", color="r")
            plt.legend()

        else:
            plt.plot(iterations_list, scores_list, color="r")
        plt.subplot(212)
        plt.plot(iterations_list, temperatures_list, color="r")
        

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



timer.finish()
print " "
