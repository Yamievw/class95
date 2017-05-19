from read_data import *
from schedule import *
from random_table2 import *
import random

courses_test = courses.values()

activities = []

test = Schedule()

##for course in courses_test:
##    components = course.get_components()
##    for key in components:
##        for i in range(components[key][0]):
##            name = course.get_name()
##            ttype = key
##            capacity = components[key][1]
##            
##            activities.append(Activity(name, ttype, capacity))
##        
##        
##
##for activity in activities:
##    i = random.randint(0, 4) 
##    j = random.randint(0, 3) # no evening timeslot.
##    test.add_activity(i, j, activity)
##    
##
##print "Uw score is: ", rate_timetable(test)
##print test
##### voorlopige conclusie: hij werkt! Hij kan checken of het een geldig rooster is. 
##
##
##def add_students(schedule):
##    timetable = schedule.timetable
##    for day in range(5):
##        for timeslot in range(5):
##            for activity in timetable[timeslot][day]:
##                if activity.type == "lectures":
##                    activity.add_participants(courses[activity.name].get_registrants())
##                # ook nog lectures & labs adden


import matplotlib.pyplot as plt


thing = []

for i in range(1000):
    test1 = random_table()
    test = test1.timetable
    score = check_bonus(test)
    thing.append(score)
    if score == max(thing):
        best = test1

print best
print best.score()
plt.hist(thing, bins=np.arange(min(thing), max(thing) + 10, 10))
plt.show()
    
    
##    
##    
##course= courses["Machine Learning"]
##ps = course.per_student
##
##print ps

