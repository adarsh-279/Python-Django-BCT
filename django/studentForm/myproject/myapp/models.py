from django.db import models

class Student(models.Model):

    YEAR_CHOICES = [
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
        ('4th Year', '4th Year'),
    ]

    DEPARTMENT_CHOICES = [
        ('BCA', 'BCA'),
        ('MCA', 'MCA'),
        ('BBA', 'BBA'),
        ('MBA', 'MBA'),
        ('CSE', 'CSE'),
        ('IT', 'IT'),
    ]

    COURSE_CHOICES = [
        ('BCA', 'BCA'),
        ('MCA', 'MCA'),
        ('BBA', 'BBA'),
        ('MBA', 'MBA'),
        ('CSE', 'CSE'),
        ('IT', 'IT'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name