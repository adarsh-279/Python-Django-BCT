from django.db import models

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.title


# Student Model
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    student_id = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# Issue Book Model
class Issue(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.book} issued to {self.student}"