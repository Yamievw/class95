# runs hillclimber exhaustively
import pickle
import random
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import progressbar as pb
import os

from HC_hill_climber import *
from random_table import *

print "Beep beeep starting enginesssss!"
print " "
print "3..."
print "2..."
print "1..."
print "Prepare for some awesome hill climbing!!!"
print " "

N = 7
iterations = 100000
tail = 500

path = os.getcwd()
path += "\\Runs\\HC\\"
path += str(datetime.now().date())
path += "\\"
time = str(datetime.now().time())
time = time.split(".")[0]
time = time.replace(":", " ")
path += time
path += "\\"


iterations_list = [0]
scores_list = []

for n in range(N):
    # set up schedule and figure
    schedule = random_table()
    scores_list.append(schedule.score())
    plt.figure()

    print "n = ", n + 1, "/", N, "performing", iterations, "iterations"
    
    

    #initialize widgets
    widgets = ['Hill Climber: ', pb.Percentage(), ' ',  
            pb.Bar(marker=pb.RotatingMarker()), ' ', pb.ETA()]
    #initialize timer
    timer = pb.ProgressBar(widgets=widgets, maxval=iterations).start()


    i = 0
    iterations_list = []
    scores_list = []

    malus_block = []
    malus_conflict = []
    malus_room = []
    bonus = []
    
    for j in range(1, iterations + 1):     
        timer.update(j)
        
        if i%3 == 0:
            schedule = hill_climber_activities(schedule)           
        elif (i-1)%3 == 0:
            schedule = hill_climber_students(schedule)
        else:
            schedule = hill_climber_rooms(schedule)

        iterations_list.append(j)
        scores_list.append(schedule.score())

        tmp = schedule.timetable
        malus_block.append(check_day(tmp))
        malus_conflict.append(check_conflict(tmp))
        malus_room.append(check_room(tmp))
        bonus.append(check_bonus(tmp))
        
        if len(scores_list) > tail:
            if (scores_list[-tail] == scores_list[-1]):
                if i%3 == 0:
                    if i < 3:
                        plt.plot(iterations_list, scores_list, label="Activities", color="b")
                    else:
                        plt.plot(iterations_list, scores_list, color="b")                   
                        
                elif (i-1)%3 == 0:
                    if i < 3:
                        plt.plot(iterations_list, scores_list, label="Students", color="g")
                    else:
                        plt.plot(iterations_list, scores_list, color="g")
                else:
                    if i < 3:
                        plt.plot(iterations_list, scores_list, label="Rooms", color="r")
                    else:
                        plt.plot(iterations_list, scores_list, color="r")
                
                i += 1
                iterations_list = []
                scores_list = []


    if i%3 == 0:
        if i < 3:
            plt.plot(iterations_list, scores_list, label="Activities", color="b")
        else:
            plt.plot(iterations_list, scores_list, color="b")                   
            
    elif (i-1)%3 == 0:
        if i < 3:
            plt.plot(iterations_list, scores_list, label="Students", color="g")
        else:
            plt.plot(iterations_list, scores_list, color="g")
    else:
        if i < 3:
            plt.plot(iterations_list, scores_list, label="Rooms", color="r")
        else:
            plt.plot(iterations_list, scores_list, color="r")   
            
        
        
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
    plt.clf()
    plt.figure()
    plt.plot(malus_block, label="block")
    plt.plot(malus_conflict, label="conflict")
    plt.plot(malus_room, label="room")
    plt.plot(bonus, label="bonus")
    plt.legend()
    plt.savefig(filename + " score distribution")
    plt.clf()
    print " "

