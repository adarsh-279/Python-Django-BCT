from django.shortcuts import render, redirect
from .models import Book, Student, Issue
from .forms import BookForm, StudentForm, IssueForm


# 📚 HOME - show all books
def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})


# ➕ ADD BOOK
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})


# 👨‍🎓 ADD STUDENT
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})


# 📖 ISSUE BOOK
def issue_book(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IssueForm()

    return render(request, 'issue_book.html', {'form': form})

# VIEW ALL BOOKS
def view_books(request):
    books = Book.objects.all()
    return render(request, 'view_books.html', {'books': books})


# VIEW ALL STUDENTS
def view_students(request):
    students = Student.objects.all()
    return render(request, 'view_students.html', {'students': students})