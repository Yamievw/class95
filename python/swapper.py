import copy # for schedule class.
import random # for the random selection.
from roadmap import roadmap
from read_data import *


def swap_activity(schedule):
    """ this function moves an activity from one place to the other """
    table = copy.deepcopy(schedule.get_timetable())


    activity1 = None

    while activity1 == None:
        day1 = random.randint(0,4)
        timeslot1 = random.randint(0, 4) # wel 17:00-19:00.
        count1 = len(table[timeslot1][day1])

        if count1 == 0:
            continue
        else:
            index1 = random.randint(0, count1 - 1)
            activity1 = table[timeslot1][day1][index1]


    # swap value 2
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

  
# Swap roooms
def swap_rooms(schedule, no_swaps=1):
    table = copy.deepcopy(schedule.get_timetable())

    day = random.randint(0,4)
    timeslot = random.randint(0,4)
    count = len(table[timeslot][day])
    while count < 2:
        day = random.randint(0,4)
        timeslot = random.randint(0,4)
        count = len(table[timeslot][day])
        
    
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
    
    # TESTEN
    #print "ben r1,1", activity1.room.get_name(), room1
    #print "ben r2,1", activity2.room.get_name(), room2

    swap_room = room1

    # make swap:
    activity1.update_room(room2)
    activity2.update_room(swap_room)

    # update table:
    table[timeslot][day][i] = activity1
    table[timeslot][day][j] = activity2

    # TESTEN
    #print "ik ben r1 na swap", activity1.room, activity1.room.get_name()
    #print "ik ben r2 na swap", activity2.room, activity2.room.get_name()

    # update i
    i += 1

    # update schedule.
    new_schedule = copy.deepcopy(schedule)  # otherwise we get pointer problems.
    new_schedule = new_schedule.update_timetable(table)

    return new_schedule



# OUDDDDDDDDDD

# def swap_room(schedule, no_swaps=1):
#     """ this function moves a specified number of rooms from one
#              activity to an activity of same type and name """
#     table = copy.deepcopy(schedule.get_timetable())
#     schedule_roadmap = roadmap(schedule)
#     # schedule_roadmap geeft coordinaten van alle activiteiten
#     # print "ben schedule", schedule_roadmap
#     # activities zijn nu alle tutorials en labs
#     activities = schedule_roadmap.keys()
#     # geeft keys uit roadmap => lectures, labs, tutorials
#     # print "ben acti", activities


#     # define the number of swaps
#     i = 0
#     while i < no_swaps:
#         n = random.randint(0, len(activities) - 1)
#         coordinates = schedule_roadmap[activities[n]]
#         print "ben co", coordinates

#         no_activities = 
#         # voor no activities willen we het aantal activiteiten in tijdslot 
#         print no_activities

#         if no_activities <= 1:
#             continue
#         elif no_activities >= 2:
#             a = random.randint(0, no_activities - 1)
#             b = random.randint(0, no_activities - 1)
#             # we need unique numbers.
#             while a == b:
#                 b = random.randint(0, no_activities - 1)

#         # coordinates is a list of (day, timeslot, index) objects. We choose the
#         # a-th and b-th elements therein and then index them by (1, 0, 2) respectively.
#         activity1 = table[coordinates[a][1]][coordinates[a][0]][coordinates[a][2]]
#         activity2 = table[coordinates[b][1]][coordinates[b][0]][coordinates[b][2]]
#         print activity1, activity2

#         room1 = activity1.room
#         print "ben r1,1", activity1.room.get_name(), room1
#         room2 = activity2.room
#         print "ben r2,1", activity2.room.get_name(), room2

#         swap_room = room1
#         print "ik ben swap_room",swap_room
#         capacity= room1.get_capacity()

#         # check of het past
#         # hoeft niet per se => geen hard constraint
#         if len(activity2.participants) <= capacity:
#             # make swap:
#             activity1.update_room(room2)
#             print "ik ben r1 na swap", activity1.room, activity1.room.get_name
#             activity2.update_room(swap_room)
#             print "ik ben r2 na swap", activity2.room, activity2.room.get_name

#             # update table:
#             table[coordinates[a][1]][coordinates[a][0]][coordinates[a][2]] = activity1
#             table[coordinates[b][1]][coordinates[b][0]][coordinates[b][2]] = activity2

#             # update i
#             i += 1

#     # update schedule.
#     new_schedule = copy.deepcopy(schedule)  # otherwise we get pointer problems.
#     new_schedule = new_schedule.update_timetable(table)

#     return new_schedule
