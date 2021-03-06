# creates a randomized timetable, with students.

from read_data import *
from schedule import *
import math
import random
# from roadmap import roadmap

def random_table():
    courses_test = courses.values()
    activities = [] 
    test = Schedule()
    rooms_test = rooms.values()
    groupies = []

    

    for course in courses_test:
        components = course.get_components()
        registrants = course.get_registrants()
        # shuffling registrants for truly random table.
        random.shuffle(registrants)
        course_name = course.get_name()
        available_rooms = []

        made_groups = False

        for key in components:
            units_per_student = courses[course_name].per_student[str(key)]
            n = components[key][0]
            if not made_groups and key != 'lectures' and n != 0:
                # print "groups made"
                groups = [Group(course_name + str(i+1), registrants[i::n]) for i in range(n)]
                made_groups = True
                # print "ben groups", groups, n, course_name, len(registrants)


            for i in range(n):
                group_id = str(i + 1)
                # print "ik ben group_id", group_id
                name = course.get_name()
                ttype = key
                # print "ben ttype", ttype
                capacity = components[key][1]
                # participants = groups[i]

                if key == "lectures":
                    group_id = 0
                
                activity = Activity(name, ttype, capacity, group_id)
                if key == "lectures":
                    activity.update_participants(registrants)
                else:
                    activity.update_participants(groups[i].get_participants())
                    activity.update_group(groups[i])
                    # print "ben name", groups[i].name
                activities.append(activity)
                    

    for activity in activities:
        # TO TEST:
        # if activity.ttype != "lectures":
        # print "ik ben:", activity.name, activity.ttype, activity.group.participants, activity.group_id, len(activity.participants)
        # else:
        # print "ik ben:", activity.name, activity.ttype, activity.group_id, len(activity.participants)

        for i in range(units_per_student):
            if units_per_student != 0:
                i = random.randint(0, 4)
                j = random.randint(0, 4)  # wel evening timeslot.

                # no more than one activity in the evening timeslot and max
                # occupation is seven. 
                while test.slot_full(i, j) or (j == 4 and test.evening_full(i)):
                    i = random.randint(0,4)
                    j = random.randint(0,4)
                test.add_activity(i, j, activity)

    timetable = test.get_timetable()
    for day in range(5):
        for timeslot in range(5):
            taken_rooms = []
            if (timeslot == 4) and (timetable[4][day] != []):
                evening_activity = timetable[4][day][0]
                evening_activity.update_room(rooms["C0.110"])
            else:
                for activity in timetable[timeslot][day]:
                    while i in taken_rooms:
                        i = random.randint(0,6)
                    taken_rooms.append(i)
                    activity.update_room(rooms_test[i])      

    return test

# OM TE TESTENN!
# oef = random_table()
# print oef
