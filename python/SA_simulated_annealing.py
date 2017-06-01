### implements a simulated annealing algorithm

from SA_cooling import *
from roadmap import roadmap
from swapper import *

import copy # for schedule class
import math # for the exp()
import random # for the sa randomness



def SA_activities(schedule, cooling, T0, iterations=1):
    """ runs a simulated annealing algorithm on the activities. """
    table = copy.deepcopy(schedule.get_timetable()) # against pointer errors.
    score = schedule.score()

    for i in range(iterations):
        # cool
        T = cool(cooling, T0, Tn, iterations, i)

        # move value randomly and assess new score. 
        new_schedule = swap_activity(schedule)
        new_score = new_schedule.score()
        compare = random.uniform(0, 1)

        # Tmin is defined because exp(a/0) at T=0 gives a problem
        # Tmin is imported from cool.py.
        if T > Tmin:
            SA_value = math.exp(-(score - new_score)/T)
        else:
            SA_value = 0

        # accept better solutions. 
        if new_score > score:
            score = new_score
            schedule = new_schedule

        # random chance. 
        elif compare <= SA_value:
            score = new_score
            schedule = new_schedule

        # start again. 
        else:
            table = schedule.get_timetable()

    return schedule

def SA_students(schedule, cooling, T0, iterations=1):
    """ runs a simulated annealing algorithm on the students. """
    table = copy.deepcopy(schedule.get_timetable()) # against pointer errors.
    score = schedule.score()  

    for k in range(iterations):
        T = cool(cooling, T0, Tn, iterations, k)

        # swap and score. 
        new_schedule = swap_student(schedule)
        new_score = new_schedule.score()

        # random chance. 
        compare = random.uniform(0, 1)

        # Tmin is defined because exp(a/0) at T=0 gives a problem
        # Tmin is imported from cool.py.
        if T > Tmin:
            SA_value = math.exp(-(score - new_score)/T)
        else:
            SA_value = 0

        # accept better schedule. 
        if new_score > score:
            score = new_score
            schedule = new_schedule

        # random chance
        elif compare <= SA_value:
            score = new_score
            schedule = new_schedule
            
        else:
            table = schedule.get_timetable()

    return schedule

            
def SA_rooms(schedule, cooling, T0, iterations=1):
    """ runs a simulated annealing algorithm on the rooms. """

    table = copy.deepcopy(schedule.get_timetable()) # against pointer errors.
    score = schedule.score()

    for k in range(iterations):
        T = cool(cooling, T0, Tn, iterations, k)

        # swap and score. 
        new_schedule = swap_room(schedule)
        new_score = new_schedule.score()
    
        compare = random.uniform(0, 1)

        # Tmin is defined because exp(a/0) at T=0 gives a problem
        # Tmin is imported from cool.py.
        if T > Tmin:
            SA_value = math.exp(-(score - new_score)/T)
        else:
            SA_value = 0

        # accept better solution. 
        if new_score > score:
            score = new_score
            schedule = new_schedule

        # random chance
        elif compare <= SA_value:
            score = new_score
            schedule = new_schedule
            
        else:
            table = schedule.get_timetable()

    return schedule                                      
    

        
        
        

        

        
        
    
    
