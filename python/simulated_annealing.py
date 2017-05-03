### implements a simulated annealing algorithm

from cooling import cool
from roadmap import roadmap

import copy # for schedule class
import math # for the exp()
import random # for the sa randomness


def SA_activities(schedule, cooling, T0, iterations=1):
    table = copy.deepcopy(schedule.get_timetable()) # against pointer errors.
    score = schedule.score()

    
    for i in range(iterations):
        # cool
        T = cool(cooling, T0, i)

        #----------------------------stop in swapfunctie-----------------
        
        # swap value 1
        day1 = random.randint(0, 4)
        timeslot1 = random.randint(0, 3) #niet 17:00-19:00
        count1 = len(table[timeslot1][day1])
        try:
            activity1 = random.randint(0, count1 - 1)
        except:
            activity1 = None

        # swap value 2
        day2 = random.randint(0, 4)
        timeslot2 = random.randint(0, 3) #niet 17:00-19:00
        count2 = len(table[timeslot2][day2])
        try:
            activity2 = random.randint(0, count2 - 1)
        except:
            activity2 = None

    
        if count1*count2 != 0:
            tmp = table[timeslot1][day1][activity1]
            table[timeslot1][day1][activity1] = table[timeslot2][day2][activity2]
            table[timeslot2][day2][activity2] = tmp

            #print "niks leeg"
            #print tmp.name, day1, timeslot1
            #print table[timeslot1][day1][activity1].name, day2, timeslot2
            
        elif count1 == 0 and count2 != 0:
            table[timeslot1][day1].append(table[timeslot2][day2][activity2])
            del table[timeslot2][day2][activity2]

            #print "2 leeg"
            #print table[timeslot1][day1][0].name
            
        elif count1 != 0 and count2 == 0:
            table[timeslot2][day2].append(table[timeslot1][day1][activity1])
            del table[timeslot1][day1][activity1]

            #print "1 leeg"
            #print table[timeslot2][day2][0]

        new_schedule = copy.deepcopy(schedule) # otherwise we get pointer problems
        new_schedule = new_schedule.update_timetable(table)

        new_score = new_schedule.score()

        if new_score == 0:
            print "we have encountered a terrible error"
            return 1

        #--------------------------stop in swapfunctie-------------------

        compare = random.uniform(0, 1)

        if T > 0:
            SA_value = math.exp(-(score - new_score)/T)
        else:
            SA_value = 1

        
        
        if new_score > score:
            score = new_score
            schedule = new_schedule
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

            if T > 0:
                SA_value = math.exp(-(score - new_score)/T)
            else:
                SA_value = 1

            
            
            if new_score > score:
                score = new_score
                schedule = new_schedule
            elif compare <= SA_value:
                score = new_score
                schedule = new_schedule
                
            else:
                table = schedule.get_timetable()

    return schedule

            
                                            
    

        
        
        

        

        
        
    
    
