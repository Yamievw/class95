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
        j = random.randint(0, 4)  # wel evening timeslot.
        test.add_activity(i, j, activity)

    #test = add_students(test)
    test = add_students2(test)
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






def add_students2(schedule):
    # zie http://stackoverflow.com/questions/48087/select-n-random-elements-from-a-listt-in-c-sharp
    # voor randomization.
    
    table = schedule.get_timetable()
    schedule_roadmap = roadmap(schedule)
    
    for key in schedule_roadmap:
        coor = schedule_roadmap[key]
        no_groups = len(coor)
        # day, timeslot, activity number
        course_name = key.split("_", 1)[0]
        registrants = courses[course_name].get_registrants()

        
        
        # get capacity from first instance of activity
        activity1 = table[coor[0][1]][coor[0][0]][coor[0][2]]
        capacity = activity1.get_capacity()
        units_per_student = courses[course_name].per_student[str(activity1.type)]
        
        registrants_per_activity = units_per_student*int(math.ceil(len(registrants)/float(no_groups)))
        
        for i in range(len(coor)):
            activity = table[coor[i][1]][coor[i][0]][coor[i][2]]        
            begin = (i)*registrants_per_activity
            end = (i+1)*registrants_per_activity
            activity.update_participants(registrants[begin:end])
            table[coor[i][1]][coor[i][0]][coor[i][2]] = activity
            
    schedule.update_timetable(table)
    return schedule


 
        

    
    
