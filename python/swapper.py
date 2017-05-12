import copy # for schedule class.
import random # for the random selection.
from roadmap import roadmap


def swap_activity(schedule):
    """ this function moves an activity from one place to the other """
    table = copy.deepcopy(schedule.get_timetable())
    
    day1 = random.randint(0, 4)
    timeslot1 = random.randint(0, 4) # wel 17:00-19:00.
    count1 = len(table[timeslot1][day1])
    try:
        activity1 = random.randint(0, count1 - 1)
    except:
        activity1 = None

    # swap value 2
    day2 = random.randint(0, 4)
    timeslot2 = random.randint(0, 4) # wel 17:00-19:00. 
  
    
    if activity1 != None:
        table[timeslot2][day2].append(table[timeslot1][day1][activity1])
        del table[timeslot1][day1][activity1]
    else:
        return schedule

    new_schedule = copy.deepcopy(schedule) # otherwise we get pointer problems.
    new_schedule = new_schedule.update_timetable(table)

    return new_schedule

def swap_student(schedule, no_swaps=1):
    """ this function moves a specified number of student form one
         activity to an activity of same type and name """
    table = copy.deepcopy(schedule.get_timetable())
    schedule_roadmap = roadmap(schedule, False)
    activities = schedule_roadmap.keys()

    # define the number of swaps
    i = 0
    while i < no_swaps:
        n = random.randint(0, len(activities)-1)
        coordinates = schedule_roadmap[activities[n]]

        no_activities = len(coordinates)
        
        if no_activities <= 1:
            continue
        elif no_activities >= 2:
            a = random.randint(0, no_activities - 1)
            b = random.randint(0, no_activities - 1)
            # we need unique numbers. 
            while a == b:
                b = random.randint(0, no_activities - 1)
    
        # coordinates is a list of (day, timeslot, index) objects. We choose the
        # a-th and b-th elements therein and then index them by (1, 0, 2) respectively.
        activity1 = table[coordinates[a][1]][coordinates[a][0]][coordinates[a][2]]
        activity2 = table[coordinates[b][1]][coordinates[b][0]][coordinates[b][2]]

        participants1 = activity1.participants
        participants2 = activity2.participants

        # HARD CONSTRAINT: maximum capacity of tutorial/lab.
        if len(participants1) == 1: # minimum occupancy
            #print activity1, n
            #print "Minimum participants1"
            continue
        if len(participants2) >= activity2.capacity:
            #print "Max capacity 2"
            continue

        swap_student = participants1[random.randint(0, len(participants1) - 1)]

        
        
        if swap_student not in participants2:
            # succesfull swap, yay!
            i += 1
        

            # move to new group and remove from old group.
            participants2.append(swap_student)
            participants1.remove(swap_student)

        
            
            # update activities.
            activity1.update_participants(participants1)
            activity2.update_participants(participants2)

            # update table.
            table[coordinates[a][1]][coordinates[a][0]][coordinates[a][2]] = activity1 
            table[coordinates[b][1]][coordinates[b][0]][coordinates[b][2]] = activity2

        
            
    # update schedule.
    new_schedule = copy.deepcopy(schedule) # otherwise we get pointer problems.
    new_schedule = new_schedule.update_timetable(table)

            
    return new_schedule

        
        
        
        
        

    
    
