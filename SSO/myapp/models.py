# school-schedule-opt/sso/myapp/models.py


from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    notes = models.TextField()

    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    notes = models.TextField()

    def __str__(self):
        return self.name
    
class Subject(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Program(models.Model):
    name = models.CharField(max_length=100)

    courses = models.ManyToManyField(Course)

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name

class Datetime(models.Model):
    datetime = models.DateTimeField(db_column="created_at")