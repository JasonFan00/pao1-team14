'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''
# testing
from schedule import Schedule
import sys

schedule = Schedule()
schedule.load_courses()
# eliminate courses with no students
schedule = schedule.enrolled(range(5, 1000))

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
    while True:
        command = input(">> (h for help) ")
        if command == 'quit':
            return
        elif command in ['h', 'help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r', 'reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5, 1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['s', 'subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])
        elif command in ['d', 'description']:
            '''created by Gisel'''
            phrase = input("Enter a phrase: ")
            schedule = schedule.description(phrase)
        elif command in ['i','instructor']:
            user_input = input("enter instructor:")
            schedule = schedule.email([user_input])
        elif command in ['c', 'course']:
            user_input = input("enter the course or course num:")
            schedule = schedule.subject([user_input])
        elif command in ['t', 'titlephrase']:
            phrase = input("enter a phrase in title:")
            schedule = schedule.title(phrase)
        elif command in ['l', 'lessThan50']:
            subject = input("enter a course:") 
            schedule = schedule.lessThan50([course])
        else:
            print('command', command, 'is not supported')
            continue

        print("courses has", len(schedule.courses), 'elements', end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n'*3)



def print_course(course):
    '''
    print_course prints a brief description of the course
    '''
    print(course['subject'], course['coursenum'], course['section'],
          course['name'], course['term'], course['instructor'])


if __name__ == '__main__':
    topmenu()
