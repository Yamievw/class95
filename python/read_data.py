# This file reads in the data and fills two lists: one with 
# students and one with courses. This data can be readily used
# by importing this module. 

import csv


class Courses():
    def __init__(self, name, components, registrants):
        self.name = name
        self.components = components # a dictionary of yet unkown format. 
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

    
students = {}
courses = {}

###
### Fiks lowercase vaknamen enzo. 
###

with open('vakken.CSV', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter = ";")
    for row in reader:
        components = {}
        components["lectures"] = (row[1], None)
        components["tutorials"] = (row[2], row[3]) # misschien problemen met nvt
        components["labs"] = (row[4], row[5])
        
        # create course object. 
        courses[row[0]] = Courses(row[0], components, [])
          

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
        


        
