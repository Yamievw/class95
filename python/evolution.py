from genetic_utils import *
import math
from swapper import *
from roadmap import roadmap
import copy


def evolve(population, mut_frac=.5):
    """ main function that executes the evolution, being
        crossover and mutation """
    population_size = len(population) 

    # determine who gets to breed
    survivors = select(population)

    # sanity check. Minimum population size after selection. 
    if len(survivors) < 4:
        return 0

    

    # relative fraction of mutation vs crossover
    cro_frac = 1 - mut_frac
    mut_count = int(population_size*mut_frac)
    cro_count = int(population_size*cro_frac)   

    # make sure population is restored to original size. 
    if mut_count + cro_count != population_size:
        mut_count += population_size - (mut_count + cro_count)

    # our new population
    next_generation = []

    next_generation += mutate(survivors, mut_count)   
    next_generation += cross(survivors, cro_count)

    return next_generation

def select(population):
    """ determine who gets to breed """
    # sort by score 
    score_sort(population)
    population_size = len(population)

    survival_rate = .2
    survivors = population[:int(math.ceil(survival_rate*population_size))]

    return survivors
    

def mutate(survivors, N):
    """ this function creates offspring with random mutations """
    children = []
    # ensure sufficient children, with preference given to first in survivors. 
    while len(children) < N:
        for survivor in survivors:
            # move one activity and ten students. Activity may not be moved due to implementation.
            child = swap_activity(survivor)
            child = swap_student(survivor, 3)
            children.append(child)
            if len(children) == N:
                break
            
    return children
        

def cross(survivors, N):
    """ this function crosses a fraction of the surviving population """
    children = []
    
    best_block = score_sort(survivors, "block")
    best_student = score_sort(survivors, "student")

    
    maximum = 0
    while len(children) < N:
        for i in range(maximum + 1):
            schedule1 = best_block[i]
            schedule2 = best_student[maximum]

            if i == maximum:
                if schedule1 != schedule2:
                    children.append(cross_block_student(schedule1, schedule2))
                if len(children) == N: # make sure we don't get too many babies. 
                    break
                maximum = (maximum + 1) % len(survivors) # ensure we don't go too high. 
                

            # cross both ways.
            else: 
                if schedule1 != schedule2:
                    children.append(cross_block_student(schedule1, schedule2))
                    if len(children) == N: # make sure we don't get too many babies. 
                        break

                schedule1 = best_block[maximum]
                schedule2 = best_student[i]
                if schedule1 != schedule2:
                    children.append(cross_block_student(schedule1, schedule2))
                    if len(children) == N: # make sure we don't get too many babies. 
                        break

    return children
    
    
    
def cross_block_student(schedule1, schedule2):
    """ crosses two schedules, keeping the first's block schedule and
        the second's student groups """

    table1 = copy.deepcopy(schedule1.timetable)
    table2 = copy.deepcopy(schedule2.timetable)
    roadmap2 = roadmap(schedule2)
    

    for day in range(5):
        for timeslot in range(5):
            activities1 = table1[timeslot][day]
            for i in range(len(activities1)):
                # get activity1
                activity1 = activities1[i]                 
                activity1_name = str(activity1.name) + "_" + str(activity1.type)

                

                # get activity2
                coor2 = roadmap2[activity1_name][0]
                activity2 = table2[coor2[1]][coor2[0]][coor2[2]]

                

                #swap participants
                participants2 = activity2.participants
                activity1.update_participants(participants2)
                table1[timeslot][day][i] = activity1
                
    baby = copy.deepcopy(schedule1) # otherwise we get pointer problems.
    baby = baby.update_timetable(table1)

    return baby

        
                
                
                
    
    
