# creates a randomized timetable, with students.

from read_data import *
from schedule import *
import math
import random
from roadmap import roadmap

def random_table():
    courses_test = courses.values()
    activities = [] 
    test = Schedule()


    # voor elke course
    for course in courses_test:
        components = course.get_components()
        registrants = course.get_registrants()

        for key in components:

            if key == 'lectures':
                n = 1
            else:
                n = components[key][0]

            # range(comp[key]) => aantal groepen
            groups = [registrants[i::n] for i in range(n)]

            for i in range(n):
                group_id = str(i + 1)
                name = course.get_name() + "_" + key + "_" + group_id
                ttype = key
                capacity = components[key][1]
                activity = Activity(name, ttype, capacity, group_id)
                activity.update_participants(groups[i])
                activities.append(activity)

                # OM TE TESTENN!
                # print len(groups[i]), n
                # print activity.name, activity.ttype, activity.capacity, activity.group_id, len(activity.participants)


    for activity in activities:
        # TO DO: Voeg hier een for-loop toe om een activity meerdere dagen toe te voegen (bijv. 2 labs per week)
        i = random.randint(0, 4)
        j = random.randint(0, 4)  # wel evening timeslot.
        test.add_activity(i, j, activity)

    return test

# OM TE TESTENN!
# oef = random_table()
# print oef