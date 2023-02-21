from pyomo.environ import Var, ConcreteModel
from datetime import datetime

class SchoolScheduleOptModel:
    class Subject:
        def __init__(self, subject_name):
            self.name = subject_name

    class Course:
        def __init__(self, subject, days):
            self.subject = subject
            self.days = days

    class Program:
        def __init__(self, courses):
            self.courses = courses

    class Group:
        def __init__(self, group_name, students):
            self.name = group_name
            self.students = students

    class Student:
        def __init__(self, student_name, student_surname, student_program):
            self.name = student_name
            self.surname = student_surname
            self.program = student_program

    class Teacher:
        def __init__(self, teacher_name, teacher_surname, teacher_subjects, teacher_days):
            self.name = teacher_name
            self.surname = teacher_surname
            self.subjects = teacher_subjects
            self.days = teacher_days

    class Room:
        def __init__(self, room_name, room_capacity, room_subjects):
            self.name = room_name
            self.capacity = room_capacity
            self.subjects = room_subjects
        
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

    def fill_model(self, data):
        # TODO: Fill model with data

        model = ConcreteModel()

        pass