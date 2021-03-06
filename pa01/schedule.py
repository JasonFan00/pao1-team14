'''
schedule maintains a list of courses with features for operating on that list
by filtering, mapping, printing, etc.
'''

import json


class Schedule():
    '''
    Schedule represent a list of Brandeis classes with operations for filtering
    '''

    def __init__(self, courses=()):
        ''' courses is a tuple of the courses being offered '''
        self.courses = courses

    def load_courses(self):
        ''' load_courses reads the course data from the courses.json file'''
        print('getting archived regdata from file')
        #with open("pa01/courses20-21.json", "r", encoding='utf-8') as jsonfile:# debugging due to import paths
        with open("courses20-21.json", "r", encoding='utf-8') as jsonfile:
            courses = json.load(jsonfile)
        for course in courses:
            course['instructor'] = tuple(course['instructor'])
            course['coinstructors'] = [tuple(f)
                                       for f in course['coinstructors']]
        # making it a tuple means it is immutable
        self.courses = tuple(courses)


    def title(self, phrase):
        '''Returns courses containing the phrase in their title'''
        x = 10
        print(x)
        return Schedule([course for course in self.courses if phrase in course['name']])

    def description(self, phrase):
        '''Returns courses containing the phrase in description'''
        return Schedule([course for course in self.courses if phrase in course['description']])

    def waitlist_count(self, waiting):
        '''Returns courses that have <= people waiting'''
        return Schedule([course for course in self.courses if course['enrolled'] <= waiting])

    def lastname(self, names):
        ''' lastname returns the courses by a particular instructor last name'''
        return Schedule([course for course in self.courses if course['instructor'][1] in names])

    def email(self, emails):
        ''' email returns the courses by a particular instructor email'''
        return Schedule([course for course in self.courses if course['instructor'][2] in emails])

    def term(self, terms):
        ''' email returns the courses in a list of term'''
        return Schedule([course for course in self.courses if course['term'] in terms])

    def enrolled(self, vals):
        ''' enrolled filters for enrollment numbers in the list of vals'''
        return Schedule([course for course in self.courses if course['enrolled'] in vals])

    def subject(self, subjects):
        ''' subject filters the courses by subject '''
        return Schedule([course for course in self.courses if course['subject'] in subjects])


    def coursenum(self, coursenums):
        ''' subject filters the courses by subject '''
        return Schedule([course for course in self.courses if course['coursenum'] in coursenums])



    def sort(self, field):
        if field == 'subject':
            return Schedule(sorted(self.courses, key=lambda course: course['subject']))
        else:
            print("can't sort by "+str(field)+" yet")
            return self

    '''
    #7e. 
    list enrollments less than 50 
    '''
    def lessThan50(self, course):
        ''' enrolled filters for enrollment numbers in the list of vals'''
        return Schedule([course for course in self.courses if course['enrolled'] < 50])
