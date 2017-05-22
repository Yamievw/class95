import pickle
import os
from rate_timetable import *

date = "2017-05-22"
time = "16 59 16"
filename = "0"

dirname = os.getcwd()
dirname += "\\Runs\\"
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
