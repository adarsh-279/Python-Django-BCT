#a=7
#b=2
#print("sum", a+b)

#a= input("Enter your name: ")
#print("Name is: ",a)

#n = int(input("Enter age: "))
#if (n >= 18):
#    print("Eligible")
#else:
#    print("Not eligible")

#n = int(input("Enter Marks: "))
#if (n >= 90):
#    print("A")
#elif (n >= 70):
#    print("B")
#elif (n >= 50):
#    print("C")
#elif (n >= 40):
#    print("D")
#else:
#    print("Fail")

#for i in range(1,11):
#    print(i)

#for i in range(1, 11):
#    print(i, "is", result)
#    result = {0: "Even", 1: "Odd"}[i % 2]

#n=3
#while (n < 31):
#    print(n)
#    n = n+3

#n=1
#for i in range (1,11):
#    if(n <=10 ):
#        s=n*i
#        print(f"{n} x {i} = {s}")


#while True:
#    num1 = float(input("Enter first number: "))
#    op = input("Enter operator (+, -, *, /): ")
#    num2 = float(input("Enter second number: "))
#
#    if op == "+":
#        print("Result:", num1 + num2)
#    elif op == "-":
#        print("Result:", num1 - num2)
#    elif op == "*":
#        print("Result:", num1 * num2)
#    elif op == "/":
#        print("Result:", num1 / num2)
#    else:
#        print("Invalid operator")

#a = int(input("Enter first term: "))
#d = int(input("Enter common difference: "))
#n = int(input("Enter number of terms: "))
#
#for i in range(n):
#    term = a + i * d
#    print(term, end=" ")

#import random
#import string
#
#length = 8
#characters = string.ascii_letters + string.digits
#password = "".join(random.choice(characters) for i in range(length))
#
#print("Generated Password:", password)
#
#while True:
#    user_pass = input("Enter password: ")
#
#    if user_pass == password:
#        print("Access Granted")
#        break
#    else:
#        print("Wrong password, try again")

#num = int(input("Enter a number: "))
#fact = 1
#
#for i in range(1, num + 1):
#    fact = fact * i
#
#print("Factorial =", fact)

#import random
#
#num = random.randint(1,10)
#
#gcount = 0
#
#while gcount <= 5:
#    gnum = int(input("Guess Number between 1-10 :- "))
#    if gnum == num:
#        gcount +=1
#        print(f"Right guess, tries taken {gcount}")
#        break
#    elif gnum > num:
#        gcount +=1
#        print("Try lower")
#    elif gnum < num:
#        gcount +=1
#        print("Try higher")
#    else:
#        print("Wrong guess,tries finished")

