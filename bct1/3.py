# class student:
#     name = "noob"

# sl = student()
# print(sl.name)

# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# sl = student("noob", 20)
# print(sl.name, sl.age)

# class book:
#     def __init__(self, name, author, price):
#         self.name = name
#         self.author = author
#         self.price = price

# sl = book("The lost jungle", "Nobody knows", 999)
# print(sl.name, sl.author, sl.price)

# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# def check(marks):
#     if (marks >= 40):
#         return "Pass"
#     else:
#         return "fail"

# name = str(input("Enter student name: "))
# marks = float(input("Enter student marks: "))
# result = check(marks)

# sl = student(name, marks)
# print(sl.name, sl.marks, result)

# class Animal:
#     def __init__(self):
#         pass
#     def eats(self):
#         print("kutta khana kha rha")

# class Dog(Animal):
#     def __init__(self):
#         pass
#     def barks(self):
#         print("Kutta bhok rha hai")

# a= Animal()
# d= Dog()
# a.eats()
# d.eats()
# d.barks()

# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")

# a = Animal()
# d = Dog()
# c = Cat()

# a.sound()
# d.sound()
# c.sound()

# class Rectangle:
#     def __init__(self, l, b):
#         self.l = l
#         self.b = b

#     def area(self):
#         return self.l * self.b

#     def perimeter(self):
#         return 2 * (self.l + self.b)

# l = float(input("Enter length : "))
# b = float(input("Enter breadth : "))

# r = Rectangle(l, b)

# print("Area is:", r.area())
# print("Perimeter is:", r.perimeter())

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def bonus(self):
#         return 0.10 * self.salary 

# name = input("Enter name: ")
# salary = float(input("Enter salary: "))

# emp = Employee(name, salary)
# total = (emp.salary + emp.bonus())

# print("Name:", emp.name)
# print("Salary:", emp.salary)
# print("Bonus (10%):", emp.bonus())
# print("Total pay : ", total)