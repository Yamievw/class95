# creates a randomized timetable, without students.

from read_data import *
from schedule import *

import random

def random_table():
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
        j = random.randint(0, 3)  # no evening timeslot.
        test.add_activity(i, j, activity)

    return test

