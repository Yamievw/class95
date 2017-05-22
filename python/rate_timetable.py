# rates any schedule, assuming a 5x5 matrix with activity 
# objects in the timeslots. 
import numpy as np

from read_data import *
from roadmap import *

def make_checklist(courses=courses):
    # creates a dictionary that keeps track of necessary timeslots per
    # course. e.g. {"Compilerbouw" : 5}. Standard input is our previous
    # "courses" list, but simpler examples may be used for testing
    
    course_checklist = {}
    
    for course in courses.values():
        components = course.get_components()
        for key in components.keys():
            course_checklist[course.get_name() + "_" + str(key)] = int(components[key][0])
        

    return course_checklist
    




def rate_timetable(timetable):
    # scores the timetable. First checks if the schedule is
    # valid, then adds/subtracts bonus/malus points.
    checklist = make_checklist() #create course checklist
    score = 1000
    
    for day in range(5):
        for timeslot in range(5):
            for activity in timetable[timeslot][day]:
                try:
                    # cross one activity off the checklist
                    name = activity.get_name() + "_" + activity.get_type()
                    checklist[name] = checklist[name] - 1
                except KeyError:
                    print "Something went horribly wrong"
                    return None
    
    
    for value in checklist.values():
        # stop checking if it's an invalid schedule
        if value != 0:
            score = 0
            return score

    score += check_day(timetable)
    score += check_conflict(timetable)
    score += check_bonus(timetable)
    score += check_evening(timetable)    
    score += check_room(timetable)
    
    return score


def check_day(timetable):
    """ Checks if a subject is scheduled more
        than once a day. """
    score_day = 0
    
    for day in range(5):
        day_check = {}
        for timeslot in range(5):
            for activity in timetable[timeslot][day]:
                name = activity.name
                group_id = int(activity.group_id)
                
                try:
                    counters = day_check[name]
                    counters[group_id] = counters[group_id] + 1
                    day_check[name] = counters
                except KeyError:
                    no_groups = courses[name].no_groups
                    counters = np.zeros(no_groups+1)
                    counters[group_id] = 1
                    day_check[name] = counters

        for key in day_check.keys():
            counters = day_check[key]
            if counters[0] > 1:
                score_day -= (10*(counters[0] - 1))
            no_groups = courses[key].no_groups
##            if counters[0] > 1:
##                print key, "lectures", counters, score_day
            for group_id in range(1, len(counters)):
                if counters[0] > 0 and counters[group_id] > 0:
                    score_day -= (10./no_groups*counters[group_id])
##                    print key, "combination", counters, score_day
                elif counters[0] == 0 and counters[group_id] > 1:
                    score_day -= (10./no_groups*(counters[group_id] - 1))
##                    print key, "just groups", counters, score_day
        

    
    return score_day

def check_conflict(timetable):
    """ Checks timetable conflicts """
    conflicts = 0
    for day in range(5):
        for timeslot in range(5):
            check = None 
            for activity in timetable[timeslot][day]:
                if check != None:
                    for student in activity.participants:
                        if student not in check:
                            check.add(student)
                        else:
                            conflicts += 1
                else:
                    check = set(activity.participants)
                 
    return -conflicts

def check_room(timetable):
    """Checks if the number of students dont pass max capacity of a room"""
    
    roomm = 0
    
    for room in rooms.values():
        capacity = room.get_capacity()

    for day in range(5):
        for timeslot in range(5):
            for activity in timetable[timeslot][day]:
                if len(activity.participants) > capacity:
                    roomm = (capacity-(len(activity.participants))) #punt per student
                    
    return roomm

def check_evening(timetable):
    score_evening = 0
    for day in range(5):
        for activity in timetable[4][day]:
            score_evening -= 50
    return score_evening

def check_bonus(timetable):
    
    mapp = roadmap_course(timetable)

    bonus = 0

    two_units1 = [0, 3]
    two_units2 = [1, 4]
    three_units = [0, 2, 4]
    four_units = [0, 1, 3, 4]

    for key in mapp:
        # find out how many groups there are and the amount of activities per student. 
        no_groups = courses[key].no_groups
        no_units = courses[key].per_student["all"]

        # workaround for courses without labs or tutorials. 
        if no_groups == 0:
            no_groups = 1

        # we only look at 2 to 4 activities per student. 
        if no_units < 2 or no_units > 4:
            continue
            
        for test_id in range(1, no_groups + 1):

            # fill this list with the configuration of this subject and group. 
            current = []
            
            for coor in mapp[key]:
                activity = get_activity(coor, timetable)
                group_id = int(activity.group_id)

                day = coor[0]
                                
                if group_id == 0 or group_id == test_id:
                    current.append(day)

            if no_units == 2 and (current == two_units1 or current == two_units2):
                bonus += 20./no_groups
            elif no_units == 3 and current == three_units:
                bonus += 20./no_groups
            elif no_units == 4 and current == four_units:
                bonus += 20./no_groups
    return bonus
                
                
def get_activity(coor, table):
    return table[coor[1]][coor[0]][coor[2]]       
            
            
                
                
            
        

