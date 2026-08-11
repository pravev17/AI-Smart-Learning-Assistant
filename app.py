from flask import Flask, render_template, request
from recommendation import get_recommendation
import sqlite3

app = Flask(__name__)


# =========================================================
# LOGIN
# =========================================================

@app.route("/")
def login():
    return render_template("login.html")


# =========================================================
# HOME
# =========================================================

@app.route("/home", methods=["POST"])
def home():

    name = request.form["name"]
    regno = request.form["regno"]

    return render_template(
        "home.html",
        name=name,
        regno=regno
    )


# =========================================================
# LEVEL
# =========================================================

@app.route("/level", methods=["POST"])
def level():

    name = request.form["name"]
    regno = request.form["regno"]
    subject = request.form["subject"]

    return render_template(
        "level.html",
        name=name,
        regno=regno,
        subject=subject
    )


# =========================================================
# RECOMMENDATION
# =========================================================

@app.route("/recommendation", methods=["POST"])
def recommendation():

    name = request.form["name"]
    regno = request.form["regno"]
    subject = request.form["subject"]
    level = request.form["level"]

    conn = sqlite3.connect("database/learning.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students(name, regno, subject, level)
        VALUES (?, ?, ?, ?)
    """, (name, regno, subject, level))

    conn.commit()
    conn.close()

    topics = get_recommendation(subject, level)

    return render_template(
        "recommendation.html",
        name=name,
        regno=regno,
        subject=subject,
        level=level,
        topics=topics
    )


# =========================================================
# NOTES DATA
# =========================================================

notes_data = {

    # =====================================================
    # PYTHON
    # =====================================================

    "Python": {

        "Beginner": """
PYTHON - BEGINNER NOTES

1. INTRODUCTION TO PYTHON

Python is a high-level, interpreted and easy-to-learn programming language.
It is widely used in web development, data science, artificial intelligence,
machine learning and automation.

Python uses simple and readable syntax.

Example:

print("Hello World")

The print() function is used to display information on the screen.


2. VARIABLES

A variable is a name used to store data.

Example:

name = "Pravelika"
age = 20

Python automatically understands the type of the value.

Example:

x = 10
name = "Python"


3. DATA TYPES

Common Python data types are:

• int - Integer numbers
• float - Decimal numbers
• str - Text
• bool - True or False
• list - Collection of values
• tuple - Ordered collection
• dict - Key-value pairs
• set - Unordered collection of unique values

Example:

age = 20
price = 25.5
name = "Python"
student = True


4. OPERATORS

Arithmetic operators:

+ Addition
- Subtraction
* Multiplication
/ Division
% Modulus
** Power

Example:

a = 10
b = 5

print(a + b)
print(a * b)


5. CONDITIONAL STATEMENTS

Conditional statements are used to make decisions.

Example:

age = 18

if age >= 18:
    print("Eligible")

else:
    print("Not Eligible")


6. LOOPS

Loops are used to repeat a block of code.

For loop:

for i in range(5):
    print(i)

While loop:

i = 1

while i <= 5:
    print(i)
    i += 1


7. FUNCTIONS

A function is a reusable block of code.

Example:

def add(a, b):
    return a + b

result = add(10, 20)
print(result)


8. LISTS

A list stores multiple values.

Example:

numbers = [10, 20, 30, 40]

print(numbers[0])

Lists can be modified after creation.


9. SUMMARY

Python is beginner-friendly and powerful.
Important beginner concepts include variables, data types,
operators, conditions, loops, functions and lists.
""",


        "Intermediate": """
PYTHON - INTERMEDIATE NOTES

1. OBJECT ORIENTED PROGRAMMING

Object Oriented Programming is a programming approach based on objects
and classes.

Important concepts:

• Class
• Object
• Inheritance
• Encapsulation
• Polymorphism


Example:

class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


student = Student("Pravelika")
student.display()


2. FILE HANDLING

Python can read and write files.

Reading a file:

file = open("data.txt", "r")

content = file.read()

print(content)

file.close()


Writing:

file = open("data.txt", "w")

file.write("Hello Python")

file.close()


3. EXCEPTION HANDLING

Errors can be handled using try and except.

Example:

try:

    number = int(input("Enter number: "))

except ValueError:

    print("Invalid input")


4. MODULES

A module is a Python file containing reusable code.

Example:

import math

print(math.sqrt(25))


5. LIST COMPREHENSION

List comprehension provides a short way to create lists.

Example:

numbers = [1, 2, 3, 4, 5]

squares = [x*x for x in numbers]

print(squares)


6. DICTIONARIES

A dictionary stores data using key-value pairs.

Example:

student = {
    "name": "Pravelika",
    "age": 20
}

print(student["name"])


7. LAMBDA FUNCTIONS

Lambda functions are small anonymous functions.

Example:

square = lambda x: x * x

print(square(5))


8. INTERMEDIATE PROJECTS

Students can build:

• Calculator
• Student management system
• File management application
• Quiz application
• Basic Flask application


9. SUMMARY

Intermediate Python focuses on OOP, files, modules,
exception handling, dictionaries and reusable programming.
""",


        "Advanced": """
PYTHON - ADVANCED NOTES

1. ADVANCED PYTHON

Advanced Python includes frameworks, APIs, databases,
automation and data processing.


2. FLASK

Flask is a lightweight Python web framework.

Example:

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

app.run()


3. APIS

API means Application Programming Interface.

APIs allow different software applications to communicate.

Python can send requests using the requests library.

Example:

import requests

response = requests.get("https://example.com")

print(response.status_code)


4. DATABASE CONNECTIVITY

Python can connect to databases such as SQLite and MySQL.

SQLite example:

import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

data = cursor.fetchall()

conn.close()


5. DECORATORS

Decorators modify the behavior of functions.

Example:

def decorator(function):

    def wrapper():
        print("Before function")
        function()

    return wrapper


6. GENERATORS

Generators produce values one at a time.

Example:

def numbers():

    for i in range(5):
        yield i


7. MACHINE LEARNING

Python is widely used for machine learning.

Popular libraries include:

• NumPy
• Pandas
• Scikit-learn
• TensorFlow
• PyTorch


8. DEPLOYMENT

Python applications can be deployed using platforms
and cloud services.

Important concepts include:

• Servers
• Hosting
• Environment variables
• Requirements files
• APIs


9. SUMMARY

Advanced Python connects programming concepts with
real-world applications such as web development,
APIs, databases, automation and machine learning.
"""
    },


    # =====================================================
    # DBMS
    # =====================================================

    "DBMS": {

        "Beginner": """
DBMS - BEGINNER NOTES

1. INTRODUCTION

DBMS stands for Database Management System.

It is software used to store, manage and retrieve data.

Examples:

• MySQL
• PostgreSQL
• Oracle
• SQLite


2. DATABASE

A database is an organized collection of information.

Example:

A college database can store:

Student ID
Name
Department
Marks


3. TABLE

A table stores data in rows and columns.

Example:

Student table:

ID | Name | Department
1  | Arun | CSE
2  | Priya | AI


4. ROW AND COLUMN

A row represents one record.

A column represents one attribute.

Example:

Name is a column.

"Arun" is a value in a row.


5. PRIMARY KEY

A primary key uniquely identifies each record.

Example:

Student_ID can be the primary key.


6. SQL

SQL means Structured Query Language.

Example:

SELECT * FROM students;


7. INSERT

Used to add data.

INSERT INTO students
VALUES (1, 'Arun', 'CSE');


8. UPDATE

Used to modify existing data.

UPDATE students
SET name = 'Kumar'
WHERE id = 1;


9. DELETE

Used to remove data.

DELETE FROM students
WHERE id = 1;


10. SUMMARY

DBMS helps organizations store and manage large amounts
of data efficiently.
""",


        "Intermediate": """
DBMS - INTERMEDIATE NOTES

1. JOINS

Joins combine data from multiple tables.

Types:

• INNER JOIN
• LEFT JOIN
• RIGHT JOIN
• FULL JOIN


2. INNER JOIN

Returns matching records from both tables.

Example:

SELECT students.name, departments.department_name
FROM students
INNER JOIN departments
ON students.department_id = departments.id;


3. NORMALIZATION

Normalization organizes data to reduce duplication.

Important normal forms:

• 1NF
• 2NF
• 3NF


4. VIEWS

A view is a virtual table created using a query.

Example:

CREATE VIEW student_view AS
SELECT name, department
FROM students;


5. INDEXING

Indexes improve database search performance.

Example:

CREATE INDEX idx_name
ON students(name);


6. SUBQUERIES

A query inside another query is called a subquery.

Example:

SELECT name
FROM students
WHERE marks >
(SELECT AVG(marks) FROM students);


7. CONSTRAINTS

Common constraints:

• PRIMARY KEY
• FOREIGN KEY
• UNIQUE
• NOT NULL
• CHECK


8. TRANSACTIONS

A transaction is a group of database operations.

Important commands:

COMMIT
ROLLBACK


9. SUMMARY

Intermediate DBMS focuses on joins, normalization,
views, indexing, constraints and transactions.
""",


        "Advanced": """
DBMS - ADVANCED NOTES

1. STORED PROCEDURES

Stored procedures are precompiled SQL programs stored
inside the database.

They can be reused multiple times.


2. TRIGGERS

A trigger automatically executes when a database event occurs.

Example events:

• INSERT
• UPDATE
• DELETE


3. TRANSACTIONS

Transactions maintain database consistency.

Important properties are ACID:

A - Atomicity
C - Consistency
I - Isolation
D - Durability


4. DATABASE SECURITY

Database security protects information from unauthorized access.

Methods include:

• Authentication
• Authorization
• Encryption
• Access control


5. QUERY OPTIMIZATION

Query optimization improves SQL query performance.

Indexes and proper joins can reduce execution time.


6. DATABASE BACKUP

Regular backups protect data from accidental loss.

Types include:

• Full backup
• Incremental backup
• Differential backup


7. DISTRIBUTED DATABASE

A distributed database stores data across multiple locations.

It can improve availability and scalability.


8. NOSQL

NoSQL databases are useful for flexible and large-scale data.

Examples:

• MongoDB
• Cassandra
• Redis


9. SUMMARY

Advanced DBMS includes security, optimization,
transactions, distributed databases, triggers and
large-scale database management.
"""
    },


    # =====================================================
    # OPERATING SYSTEM
    # =====================================================

    "Operating System": {

        "Beginner": """
OPERATING SYSTEM - BEGINNER NOTES

1. INTRODUCTION

An Operating System is system software that manages
computer hardware and software resources.

Examples:

• Windows
• Linux
• macOS
• Android


2. FUNCTIONS OF OS

Major functions include:

• Process management
• Memory management
• File management
• Device management
• Security


3. PROCESS

A process is a program currently being executed.

Example:

When you open a browser, the operating system creates
a process for it.


4. MEMORY

Memory stores programs and data needed by the CPU.

Types include:

• RAM
• ROM
• Cache


5. FILE SYSTEM

The operating system manages files and folders.

Examples:

Documents
Pictures
Videos


6. DEVICE MANAGEMENT

The OS manages hardware devices such as:

• Keyboard
• Mouse
• Printer
• Disk
• Monitor


7. USER INTERFACE

Users interact with an OS through:

• GUI
• Command Line Interface


8. SUMMARY

An operating system acts as a bridge between the user
and computer hardware.
""",


        "Intermediate": """
OPERATING SYSTEM - INTERMEDIATE NOTES

1. PROCESS MANAGEMENT

The OS creates, schedules and terminates processes.

Process states include:

• New
• Ready
• Running
• Waiting
• Terminated


2. CPU SCHEDULING

CPU scheduling decides which process should execute.

Algorithms include:

• FCFS
• SJF
• Round Robin
• Priority Scheduling


3. THREADS

A thread is a smaller unit of a process.

Multiple threads can execute within one process.


4. DEADLOCK

Deadlock occurs when processes wait indefinitely
for resources held by each other.

Four conditions:

• Mutual exclusion
• Hold and wait
• No preemption
• Circular wait


5. VIRTUAL MEMORY

Virtual memory allows the system to use disk space
as an extension of RAM.


6. PAGING

Paging divides memory into fixed-size blocks called pages
and frames.


7. FILE MANAGEMENT

The OS manages creation, deletion, reading and writing
of files.


8. SUMMARY

Intermediate OS concepts include scheduling,
deadlocks, threads, paging and memory management.
""",


        "Advanced": """
OPERATING SYSTEM - ADVANCED NOTES

1. ADVANCED PROCESS MANAGEMENT

Modern operating systems support multiple processes
and threads simultaneously.

Process synchronization is required when processes
share resources.


2. SYNCHRONIZATION

Synchronization prevents incorrect results when
multiple processes access shared data.

Common techniques:

• Mutex
• Semaphore
• Monitor


3. DEADLOCK HANDLING

Deadlocks can be handled using:

• Prevention
• Avoidance
• Detection
• Recovery


4. PAGE REPLACEMENT

When memory is full, the OS replaces pages.

Algorithms include:

• FIFO
• LRU
• Optimal


5. FILE SYSTEM DESIGN

Advanced file systems manage:

• File allocation
• Directories
• Permissions
• Storage blocks


6. SECURITY

Operating systems provide:

• User authentication
• Access control
• Encryption
• Process isolation


7. VIRTUALIZATION

Virtualization allows multiple virtual machines
to run on one physical system.

Examples include virtual machines and containers.


8. SUMMARY

Advanced OS concepts include synchronization,
deadlock handling, memory management, security
and virtualization.
"""
    },


    # =====================================================
    # APTITUDE
    # =====================================================

    "Aptitude": {

        "Easy": """
APTITUDE - EASY LEVEL

1. NUMBER SYSTEM

A number system represents numbers using different forms.

Important types:

• Natural numbers
• Whole numbers
• Integers
• Rational numbers
• Prime numbers


2. PERCENTAGE

Percentage means a value out of 100.

Formula:

Percentage = (Part / Total) × 100

Example:

20 out of 100 = 20%


3. RATIO

Ratio compares two quantities.

Example:

If boys = 10 and girls = 20,

Ratio = 10 : 20
      = 1 : 2


4. AVERAGE

Average is calculated using:

Average = Sum of values / Number of values


Example:

10, 20, 30

Average = 60 / 3
        = 20


5. PROFIT AND LOSS

Profit = Selling Price - Cost Price

Loss = Cost Price - Selling Price


6. SIMPLE INTEREST

Simple Interest:

SI = (P × R × T) / 100

where:

P = Principal
R = Rate
T = Time


7. TIME AND WORK

If a person completes a work in 10 days,
their one-day work is:

1/10


8. BASIC REASONING

Reasoning questions test logical thinking.

Common topics:

• Series
• Odd one out
• Coding
• Directions
• Analogy


9. SUMMARY

Easy aptitude focuses on basic arithmetic,
percentages, ratios, averages, profit and loss,
time and work and simple reasoning.
""",


        "Medium": """
APTITUDE - MEDIUM LEVEL

1. PROFIT AND LOSS

Profit percentage:

Profit % = (Profit / Cost Price) × 100


2. COMPOUND INTEREST

Compound interest calculates interest on
principal plus previously earned interest.

Formula:

A = P(1 + R/100)^T

CI = A - P


3. TIME, SPEED AND DISTANCE

Speed = Distance / Time

Distance = Speed × Time

Time = Distance / Speed


4. PROBLEMS ON TRAINS

Important concepts include:

Time = Distance / Speed

When a train crosses a person,
distance is usually the length of the train.


5. WORK AND WAGES

Work problems compare the efficiency of workers.

If A completes a task in 10 days:

One-day work = 1/10


6. PERMUTATION

Permutation deals with arrangements.

Formula:

nPr = n! / (n-r)!


7. COMBINATION

Combination deals with selections.

Formula:

nCr = n! / (r!(n-r)!)


8. PROBABILITY

Probability measures the chance of an event.

Probability = Favorable outcomes / Total outcomes


9. DATA INTERPRETATION

Data interpretation involves tables,
charts and graphs.

The student must calculate:

• Percentage
• Difference
• Ratio
• Average


10. SUMMARY

Medium aptitude focuses on mathematical
problem solving and logical reasoning.
""",


        "Hard": """
APTITUDE - HARD LEVEL

1. ADVANCED PROBABILITY

Probability can involve multiple events.

Important concepts:

• Independent events
• Dependent events
• Conditional probability


2. PERMUTATION AND COMBINATION

Advanced problems combine arrangements,
selections and restrictions.

Example:

Number of arrangements of n objects:

n!


3. TIME AND WORK

Advanced problems may involve multiple workers,
efficiency changes and work distribution.


4. SPEED AND DISTANCE

Advanced questions may involve:

• Relative speed
• Boats and streams
• Trains
• Circular tracks


5. DATA INTERPRETATION

Advanced DI may involve multiple tables,
graphs and calculations.

Students should identify relationships
before performing calculations.


6. NUMBER THEORY

Important concepts:

• HCF
• LCM
• Prime numbers
• Divisibility
• Remainders


7. ALGEBRA

Important concepts include:

• Linear equations
• Quadratic equations
• Algebraic identities
• Inequalities


8. LOGICAL REASONING

Advanced reasoning includes:

• Seating arrangement
• Blood relations
• Syllogisms
• Puzzles
• Statement and conclusion


9. INTERVIEW APTITUDE

Aptitude preparation is useful for placement
tests and competitive examinations.

Students should practice regularly
and improve speed and accuracy.


10. SUMMARY

Hard aptitude focuses on advanced mathematical
reasoning, probability, combinations, algebra,
data interpretation and complex puzzles.
"""
    }
}


# =========================================================
# NOTES PAGE
# =========================================================

@app.route("/notes", methods=["POST"])
def notes():

    name = request.form["name"]
    regno = request.form["regno"]
    subject = request.form["subject"]
    level = request.form["level"]

    content = notes_data.get(subject, {}).get(level)

    if content is None:
        content = "Notes are not available for this subject and level."

    return render_template(
        "notes.html",
        name=name,
        regno=regno,
        subject=subject,
        level=level,
        content=content
    )


# =========================================================
# DASHBOARD
# =========================================================

@app.route("/dashboard", methods=["POST"])
def dashboard():

    name = request.form["name"]

    conn = sqlite3.connect("database/learning.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT subject, level FROM students WHERE name=?",
        (name,)
    )

    records = cursor.fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        name=name,
        records=records
    )


# =========================================================
# QUIZ
# =========================================================

@app.route("/quiz", methods=["POST"])
def quiz():

    name = request.form["name"]
    regno = request.form["regno"]
    subject = request.form["subject"]
    level = request.form["level"]

    return render_template(
        "quiz.html",
        name=name,
        regno=regno,
        subject=subject,
        level=level
    )


# =========================================================
# SUBMIT QUIZ
# =========================================================

@app.route("/submit_quiz", methods=["POST"])
def submit_quiz():

    name = request.form["name"]
    regno = request.form["regno"]
    subject = request.form["subject"]
    level = request.form["level"]

    score = 0

    # Python questions
    if subject == "Python":

        if request.form.get("q1") == "Language":
            score += 1

        if request.form.get("q2") == "#":
            score += 1

        if request.form.get("q3") == "def":
            score += 1

        if request.form.get("q4") == "List":
            score += 1

        if request.form.get("q5") == "for":
            score += 1


    # DBMS questions
    elif subject == "DBMS":

        if request.form.get("q1") == "Database Management System":
            score += 1

        if request.form.get("q2") == "Table":
            score += 1

        if request.form.get("q3") == "Primary Key":
            score += 1

        if request.form.get("q4") == "SELECT":
            score += 1

        if request.form.get("q5") == "SQL":
            score += 1


    # Operating System questions
    elif subject == "Operating System":

        if request.form.get("q1") == "Operating System":
            score += 1

        if request.form.get("q2") == "Process":
            score += 1

        if request.form.get("q3") == "RAM":
            score += 1

        if request.form.get("q4") == "Round Robin":
            score += 1

        if request.form.get("q5") == "Deadlock":
            score += 1


    # Aptitude questions
    elif subject == "Aptitude":

        if request.form.get("q1") == "20":
            score += 1

        if request.form.get("q2") == "50":
            score += 1

        if request.form.get("q3") == "20":
            score += 1

        if request.form.get("q4") == "10":
            score += 1

        if request.form.get("q5") == "100":
            score += 1


    percentage = (score / 5) * 100


    # Save result
    conn = sqlite3.connect("database/learning.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO quiz_results
        (name, regno, subject, level, score, percentage)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        name,
        regno,
        subject,
        level,
        score,
        percentage
    ))

    conn.commit()
    conn.close()


    return render_template(
        "quiz_result.html",
        name=name,
        regno=regno,
        subject=subject,
        level=level,
        score=score,
        percentage=percentage
    )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":
    app.run(debug=True)