# Module 2 — Lesson 4: Functions
# Student: Adrian Kyle Flores
# Date: 9/27/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
functions are blocks of code that i can use again instead of writing the same code over and over. i can give a function information and it can give me a result back


============================================
KEY VOCABULARY
============================================
- function: a block of code that does a specific task
- parameter: information that a function can receive
- argument: the actual value given to a parameter
- return: sends a value back from the function
- function call: using a function in the program
- def: used to create a function


============================================
CODE
============================================

def greet(name):
    return "hello " + name


student_name = "Adrian"
message = greet(student_name)

print(message)


def add_numbers(a, b):
    return a + b


result = add_numbers(10, 5)

print("the answer is:", result)


============================================
WHAT I LEARNED
============================================
i learned that functions can make my code shorter and easier to reuse. i can put code inside a function and call it whenever i need it


============================================
A MISTAKE I MADE
============================================
i sometimes forget to put the values in the function when calling it. i also need to make sure the return statement is inside the function


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
functions are useful because bigger programs can have a lot of code. putting parts of the code into functions makes it easier to organize and reuse
