### implements a simulated annealing algorithm

from cooling import *
from roadmap import roadmap
from swapper import *

import copy # for schedule class
import math # for the exp()
import random # for the sa randomness



def SA_activities(schedule, cooling, T0, iterations=1):
    table = copy.deepcopy(schedule.get_timetable()) # against pointer errors.
    score = schedule.score()

    
    for i in range(iterations):
        # cool
        T = cool(cooling, T0, i)

              
        # move value randomly and assess new score. 
        new_schedule = swap_activity(schedule)
        new_score = new_schedule.score()
        compare = random.uniform(0, 1)

        if T > Tmin:
            SA_value = math.exp(-(score - new_score)/T)
        else:
            SA_value = 0
            
        

        
        if new_score > score:
            score = new_score
            schedule = new_schedule

        # random chance. 
        elif compare <= SA_value:
            score = new_score
            schedule = new_schedule
            
        else:
            table = schedule.get_timetable()

    return schedule

def SA_students(schedule, cooling, T0, iterations=1):
    table = copy.deepcopy(schedule.get_timetable()) # against pointer errors.
    score = schedule.score()

    schedule_roadmap = roadmap(schedule, False)
    keys = schedule_roadmap.keys()
   

    for k in range(iterations):
        T = cool(cooling, T0, k)

        
        # random selection of activity.
        n = random.randint(0, len(keys)-1)
        coordinates = schedule_roadmap[keys[n]]

        
        no_activities = len(coordinates)
        
        # random selection of two objects.
        if no_activities <= 1:
            continue
        elif no_activities == 2:
            i = 0
            j = 1
        elif no_activities > 2:
            i = random.randint(0, no_activities - 1)
            j = random.randint(0, no_activities - 1)
            # we need unique numbers. 
            while i == j:
                j = random.randint(0, no_activities - 1)

        
        # coordinates (day, timeslot, activity index)
        activity1 = table[coordinates[i][1]][coordinates[i][0]][coordinates[i][2]]
        activity2 = table[coordinates[j][1]][coordinates[j][0]][coordinates[j][2]]

        participants1 = activity1.participants
        participants2 = activity2.participants

        m = random.randint(0, len(participants1) - 1)
        n = random.randint(0, len(participants2) - 1)

        student1 = participants1[m]
        student2 = participants2[n]

        if student1 not in participants2:
            participants1[m] = student2
            participants2[n] = student1

            activity1.update_participants(participants1)
            activity2.update_participants(participants2)

            table[coordinates[i][1]][coordinates[i][0]][coordinates[i][2]] = activity1 
            table[coordinates[j][1]][coordinates[j][0]][coordinates[j][2]] = activity2

            
            

            new_schedule = copy.deepcopy(schedule) # otherwise we get pointer problems
            new_schedule = new_schedule.update_timetable(table)

            new_score = new_schedule.score()

            if new_score == 0:
                print "we have encountered a terrible error"
                return 1

            

            compare = random.uniform(0, 1)

            if T > Tmin:
                SA_value = math.exp(-(score - new_score)/T)
            else:
                SA_value = 0

            
            
            if new_score > score:
                score = new_score
                schedule = new_schedule

            # random chance
            elif compare <= SA_value:
                score = new_score
                schedule = new_schedule
                
            else:
                table = schedule.get_timetable()

    return schedule

            
                                            
    

        
        
        

        

        
        
    
    
