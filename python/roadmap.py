# Makes a roadmap, so activities can be efficiently found in the schedule object. 

def roadmap(schedule, lectures_bool=True):
    """ roadmap for different types of activities for all courses. """

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


def roadmap_course(schedule):
    """  roadmap for all activities (labs, tutorials, lectures) for all courses. """
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
                try:
                    # append coordinates
                    roadmap[act_name].append((day, timeslot, i)) 
                except KeyError:
                    roadmap[act_name] = [(day, timeslot, i)]
                i += 1
    return roadmap

# test code. 
## schedule = random_table()
## mapp = roadmap(schedule)
## print mapp["Advanced Heuristics_labs"]
