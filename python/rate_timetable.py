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
    score += check_room(timetable)
    
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

def check_room(timetable):
    """Checks if a room in a timeslot only contains 1 component and
        if the number of students dont pass max capacity"""
    room = 0
    for day in range(5):
        for timeslot in range(5):
            for activity in timetable[timeslot][day]:
                room = activity.room
                if courses.components in room > 1:
                    room += 1
                if len(activity.participants) > room.capacity:
                    room += 1
                    
    return room   

def check_bonus(timetable):
    bonus = 20

    schedule = random_table()
    mapp = roadmap(schedule)
    true_set = mapp[course.components]

    set1 = timetable[0] and timetable[3] # ma-do
    set2 = timetable[1] and timetable[4] # di-vrij
    set3 = timetable[0] and timetable[2] and timetable[4] #ma-woe-vrij
    set4 = timetable[0] and timetable[1] and timetable[3] and timetable[4] #ma-di-do-vrij

    for day in range(7):
        for activity in timetable[day]:
            if true_set == 2:
                if true_set != set1:
                    bonus -= 5
                    print bonus
                if true_set != set2:
                    bonus -= 5
                    print bonus
            if true_set == 3:
                if true_set != set3:
                    bonus -= 5
                    print bonus
            if true_set == 4:
                if true_set != set4:
                    bonus -= 5
                    print bonus
    return bonus

                
                
                
            
        

