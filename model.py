class SchoolScheduleOptModel:
    class Subject:
        def __init__(self, subject_name):
            self.name = subject_name

    class Course:
        def __init__(self, subject, days):
            self.subject = subject
            self.days = days

    class Programm:
        def __init__(self, courses):
            self.courses = courses

    class Group:
        def __init__(self, group_name, students):
            self.name = group_name
            self.students = students

    class Student:
        def __init__(self, student_name, student_surname, student_programm):
            self.name = student_name
            self.surname = student_surname
            self.programm = student_programm

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

    class Day:
        def __init__(self, day_intervals):
            self.intervals = day_intervals
    
    def __init__(self):
        data = self.read_data()

        self.fill_model(data)


    def read_data(self):
        #TODO: Read data from database
        pass

    def fill_model(self, data):
        #TODO: Fill model with data
        pass
    


