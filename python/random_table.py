# creates a randomized timetable, with students.

from read_data import *
from schedule import *
import math
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

    test = add_students(test)

    return test

def add_students(schedule):
    timetable = schedule.timetable
    for day in range(5):
        for timeslot in range(5):
            for activity in timetable[timeslot][day]:
                if activity.type == "lectures":
                    activity.add_participants(courses[activity.name].get_registrants())
                else:
                    make_groups(activity, timetable)
    return schedule


def make_groups(activity, timetable):
    data = []
    students = courses[activity.name].get_registrants()
    for student in students:
        data.append(student)

    maxsize = int(activity.get_capacity())

    n = math.ceil(float(len(data))/(maxsize))
    n = int(n)

    groups = [data[i::n] for i in range(n)]
    all_activities = []
    for i, group in enumerate(groups):
        name = activity.name + " (" + str(i + 1) + ")"
        new_activity = Activity(name, activity.type, activity.capacity, participants=group)
        all_activities.append(new_activity)

    return all_activities
