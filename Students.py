import csv
import matplotlib.pyplot as plt
#import seaborn as sns
import networkx as nx
import counter


class student():
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

with open('C:\Users\Larry\Documents\Heuristics\studenten_roostering.CSV', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    for row in reader:
        
        students.append(student(row[1], row[0], row[2], row[3:]))


course_hist = []
for student in students:
    course_hist.append(student.get_coursenumber())
    
    
plt.hist(course_hist, bins = [1, 2, 3, 4, 5, 6, 7])
plt.xlabel("Number of courses")
plt.ylabel("Frequency")
plt.title("Distribution of courses per student")
plt.xlim(1, 8)
plt.ylim(0, 230)
plt.show()

courses_list = []
for student in students:
    for course in student.get_courses():
        if course not in courses_list:
            courses_list.append(course)
courses_list = sorted(courses_list)
#print len(courses_list)


G = nx.Graph()
G.add_nodes_from(courses_list)
edges = []
for student in students:
    for course1 in student.get_courses():
        for course2 in student.get_courses():
            if course1 != course2 and (course2, course1) not in edges:
                edges.append((course1, course2))
                
edges2 = {edge:edges.count(edge) for edge in edges}

edges = []
colors = []
for edge in edges2:
    edges.append(edge)
    colors.append(edges2[edge])
    
    
    
G.add_edges_from(edges)
#nx.draw(G, with_labels=True, edge_color = colors, edge_vmin=1, edge_vmax=25, edge_cmap=plt.cm.Blues)
#nx.draw_spring(G)
#nx.draw_random(G)
#nx.draw_circular(G)
#nx.draw_spectral(G)
#plt.show()
        




    
