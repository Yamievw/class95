from read_data import *
from schedule import *
from random_table import *

import copy # to copy instance of Schedule class. 


def hill_climber_activities(schedule, iterations=1):

    table = copy.deepcopy(schedule.get_timetable()) # against pointer errors.
    score = schedule.score()
    for i in range(iterations):
        # swap value 1
        day1 = random.randint(0, 4)
        timeslot1 = random.randint(0, 4) #wel 17:00-19:00
        count1 = len(table[timeslot1][day1])
        try:
            activity1 = random.randint(0, count1 - 1)
        except:
            activity1 = None

        # swap value 2
        day2 = random.randint(0, 4)
        timeslot2 = random.randint(0, 4) #wel 17:00-19:00
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

        
        if new_score > score:
            score = new_score
            schedule = new_schedule
        else:
            table = schedule.get_timetable()

    return schedule



