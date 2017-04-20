from read_data import *
from schedule import *
import random

courses_test = courses.values()



activities = []

test = Schedule()

for course in courses_test:
    components = course.get_components()
    for key in components:
        for i in range(components[key][0]):
            name = course.get_name()
            ttype = key
            capacity = components[key][1]
            
            activities.append(Activity(name, ttype, capacity))
        
        

for activity in activities:
    i = random.randint(0, 4)
    j = random.randint(0, 4)
    test.add_activity(i, j, activity)
    

print "Uw score is: ", rate_timetable(test)
print test
### voorlopige conclusie: hij werkt! Hij kan checken of het een geldig rooster is. 

    
    
    
    
