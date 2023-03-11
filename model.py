from pyomo.environ import Var, ConcreteModel
from datetime import datetime

class SchoolScheduleOptModel:
    class Subject:
        def __init__(self, subject_name):
            self.name = subject_name
        #TODO: Compare subjects

    class Course:
        def __init__(self, subject, days):
            self.subject = Subject(subject)
            self.days = days

    class Program:
        def __init__(self, courses):
            self.courses = {Course(c['subject'], c['days']) for c in courses}

    class Group:
        def __init__(self, group_name, students):
            self.name = group_name
            self.students = students

    class Student:
        def __init__(self, student_name, student_surname, student_courses):
            self.name = student_name
            self.surname = student_surname
            self.program = Program(student_courses)

    class Teacher:
        def __init__(self, teacher_name, teacher_surname, teacher_subjects, teacher_days):
            self.name = teacher_name
            self.surname = teacher_surname
            self.subjects = {Subject(s) for s in teacher_subjects}
            self.days = teacher_days

    class Room:
        def __init__(self, room_name, room_capacity, room_subjects):
            self.name = room_name
            self.capacity = room_capacity
            self.subjects = {Subject(s) for s in room_subjects}
        
    class Date:
        def __init__(self, date_dt):
            self.dateDt = date_dt
            #TODO: Add str date
        #TODO: Add __add__ for date+1
        
    class Time:
        def __init__(self, time_dt):
            self.timeDt = time_dt
            #TODO: Add str time
        #TODO: Add __add__ for time+1

    class Datetime:
        def __init__(self, date_dt, time_dt):
            self.date = Date(date_dt)
            self.time = Time(time_dt)
        #TODO: Add comp Datetimes

    
    def __init__(self):
        data = self.read_data()

        self.fill_model(data)

    def read_data(self):
        # TODO: Read data from database
        pass

    def fill_model(self):
        # TODO: Fill model with data

        self.setStudents = {s['id'] for s in self.data['students']}

        self.setSubjects = self.get_subjects()
        self.setTeachers = self.get_teachers()
        self.setClassrooms = self.get_classrooms()
        self.setStudentDatetimes = self.get_student_datetimes()
        self.setTeacherDatetimes = self.get_teacher_datetimes()

        self.model = ConcreteModel()

        pass

    def get_subjects(self):
        sjFromStudent = {c.subject['id'] for c in s.courses for s in self.data['students']}
        subjects = {sj['id'] for sj in self.data['sbujects'] if sj['id'] in sjFromStudent}
        return subjects

    def get_teachers():
        teachers = {t['id'] for t in self.data['teachers'] if self.setSubjects.intersection({sj['id'] for sj in t.subjects})}
        return teachers
        

    def get_classrooms(self):
        crFromSubjects = {cr for cr in self.data['classrooms'] if self.setSubjects.intersection({sj['id'] for sj in cr.subjects})}
        return crFromSubjects

    def get_student_datetimes(self):
        sDatetimes = {sl['datetime'] for sl in s['slots'] for s in self.setStudents if sl['datetime'] in self.data['datetimes']}
        return sDatetimes

    def get_teacher_datetimes(self):
        tDatetimes = {sl['datetime'] for sl in t['slots'] for t in self.setTeachers if sl['datetime'] in self.setStudentDatetimes}