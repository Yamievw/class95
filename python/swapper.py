# Module that allows the shuffling of objects in the timetable.
# Necessary for HC and SA. 

import copy # for schedule class.
import random # for the random selection.
from roadmap import roadmap
from read_data import *


def swap_activity(schedule):
    """ this function moves an activity from one place to the other """
    table = copy.deepcopy(schedule.get_timetable())
    activity1 = None

    # swap value 1.
    while activity1 == None:
        day1 = random.randint(0,4)
        timeslot1 = random.randint(0, 4) # wel 17:00-19:00.
        count1 = len(table[timeslot1][day1])

        if count1 == 0:
            continue
        else:
            index1 = random.randint(0, count1 - 1)
            activity1 = table[timeslot1][day1][index1]

    # swap value 2.
    day2 = random.randint(0, 4)
    timeslot2 = random.randint(0, 4) # wel 17:00-19:00. 
  
    while schedule.slot_full(day2, timeslot2) or (timeslot2 == 4 and schedule.evening_full(day2)):
        day2 = random.randint(0, 4)
        timeslot2 = random.randint(0, 4)
   
    free_room_name = schedule.free_rooms(day2, timeslot2)[0]
    activity1.update_room(rooms[free_room_name])

    del table[timeslot1][day1][index1]
    table[timeslot2][day2].append(activity1)

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

        participants1 = activity1.group.participants
        participants2 = activity2.group.participants

        # HARD CONSTRAINT: maximum capacity of tutorial/lab.
        if len(participants1) == 1: # minimum occupancy
            continue
        if len(participants2) >= activity2.capacity:
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

  
# Swap roooms
def swap_rooms(schedule, no_swaps=1):
    """ moves activities between rooms. """
    table = copy.deepcopy(schedule.get_timetable())

    # choose a timeslot with at least 2 activities. 
    day = random.randint(0,4)
    timeslot = random.randint(0,4)
    count = len(table[timeslot][day])
    while count < 2:
        day = random.randint(0,4)
        timeslot = random.randint(0,4)
        count = len(table[timeslot][day])
        
    # choose two activities. 
    i = random.randint(0, count - 1)
    j = random.randint(0, count - 1)
    while j == i:
        j = random.randint(0, count - 1)
    
    # coordinates is a list of (day, timeslot, index) objects. We choose the
    # a-th and b-th elements therein and then index them by (1, 0, 2) respectively.
    activity1 = table[timeslot][day][i]
    activity2 = table[timeslot][day][j]
    #print activity1, activity2

    room1 = activity1.room
    room2 = activity2.room

    # find free rooms and set up a chance. 
    free_rooms = schedule.free_rooms(day, timeslot)
    new_room_chance = random.randint(0, 6)

    # either swap or take a new room, depending on how many rooms are still available.
    # Choice is random chance. 
    if new_room_chance > (6 - len(free_rooms)):
        random_room = rooms[free_rooms[random.randint(0, len(free_rooms) -1)]]
        activity1.update_room(random_room)
        table[timeslot][day][i] = activity1
    
    else:
        swap_room = room1

        # make swap:
        activity1.update_room(room2)
        activity2.update_room(swap_room)

        # update table:
        table[timeslot][day][i] = activity1
        table[timeslot][day][j] = activity2

    # update schedule.
    new_schedule = copy.deepcopy(schedule)  # otherwise we get pointer problems.
    new_schedule = new_schedule.update_timetable(table)

    return new_schedule
