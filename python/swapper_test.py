from random_table import *
from swapper import *
from roadmap import roadmap

schedule = random_table()
# print schedule
for i in range(200):
    schedule = swap_student(schedule)
# print schedule

mapp = roadmap_course(schedule)
coors = mapp["Algoritmen en complexiteit"]

def get(table, coor):
    return table[coor[1]][coor[0]][coor[2]]


table = schedule.timetable
for coor in coors:
    activity = get(table, coor)
    print activity.ttype, activity.group_id
    print activity.participants
    
    if activity.ttype != "lectures":
        print "----------------------"
        print activity.group.get_participants()
    print "@@@@@@@@@@@@@@@@@@@@@@@@@@"
    
