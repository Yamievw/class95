import copy # for schedule class
import random # for the sa randomness


def swap_activity(schedule):
    table = copy.deepcopy(schedule.get_timetable())
    
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
  
    
    if activity1 != None:
        table[timeslot2][day2].append(table[timeslot1][day1][activity1])
        del table[timeslot1][day1][activity1]
    else:
        return schedule

    new_schedule = copy.deepcopy(schedule) # otherwise we get pointer problems
    new_schedule = new_schedule.update_timetable(table)

    return new_schedule

