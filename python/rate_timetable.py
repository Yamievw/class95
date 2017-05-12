# rates any schedule, assuming a 5x5 matrix with activity 
# objects in the timeslots. 

from read_data import *

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
    
    return score


def check_day(timetable):
    """ Checks if a subject is scheduled more
        than once a day. """
    score = 0
    for day in range(5):
        daycheck = {}
        for timeslot in range(5):
            for activity in timetable[timeslot][day]:
                name = activity.name
                try:
                    daycheck[name] = daycheck[name] + 1
                except KeyError:
                    daycheck[name] = 1

        for value in daycheck.values():
            if value > 1:
                score -= (value - 1)*10 #points deducted
    return score

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

def check_conflictRooms(timetable):
    """Checks if a room in a timeslot only contains 1 component and
        if the number of students dont pass max capacity"""
    conflictRooms = 0
    for day in range(5):
        for timeslot in range(5):
            for rooms in timetable[timeslot][day]:
                if courses.components in rooms > 1:
                    conflictRooms += 1
                if len(activity.participants) > rooms.capacity:
                    conflicRooms += 1
                    
                    
def check_bonus(timetable):
    bonus = 0
    for day in range(5):
        for timeslot in range(5):
                
                
                
                
            
        

