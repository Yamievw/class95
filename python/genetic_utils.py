from operator import itemgetter

def score_sort(population):
    """ sorts a given population by its score """

    
    
    # score schedules in population
    scored = []
    for schedule in population:
        scored.append((schedule, schedule.score()))
        
    # sort by second element in tuple, namely the score. Sort descending.
    scored = sorted(scored, key=itemgetter(1), reverse=True)
    
    # list comprehension to return list of schedules.
    output = [i[0] for i in scored]
    return output


