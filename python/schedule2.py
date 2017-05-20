# creates a datastructure for the schedule

from read_data import *
from rate_timetable import *
import numpy as np
from visualize import visualize

class Activity():
    # a two hour timeslot with a name, participants and a
    # specific room.
    
    def __init__(self, name, ttype, capacity, group_id=None, room=None, participants=[]):
        self.name = name
        self.ttype = ttype
        self.group_id = group_id
        self.capacity = capacity
        self.room = room
        self.participants = participants

    def get_name(self):
        return self.name
    def get_type(self):
        return self.ttype
    def get_capacity(self):
        return self.capacity
    def get_room(self):
        return self.room
    def get_participants(self):
        return self.participants
    def get_group_id(self):
        return self.group_id

    def update_name(self, name):
        self.name = name

    def update_participants(self, participants):
        if type(participants) != type([]):
            return 0
        self.participants = participants
        return 1

    def update_group_id(self, group_id):
        self.group_id = group_id
        
    def update_room(self, room):
        self.room = room

    def add_participants(self, participants):
        self.participants.append(participants) # sanity check iemand twee keer. 

    def __str__(self):
        return str(self.name) + " " + str(self.ttype) + " " + str(self.group_id)

class Schedule():
    # a 5x5 matrix that represents the available timeslots
    # and can calculate its own fitness.

    
    
    def __init__(self):
        self.timetable = [[[] for x in range(5)] for y in range(5)]
        self.day_dict = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday"}
        self.timeslot_dict = {0:"9:00-11:00", 1:"11:00-13:00", 2:"13:00-15:00", 3:"15:00-17:00", 4:"17:00-19:00"}
        

    def get_timetable(self):
        return self.timetable
    def update_activity(self, day, timeslot, name, replacement):
        i = 0
        for activity in self.timetable[timeslot][day]:          
            if activity.name + "_" + activity.type + "_" + activity.group_id == name:
                self.timetable[timeslot][day][i] = replacement
                return 1 # if successful
            i += i
        return 0 # if unsuccessful
    def update_timetable(self, new_timetable):
        self.timetable = new_timetable # sanity check hiero moet noggg! #check of het een 5 bij 5 matrix is!!
        return self


    def evening_full(self, day):
        """ check if evening timeslot is taken """
        return self.timetable[4][day] != []
    def slot_full(self, day, timeslot):
        """ check if timeslot is full """
        return len(self.timetable[timeslot][day]) == 7

    def add_activity(self, day, timeslot, activity):
        self.timetable[timeslot][day].append(activity)
    
    def score(self):
        # get timetable's score. 
        return rate_timetable(self.timetable)

    def plot(self):
        visualize(self.timetable)

    def personal(student, visual=False):

        
        personal_table = [[[] for x in range(5)] for y in range(5)]

        for day in range(5):
            for timeslot in range(5):
                for activity in self.timetable[timeslot][day]:
                    if student in activity.participants:
                        personal_table.append(activity)

        if visual:
            self.visualize(personal_table)
        

    def __str__(self):
        for day in range(5):
            print "^^^^^^^^^" + self.day_dict[day] + "^^^^^^^^^^^"           
            for timeslot in range(5):
                print "------------"+ self.timeslot_dict[timeslot] + "----------"
                for activity in self.timetable[timeslot][day]:
                    group = str(activity.group_id)
                    if activity.ttype == "lectures":
                        print activity.name + " " + activity.ttype + " " + group
                    else:
                        print activity.name + " " + activity.ttype + " Group " + group
        return ""
