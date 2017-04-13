import csv

class Courses():
    def __init__(self, name, number, hoorcolleges, werkcolleges, practica, registrants):
        self.name = name
        self.number = number
        self.hoorcolleges = hoorcolleges
        self.werkcolleges = werkcolleges
        self.practica = practica
        self.registrants = []
            
        for registrant in registrants:
            if registrant != '':
                if registrant == 'Zweekhorst':
                    self.registrants.append('Stein Zweekhorst')
                elif course != ' Stein':
                    self.registrants.append(registrant)
            self.registrants = sorted(self.registrants)
            self.amountregistrants = len(self.registrants)

    def get_registrants(self):
        return self.registrants

    def get_amountregistrants(self):
        return self.amountregistrants
    
# get the registrants per course
with open('studenten_roostering.CSV', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    for row in reader:
        registrants.append(registrant(row[1], row[0], row[2], row[3:]))
        
# get all courses with corresponding data
with open('vakken.CSV', 'rb') as csvfile:
    reader = csv.reader(csvfile,delimiter = ",")
    for row in reader:
        
