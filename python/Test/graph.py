# This file allows for early graphical analytics, mainly probing 
# the burden different courses put on the schedule. 

import matplotlib.pyplot as plt
import networkx as nx
import counter

from read_data import *

# ------------------------------------------------------------
# Plot a histogram of courses per student. 
#course_hist = []
#for student in students:
#    course_hist.append(student.get_coursenumber())
    
    
#plt.hist(course_hist, bins = [1, 2, 3, 4, 5, 6, 7])
#plt.xlabel("Number of courses")
#plt.ylabel("Frequency")
#plt.title("Distribution of courses per student")
#plt.xlim(1, 8)
#plt.ylim(0, 230)
#plt.show()

#--------------------------------------------------------------
# plot a network showing which courses are often taken together. 
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
#plt.show()


        




    
