from read_data import *
from schedule import *
from random_table import *
from swapper import *

import copy # to copy instance of Schedule class. 


def hill_climber_activities(schedule, iterations=1):

    
    score = schedule.score()
    for i in range(iterations):        
        new_schedule = swap_activity(schedule)

        new_score = new_schedule.score()
       
        if new_score > score:
            score = new_score
            schedule = new_schedule
        else:
            table = schedule.get_timetable()

    return schedule

def hill_climber_students(schedule, iterations=1):
    
    score = schedule.score()
    for i in range(iterations):
        new_schedule = swap_student(schedule)
        new_score = new_schedule.score()

        if new_score > score:
            score = new_score
            schedule = new_schedule
        else:
            table = schedule.get_timetable()

    return schedule

def hill_climber_rooms(schedule, iterations=1):
    
    score = schedule.score()
    for i in range(iterations):
        new_schedule = swap_rooms(schedule)
        new_score = new_schedule.score()

        if new_score > score:
            score = new_score
            schedule = new_schedule
        else:
            table = schedule.get_timetable()

    return schedule