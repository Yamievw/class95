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
subdivision = 100

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
    
    
    for j in range(iterations/subdivision):
        begin = j*subdivision 
        end = (j+1)*subdivision

        

        if j%3==0:
            iterations_list = []
            scores_list = []
            temperatures_list = []
            for i in range(begin, end):
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

    print " "
