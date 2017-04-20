# creates a datastructure for the schedule

from read_data import *
from rate_timetable import *
import numpy as np

class Activity():
    # a two hour timeslot with a name, participants and a
    # specific room.
    
    def __init__(self, name, activity_type, capacity, room=None, participants=None):
        self.name = name
        self.type = activity_type
        self.capacity = capacity
        self.room = room
        self.participants = participants

    def get_name(self):
        return self.name
    def get_type(self):
        return self.type
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
        self.day_dict = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday"}
        self.timeslot_dict = {0:"9:00-11:00", 1:"11:00-13:00", 2:"13:00-15:00", 3:"15:00-17:00", 4:"17:00-19:00"}
                
        

    def get_timetable(self):
        return self.timetable

    def add_activity(self, day, timeslot, activity):
        self.timetable[timeslot][day].append(activity)
    
    def score(self):
        # get timetable's score. 
        return rate_timetable(self.timetable)

    def __str__(self):
        for day in range(5):
            print "^^^^^^^^^" + self.day_dict[day] + "^^^^^^^^^^^"           
            for timeslot in range(5):
                print "------------"+ self.timeslot_dict[timeslot] + "----------"
                for activity in self.timetable[timeslot][day]:
                    print activity.name + " " + activity.type
        return "--"
                    
        
    


    
        
        
