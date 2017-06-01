# reads a saved schedule object. 

import pickle
import os
from rate_timetable import *

##ttype = "HC"
##date = "2017-05-29"
##time = "17 27 10"
##filename = "1 score=1232"

# define saved object. 
ttype = "HC"
date = "2017-06-01"
time = "01 01 33"
filename = "4 score=1299"

# get path. 
dirname = os.getcwd()
dirname += "\\Runs\\"
dirname += ttype
dirname += "\\"
dirname += date
dirname += "\\"
dirname += time
dirname += "\\"
dirname += filename

# open file. 
file_pi2 = open(dirname, 'r') 
schedule = pickle.load(file_pi2)
table = schedule.timetable

# use schedule however you see fit. 
##print "block ", check_day(table)
##print "conflict ", check_conflict(table)
##print "room ", check_room(table)
##print "bonus ", check_bonus(table)
##schedule.plot()
