#!/usr/bin/env python
#
#Melissa Wijngaarden
#Heuristieken, lesroosters

from collections import Counter, defaultdict
import csv
import numpy as np

header_counter = defaultdict(Counter)

def read_student_data(filename):

	with open(filename) as f:

		database = []

		r = csv.reader(f, delimiter=',')
	    
	    # read headers
		headers = next(r)
		for row in r:
			if len(row) > 8:
				database.append(row[:-1])
			else:
				database.append(row)

	database = np.array(database)

	return database

def read_course_data(filename):

	data = np.genfromtxt(filename, skip_header=1, delimiter=';', dtype=str)
	return data

if __name__ == '__main__':

	# store studenten_rooster.csv in database an read into data
	database = read_student_data('studenten_rooster.csv')

	# student number is in the second column of database
	student_nr =  database[:,2]

	# courses subscriptions are given in the 3th to 7th column 
	courses = np.concatenate((database[:,3],database[:,4],database[:,5],database[:,6], database[:,7] ))

	# not everyone filled in 5 courses, get those out of our coursenames
	courses = courses[np.where(courses != '')]

	# create a list of all the unique courses
	unique_courses = np.unique(courses)
	print 'ik ben unique: ', unique_courses

	# store vakken.csb in course_info and read into data
	course_info = read_course_data('vakken.csv')

	# create a list to store course subscriptions
	course_subscriptions = []

	# count for every course in in the zeroth column from 'vakken' how many times each course occurs in database
	for i, course in enumerate(course_info[:,0]):

		# course == course[0] uit database 'vakken' => courses =  how many times coursenames match
		nr_of_students = len(np.where(courses == course)[0])
		course_subscriptions.append(nr_of_students)
		print course,'\t', nr_of_students

		# look how many times the tutorial needs to be given 
		if course_info[i][3] != 'nvt':
			classes_needed = int(nr_of_students)/float(course_info[i][3])
			print 'number of werkcolleges needed : ', np.ceil(classes_needed)

		# look how many times the practicum needs to be given
		if course_info[i][5] != 'nvt':
			classes_needed = int(nr_of_students)/float(course_info[i][5])
			print 'number of practica needed : ', np.ceil(classes_needed)

	print course_subscriptions

	# add a column to course_info to add the course_subscriptions to the column
	course_info = np.column_stack((course_info, np.array(course_subscriptions)))

	print course_info[:,-1]
