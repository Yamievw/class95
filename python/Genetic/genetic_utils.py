from operator import itemgetter
from rate_timetable import *

def assess(population, population_size):
    N = float(len(population))  

    # sanity check: population size. 
    if N != population_size:
        return 0
    
    max_score = score_sort(population)[0].score()

    tot_score = 0
    for schedule in population:
        tot_score += schedule.score()
    ave_score = tot_score/N

    sdev = 0
    for schedule in population:
        sdev += (ave_score - schedule.score())**2
        
    
    try:
        sdev = math.sqrt(sdev/N)
    except ValueError:
        sdev = 0
        
    return max_score, ave_score, sdev

def score_sort(population, crit="score"):
    """ sorts a given population by its score """


    # score schedules in population
    scored = []

    if crit == "score":
        for schedule in population:
            scored.append((schedule, schedule.score()))
    elif crit == "student":
        for schedule in population:
            scored.append((schedule, check_conflict(schedule.timetable)))
    elif crit == "block":
        for schedule in population:
            scored.append((schedule, check_day(schedule.timetable)))

    
        
    # sort by second element in tuple, namely the score. Sort descending.
    scored = sorted(scored, key=itemgetter(1), reverse=True)

    
    # list comprehension to return list of schedules.
    output = [i[0] for i in scored]
    
    return output

##  test code:
##
##from random_table import *
##population = []
##for i in range(10):
##    population.append(random_table())
##
##score_sort(population, "student")
##print '' 
##score_sort(population, "block")
