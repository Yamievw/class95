# creates a datastructure for the schedule

from read_data import *
from rate_timetable import *
import numpy as np

class Activity():
    # a two hour timeslot with a name, participants and a
    # specific room.
    
    def __init__(self, name, capacity, room, participants):
        self.name = name
        self.capacity = capacity
        self.room = room
        self.participants = participants

    def get_name(self):
        return self.name
    def get_capacity(self):
        return self.capacity
    def get_room(self):
        return self.room
    def get_participants(self):
        return self.participants

class Schedule():
    # a 5x5 matrix that represents the available timeslots
    # and can calculate its own fitness. 
    def __init__(self):
        self.timetable = [[[] for x in range(5)] for y in range(5)] 
                
        

    def get_timetable(self):
        return self.timetable

    def add_activity(day, timeslot, activity):
        self.timetable[timeslot][day].append(activity)
    
    def score(self):
        # get timetable's score. 
        return rate_timetable(self.timetable)
        
    


    
        
        
