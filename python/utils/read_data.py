# This file reads in the data and fills two lists: one with 
# students and one with courses. This data can be readily used
# by importing this module. 

import csv
import math # for ceil.


class Courses():
    def __init__(self, name, components, registrants):
        self.name = name
        # a dictionary with keys "lectures", "tutorials" or "labs" and the
        # required number per student and capacity. 
        self.components = components
        self.per_student = {}
        self.registrants = registrants # a list containing students in an unknown format. 
        self.registrants = sorted(self.registrants) # is dit nodig of niet? hangt van format registrants af. 
        self.amount_registrants = len(self.registrants)
        
    def __str__():
        return self.name

    def get_registrants(self):
        return self.registrants
    def get_amount_registrants(self):
        return self.amount_registrants
    def get_lectures(self):
        return self.components["lectures"]
    def get_tutorials(self):
        return self.components["tutorials"]
    def get_labs(self):
        return self.components["labs"]
    def get_name(self):
        return self.name
    def get_components(self):
        return self.components
    
    def add_registrant(self, registrant):
        self.registrants.append(registrant)

    def update_components(self):
        tutorials_per_student = self.components["tutorials"][0]
        labs_per_student = self.components["labs"][0]
        tutorials_capacity = self.components["tutorials"][1]
        labs_capacity = self.components["labs"][1]

        tutorial_result = tutorials_per_student*len(self.registrants)/float(tutorials_capacity)
        labs_result = labs_per_student*len(self.registrants)/float(labs_capacity)

        self.per_student["tutorials"] = tutorials_per_student
        self.per_student["labs"] = labs_per_student
        self.per_student["lectures"] = self.components["lectures"][0]
        self.per_student["all"] = tutorials_per_student + labs_per_student + self.components["lectures"][0]

        
        # math.ceil to ensure enough activities
        self.components["tutorials"] = (int(math.ceil(tutorial_result)), tutorials_capacity)
        self.components["labs"] = (int(math.ceil(labs_result)), labs_capacity)
        

        self.no_groups = max(self.components["tutorials"][0], self.components["labs"][0])

class Student():
    def __init__(self, name, surname, number, courses):
        self.name = name
        self.surname = surname
        self.number = number
        self.courses = []
        
        
        for course in courses:
            if course != '':
                if course == 'Zoeken':
                    self.courses.append('Zoeken, sturen en bewegen')
                elif course != ' sturen en bewegen':
                    self.courses.append(course)
        self.courses = sorted(self.courses)
        self.coursenumber = len(self.courses)

    def get_courses(self):
        return self.courses
    def get_coursenumber(self):
        return self.coursenumber
    
    
       
    
    
    
    
class Room():
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    
    def get_name(self):
        return self.name
    def get_capacity(self):
        return self.capacity


    
students = {}
courses = {}
rooms = {}



###
### Fiks lowercase vaknamen enzo. 
###



# read in rooms
with open('rooms.CSV', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter = ";")
    for row in reader:
        name = row[0]
        capacity = row[1]
        
        # create course object. 
        rooms[row[0]] = Room(row[0], row[1])

        
        
# read in courses
with open('vakken.CSV', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter = ";")
    for row in reader:
        components = {}

        tutorials_capacity = row[3]
        labs_capacity = row[5]

        # 1000 means unlimited capacity.
        if tutorials_capacity == "nvt":
            tutorials_capacity = 1000
        if labs_capacity == "nvt":
            labs_capacity = 1000
        
        # tupe structure: (number per student, capacity)
        components["lectures"] = (int(row[1]), 1000) # 1000 means unlimited capacity
        components["tutorials"] = (int(row[2]), tutorials_capacity) 
        components["labs"] = (int(row[4]), labs_capacity)
        
        # create course object. 
        courses[row[0]] = Courses(row[0], components, [])
     
    
    
    
# read in students and add them to courses
with open('studenten_roostering.CSV', 'rb') as csvfile:
    # open txt file. 
    reader = csv.reader(csvfile, delimiter = ",")
    for row in reader:
        # create students.
        students[row[2]] = Student(row[1], row[0], row[2], row[3:])
        for course in row[3:]:
            try:
                courses[course].add_registrant(row[2])
            except KeyError:
                continue

# update the requirement for the number of tutorials and labs
for key in courses:
    courses[key].update_components()

# to test the components update.
#print courses["Collectieve Intelligentie"].get_components()
