# from random_table2 import *

def roadmap(schedule, lectures_bool=True):
    # allow for two types of input. 
    try:
        timetable = schedule.get_timetable()
    except:
        timetable = schedule

    roadmap = {}

    for day in range(5):
        for timeslot in range(5): #wel avondslot
            i = 0
            for activity in timetable[timeslot][day]:
                act_name = activity.get_name()
                act_type = activity.get_type()
                if act_type == "lectures" and not lectures_bool:
                    # skip lectures
                    i += 1
                    continue                   

                try:
                    # append coordinates
                    roadmap[act_name + "_" + act_type].append((day, timeslot, i)) 
                except KeyError:
                    roadmap[act_name + "_" + act_type] = [(day, timeslot, i)]
                i += 1
    return roadmap


# schedule = random_table()
# mapp = roadmap(schedule)
# print mapp["Advanced Heuristics_labs"]
