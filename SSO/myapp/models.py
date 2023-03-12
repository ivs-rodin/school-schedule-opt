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

    slots = models.ManyToManyField(Datetime)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    notes = models.TextField()

    slots = models.ManyToManyField(Datetime)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name
    
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    days = models.IntegerField()

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=100)

    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    subjects = models.ManyToManyField(Subject)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Datetime(models.Model):
    datetime = models.DateTimeField()