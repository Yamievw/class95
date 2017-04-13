# This file reads in the data and fills two lists: one with 
# students and one with courses. This data can be readily used
# by importing this module. 

import csv

###
### Hier moet de course-class
###


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

    
students = []
courses = []

with open('studenten_roostering.CSV', 'rb') as csvfile:
    # open txt file. 
    reader = csv.reader(csvfile, delimiter = ",")
    for row in reader:
        # create students. 
        students.append(Student(row[1], row[0], row[2], row[3:]))


        
