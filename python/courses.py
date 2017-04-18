import csv

class Courses():
    def __init__(self, name, components, registrants):
        self.name = name
        self.components = components # a dictionary of yet unkown format. 
        self.registrants = registrants # a list containing students in an unknown format. 
           
        self.registrants = sorted(self.registrants) # is dit nodig of niet? hangt van format registrants af. 
        self.amount_registrants = len(self.registrants)

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
    
# get the registrants per course
with open('studenten_roostering.CSV', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    for row in reader:
        registrants.append(registrant(row[1], row[0], row[2], row[3:]))
        
# get all courses with corresponding data
with open('vakken.CSV', 'rb') as csvfile:
    reader = csv.reader(csvfile,delimiter = ",")
    for row in reader:
        
