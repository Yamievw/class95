# rates any schedule, assuming a 5x5 matrix with activity 
# objects in the timeslots. 

from read_data import *

def checklist(courses=courses):
    # creates a dictionary that keeps track of necessary timeslots per
    # course. e.g. {"Compilerbouw" : 5}. Standard input is our previous
    # "courses" list, but simpler examples may be used for testing
    
    course_checklist = {}
    
    for course in courses.values():
        components = course.get_components()
        for key in components.keys():
            course_checklist[course.get_name() + "_" + str(key)] = int(components[key][0])
        

    return course_checklist
    
course_checklist = checklist()



def rate_timetable(timetable, checklist=course_checklist):
    # scores the timetable. First checks if the schedule is
    # valid, then adds/subtracts bonus/malus points. 
    score = 1000
    timetable = timetable.get_timetable()
    for day in range(5):
        for timeslot in range(5):
            for activity in timetable[timeslot][day]:
                try:
                    # cross one activity off the checklist
                    name = activity.get_name() + "_" + activity.get_type()
                    checklist[name] = checklist[name] - 1
                except KeyError:
                    print "Er gaat iets flink mis"
                    return 0
    
    
    for value in checklist.values():
        # stop checking if it's an invalid schedule
        if value != 0:
            score = 0
            return score

    for day in range(5):
        daycheck = {}
        for timeslot in range(5):
            for activity in timetable[timeslot][day]:
                name = activity.name
                try:
                    daycheck[name] = daycheck[name] + 1
                    print activity.name, day, timeslot 
                except KeyError:
                    daycheck[name] = 1

        for value in daycheck.values():
            if value > 1:
                score -= (value - 1)*10 #points deducted
                    
        

    
    return score



              
                
                
            
        

