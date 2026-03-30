from django import forms
from .models import Book, Student, Issue


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'quantity']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'student_id']


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['book', 'student', 'return_date']