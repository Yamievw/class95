# creates a randomized timetable, with students.

from read_data import *
from schedule2 import *
import math
import random
# from roadmap import roadmap

def random_table():
    courses_test = courses.values()
    # print "ik ben ct", len(courses_test)
    activities = [] 
    test = Schedule()

    for course in courses_test:
        components = course.get_components()
        registrants = course.get_registrants()
        # print "lenreg", len(registrants)
        course_name = course.get_name()
        # print course_name
        

        for key in components:
            units_per_student = courses[course_name].per_student[str(key)]
            n = components[key][0]
            groups = [registrants[i::n] for i in range(n)]

            for i in range(n):
                # "ik ben in range n"
                group_id = str(i + 1)
                name = course.get_name()
                ttype = key
                capacity = components[key][1]
                activity = Activity(name, ttype, capacity, group_id)
                if key == "lectures":
                    activity.update_participants(registrants)
                else:
                    activity.update_participants(groups[i])
                activities.append(activity)

                # OM TE TESTENN!
                # print len(groups[i]), n,  activity.capacity, len(activity.participants)
                # print activity.name, activity.ttype, activity.group_id

    for activity in activities:
        for i in range(units_per_student):
            if units_per_student != 0:
                i = random.randint(0, 4)
                j = random.randint(0, 4)  # wel evening timeslot.
                test.add_activity(i, j, activity)

    return test

# OM TE TESTENN!
# oef = random_table()
# print oef