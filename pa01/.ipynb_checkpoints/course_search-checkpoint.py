'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''
<<<<<<< HEAD

=======
#testing
>>>>>>> 90033cd6006fa59d52f8e2a13e016a1499ec9693
from schedule import Schedule
import sys

schedule = Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5,1000)) # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
timeofday (filter by day and time, e.g. meets at 11 on Wed)
'''

terms = {c['term'] for c in schedule.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global schedule
<<<<<<< HEAD
    while True:         
=======
    while True:
>>>>>>> 90033cd6006fa59d52f8e2a13e016a1499ec9693
        command = input(">> (h for help) ")
        if command=='quit':
            return
        elif command in ['h','help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r','reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5,1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['s','subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])
<<<<<<< HEAD
        elif command in ['l', 'lessThan50']:
            subject = input("enter a course:") 
            schedule = schedule.lessThan50([course])
        else:
            print('command',command,'is not supported')
            continue
        
=======
        else:
            print('command',command,'is not supported')
            continue

>>>>>>> 90033cd6006fa59d52f8e2a13e016a1499ec9693
        print("courses has",len(schedule.courses),'elements',end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n'*3)

def print_course(course):
    '''
<<<<<<< HEAD
    print_course prints a brief description of the course 
=======
    print_course prints a brief description of the course
>>>>>>> 90033cd6006fa59d52f8e2a13e016a1499ec9693
    '''
    print(course['subject'],course['coursenum'],course['section'],
          course['name'],course['term'],course['instructor'])




if __name__ == '__main__':
    topmenu()
<<<<<<< HEAD


    '''
7. your team should add the following features to the course_search.py script

a. course  -- filter by subject/coursenumber
b. instructor -- filter by instructor email or lastname
c. title -- filter by phrase in the title
d. description -- filter by phrase in the description
e. Create your own filter (each team member creates their own)

    '''
=======
>>>>>>> 90033cd6006fa59d52f8e2a13e016a1499ec9693
