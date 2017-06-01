import pickle
import os
from rate_timetable import *

##ttype = "HC"
##date = "2017-05-29"
##time = "17 27 10"
##filename = "1 score=1232"

ttype = "HC"
date = "2017-06-01"
time = "01 01 33"
filename = "4 score=1299"

dirname = os.getcwd()
dirname += "\\Runs\\"
dirname += ttype
dirname += "\\"
dirname += date
dirname += "\\"
dirname += time
dirname += "\\"
dirname += filename


file_pi2 = open(dirname, 'r') 
schedule = pickle.load(file_pi2)
table = schedule.timetable

print "block ", check_day(table)
print "conflict ", check_conflict(table)
print "room ", check_room(table)
print "bonus ", check_bonus(table)
schedule.plot()
