from genetic_utils import *
import math
from swapper import *


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
    mut_count = population_size*mut_frac
    cro_count = population_size*cro_frac

    

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
    return children
        

def cross(survivors, N):
    """ this function crosses a fraction of the surviving population """
    children = []

    return children
    
    
    
    
    
    
