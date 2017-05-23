import pickle
import os
from rate_timetable import *

ttype = "HC"
date = "2017-05-23"
time = "00 16 37"
filename = "0 score=1270"

dirname = os.getcwd()
dirname += "\\Runs\\"
dirname += ttype
dirname += "\\
dirname += date
dirname += "\\"
dirname += time
dirname += "\\"
dirname += filename


file_pi2 = open(dirname, 'r') 
schedule = pickle.load(file_pi2)
table = schedule.timetable

print check_day(table)
print check_conflict(table)
print check_room(table)
print check_bonus(table)
schedule.plot()
