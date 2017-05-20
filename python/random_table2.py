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
    rooms_test = rooms.values()

    # for i in range(7):
    #     print rooms_test[i]
    # print rooms_test

    for course in courses_test:
        components = course.get_components()
        registrants = course.get_registrants()
        # shuffling registrants for truly random table.
        random.shuffle(registrants)
        # print "lenreg", len(registrants)
        course_name = course.get_name()
        available_rooms = []
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
                room = 1
                if key == "lectures":
                    group_id = 0                
                activity = Activity(name, ttype, capacity, group_id, room)
                if key == "lectures":
                    activity.update_participants(registrants)
                else:
                    activity.update_participants(groups[i])
                activities.append(activity)

                # Voor elke activiteit in activities
                #  if activity.participants <= room.capacity:
                        # append room in lijst available rooms
                        # activity.update_room(kamer uit lijst available rooms)
                        #  

                # OM TE TESTENN!
                # print len(groups[i]), n,  activity.capacity, len(activity.participants)
                # print activity.name, activity.ttype, activity.group_id

    for activity in activities:
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

        # print "ik ben ",activity.name, activity.ttype, activity.group_id

        # activity.update_room(rooms_test[i])

    # available_rooms_per_timeslot = []
    # available_per_capacity = []
        timetable = test.get_timetable()
        for day in range(5):
            for timeslot in range(5):
                taken_rooms = []
                for activity in timetable[timeslot][day]:
                    i = random.randint(0,6)
                    while i not in taken_rooms:
                        taken_rooms.append(i)
                        activity.update_room(rooms_test[i])












                # for room in rooms_test:
                #     room_capacity = room.get_capacity()
                #     if activity.participants <= room.capacity:
                #         room = room.get_name()
                #         available_rooms.append(room)
                #         # print "ik ben ar 1", len(available_rooms)
                # activity.update_room(available_rooms[0])
                # available_rooms.pop(0)
                # print "ik ben ar 2", len(available_rooms)

    print "ik ben het type", type(activity.room)

    print "ik ben ",activity.name, activity.ttype, activity.group_id, activity.room

                

    return test

# OM TE TESTENN!
oef = random_table()
print oef