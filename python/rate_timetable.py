# rates any schedule, assuming a 5x5 matrix with activity 
# objects in the timeslots. 

from read_data import *





def checklist(courses=courses):
    # creates a dictionary that keeps track of necessary timeslots per
    # course. e.g. {"Compilerbouw" : 5}. Standard input is our previous
    # "courses" list, but simpler examples may be used for testing
    
    course_checklist = {}


    return course_checklist
    
course_checklist = checklist()


def rate_timetable(timetable, checklist=course_checklist):
    # scores the timetable. First checks if the schedule is
    # valid, then adds/subtracts bonus/malus points. 
    
    for day in range(5):
        for timeslot in range(5):
            
        

