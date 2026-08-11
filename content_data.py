# ============================================================
# AI SMART LEARNING ASSISTANT
# Subject-wise and Level-wise Learning Content
# ============================================================

CONTENT = {

    # ========================================================
    # PYTHON
    # ========================================================

    "Python": {

        "Beginner": {
            "notes": [
                {
                    "title": "1. Introduction to Python",
                    "content": """
Python is a high-level, interpreted programming language.
It is popular because its syntax is simple and easy to understand.

Python is used in:
• Web development
• Data Science
• Artificial Intelligence
• Machine Learning
• Automation
• Application development

Example:

print("Hello World")

The print() function is used to display information on the screen.
"""
                },
                {
                    "title": "2. Variables and Data Types",
                    "content": """
A variable is a name used to store a value.

Example:

name = "Prave"
age = 20
mark = 85.5

Common Python data types are:

1. int – whole numbers
2. float – decimal numbers
3. str – text
4. bool – True or False
5. list – collection of values
6. tuple – ordered collection
7. dict – key-value pairs

Example:

age = 20
name = "Prave"
student = True
"""
                },
                {
                    "title": "3. Operators",
                    "content": """
Operators are symbols used to perform operations.

Arithmetic operators:
+ addition
- subtraction
* multiplication
/ division
% modulus
** power
// floor division

Example:

a = 10
b = 3

print(a + b)
print(a * b)
print(a % b)

Comparison operators include:
>, <, >=, <=, == and !=
"""
                },
                {
                    "title": "4. Conditional Statements",
                    "content": """
Conditional statements are used to make decisions.

The main statements are:
if
elif
else

Example:

age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")

The condition is checked and the appropriate block is executed.
"""
                },
                {
                    "title": "5. Loops",
                    "content": """
Loops are used to repeat a block of code.

Python mainly provides:

1. for loop
2. while loop

Example:

for i in range(5):
    print(i)

This prints numbers from 0 to 4.

A while loop continues as long as its condition is True.
"""
                },
                {
                    "title": "6. Functions",
                    "content": """
A function is a reusable block of code.

Functions are created using the def keyword.

Example:

def add(a, b):
    return a + b

result = add(10, 20)
print(result)

Advantages:
• Code reuse
• Better organization
• Easier debugging
"""
                }
            ],

            "questions": [
                {
                    "question": "Which keyword is used to define a function in Python?",
                    "options": ["function", "def", "fun", "define"],
                    "answer": "def"
                },
                {
                    "question": "Which data type is used for text?",
                    "options": ["int", "float", "str", "bool"],
                    "answer": "str"
                },
                {
                    "question": "Which symbol is used for multiplication?",
                    "options": ["+", "*", "%", "//"],
                    "answer": "*"
                },
                {
                    "question": "Which loop is commonly used to iterate over a sequence?",
                    "options": ["for", "if", "switch", "case"],
                    "answer": "for"
                },
                {
                    "question": "What does print() do?",
                    "options": [
                        "Takes input",
                        "Displays output",
                        "Creates a variable",
                        "Deletes data"
                    ],
                    "answer": "Displays output"
                }
            ]
        },

        "Intermediate": {
            "notes": [
                {
                    "title": "1. Object-Oriented Programming",
                    "content": """
Object-Oriented Programming (OOP) organizes programs using objects and classes.

A class is a blueprint for creating objects.

Example:

class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("Prave")

Important OOP concepts include:
• Class
• Object
• Inheritance
• Encapsulation
• Polymorphism
• Abstraction
"""
                },
                {
                    "title": "2. Exception Handling",
                    "content": """
Exception handling allows a program to handle errors without stopping suddenly.

Python uses:

try
except
else
finally

Example:

try:
    a = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

This makes programs more reliable.
"""
                },
                {
                    "title": "3. File Handling",
                    "content": """
Python can read and write files.

Common modes:
r – read
w – write
a – append

Example:

file = open("data.txt", "r")
content = file.read()
file.close()

The with statement is preferred because it automatically closes the file.
"""
                },
                {
                    "title": "4. Modules and Packages",
                    "content": """
A module is a Python file containing reusable code.

Example:

import math

print(math.sqrt(25))

Packages are collections of related modules.

Python provides many useful libraries such as:
• math
• random
• datetime
• os
• json
"""
                },
                {
                    "title": "5. List and Dictionary Comprehension",
                    "content": """
Comprehensions provide a shorter way to create collections.

List comprehension example:

numbers = [1, 2, 3, 4]
squares = [x*x for x in numbers]

Dictionary comprehension:

squares = {x: x*x for x in numbers}

They can make simple collection operations shorter and cleaner.
"""
                },
                {
                    "title": "6. Working with JSON",
                    "content": """
JSON is commonly used to exchange structured data between applications.

Python provides the json module.

Example:

import json

data = {"name": "Prave", "age": 20}

text = json.dumps(data)

dumps() converts Python data into JSON format.
loads() converts JSON text into Python data.
"""
                }
            ],

            "questions": [
                {
                    "question": "Which concept allows a class to acquire properties of another class?",
                    "options": ["Inheritance", "Compilation", "Iteration", "Parsing"],
                    "answer": "Inheritance"
                },
                {
                    "question": "Which block is used to handle an exception?",
                    "options": ["try-except", "if-else", "for", "def"],
                    "answer": "try-except"
                },
                {
                    "question": "Which mode is used to read a file?",
                    "options": ["r", "w", "a", "x"],
                    "answer": "r"
                },
                {
                    "question": "Which module is used to work with JSON?",
                    "options": ["json", "math", "os", "sys"],
                    "answer": "json"
                },
                {
                    "question": "What is a class?",
                    "options": [
                        "A blueprint for objects",
                        "A loop",
                        "A variable",
                        "An operator"
                    ],
                    "answer": "A blueprint for objects"
                }
            ]
        },

        "Advanced": {
            "notes": [
                {
                    "title": "1. Flask Web Development",
                    "content": """
Flask is a lightweight Python web framework.

It can be used to create web applications and APIs.

A basic Flask application contains:

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

Flask supports:
• Routes
• Templates
• Forms
• Sessions
• Database integration
• APIs
"""
                },
                {
                    "title": "2. REST APIs",
                    "content": """
An API allows different software applications to communicate.

REST APIs commonly use HTTP methods:

GET – retrieve data
POST – create/send data
PUT – update data
DELETE – remove data

APIs commonly exchange data using JSON.
"""
                },
                {
                    "title": "3. NumPy and Pandas",
                    "content": """
NumPy is used for numerical computing and arrays.

Pandas is widely used for data analysis.

Example:

import pandas as pd

data = pd.read_csv("students.csv")

Pandas provides DataFrame structures for working with tabular data.
"""
                },
                {
                    "title": "4. Machine Learning with Python",
                    "content": """
Python is widely used for machine learning.

A basic machine learning workflow is:

1. Collect data
2. Clean data
3. Explore data
4. Prepare features
5. Split training and testing data
6. Train model
7. Evaluate model
8. Deploy model

Popular libraries include:
• Scikit-learn
• TensorFlow
• PyTorch
"""
                },
                {
                    "title": "5. Database Integration",
                    "content": """
Python applications can connect to databases.

SQLite is useful for lightweight applications.

Example:

import sqlite3

conn = sqlite3.connect("learning.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

data = cursor.fetchall()

conn.close()
"""
                },
                {
                    "title": "6. Application Deployment",
                    "content": """
Deployment means making an application available for users.

A web application may be deployed using cloud platforms.

Before deployment:
• Test the application
• Secure sensitive information
• Configure environment variables
• Handle errors
• Optimize the application
"""
                }
            ],

            "questions": [
                {
                    "question": "Which Python framework is commonly used for lightweight web applications?",
                    "options": ["Flask", "NumPy", "Pandas", "Matplotlib"],
                    "answer": "Flask"
                },
                {
                    "question": "Which HTTP method is commonly used to retrieve data?",
                    "options": ["GET", "POST", "DELETE", "PATCH"],
                    "answer": "GET"
                },
                {
                    "question": "Which library is mainly used for tabular data analysis?",
                    "options": ["Pandas", "Flask", "Tkinter", "Requests"],
                    "answer": "Pandas"
                },
                {
                    "question": "What is the purpose of a machine learning model?",
                    "options": [
                        "Learn patterns from data",
                        "Only store files",
                        "Only display HTML",
                        "Only create folders"
                    ],
                    "answer": "Learn patterns from data"
                },
                {
                    "question": "Which database is lightweight and file-based?",
                    "options": ["SQLite", "Redis", "MongoDB", "Oracle"],
                    "answer": "SQLite"
                }
            ]
        }
    },


    # ========================================================
    # DBMS
    # ========================================================

    "DBMS": {

        "Beginner": {
            "notes": [
                {
                    "title": "1. Introduction to DBMS",
                    "content": """
A Database Management System (DBMS) is software used to store,
organize, manage and retrieve data.

Examples:
• MySQL
• PostgreSQL
• Oracle
• SQLite
• SQL Server

Advantages:
• Data organization
• Data security
• Easy retrieval
• Reduced duplication
"""
                },
                {
                    "title": "2. Tables and Records",
                    "content": """
A relational database stores data in tables.

A table contains:
• Rows – records
• Columns – attributes

Example Student table:

ID | Name | Department
1  | Ravi | AI&DS
2  | Priya | CSE

Each row represents one student record.
"""
                },
                {
                    "title": "3. SQL Basics",
                    "content": """
SQL stands for Structured Query Language.

Common commands:

CREATE – creates database objects
INSERT – adds records
SELECT – retrieves records
UPDATE – modifies records
DELETE – removes records

Example:

SELECT * FROM students;
"""
                },
                {
                    "title": "4. Primary Key",
                    "content": """
A primary key uniquely identifies each record in a table.

Example:

CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT
);

The ID should be unique for every student.
"""
                },
                {
                    "title": "5. Relationships",
                    "content": """
Tables can be related to each other.

Common relationships:
• One-to-one
• One-to-many
• Many-to-many

Foreign keys are used to connect related tables.
"""
                }
            ],

            "questions": [
                {
                    "question": "What does DBMS stand for?",
                    "options": [
                        "Database Management System",
                        "Data Backup Management System",
                        "Database Machine System",
                        "Data Management Software"
                    ],
                    "answer": "Database Management System"
                },
                {
                    "question": "Which SQL command retrieves data?",
                    "options": ["SELECT", "INSERT", "DELETE", "UPDATE"],
                    "answer": "SELECT"
                },
                {
                    "question": "What uniquely identifies a record?",
                    "options": ["Primary Key", "Foreign Key", "View", "Index"],
                    "answer": "Primary Key"
                },
                {
                    "question": "Which SQL command adds a record?",
                    "options": ["INSERT", "SELECT", "DROP", "UPDATE"],
                    "answer": "INSERT"
                },
                {
                    "question": "What does a row represent?",
                    "options": ["Record", "Database", "Column", "Table name"],
                    "answer": "Record"
                }
            ]
        },

        "Intermediate": {
            "notes": [
                {
                    "title": "1. SQL Joins",
                    "content": """
Joins combine data from multiple tables.

Common joins:
• INNER JOIN
• LEFT JOIN
• RIGHT JOIN
• FULL JOIN

Example:

SELECT students.name, departments.name
FROM students
INNER JOIN departments
ON students.dept_id = departments.id;
"""
                },
                {
                    "title": "2. Normalization",
                    "content": """
Normalization organizes database tables to reduce data redundancy.

Important normal forms:
1NF – atomic values
2NF – removes partial dependency
3NF – removes transitive dependency

Normalization improves consistency and reduces duplication.
"""
                },
                {
                    "title": "3. Constraints",
                    "content": """
Constraints are rules applied to table columns.

Common constraints:
• PRIMARY KEY
• FOREIGN KEY
• NOT NULL
• UNIQUE
• CHECK
• DEFAULT

They help maintain data integrity.
"""
                },
                {
                    "title": "4. Views",
                    "content": """
A view is a virtual table based on a SQL query.

Example:

CREATE VIEW student_view AS
SELECT name, department
FROM students;

Views can simplify complex queries and restrict access to sensitive columns.
"""
                },
                {
                    "title": "5. Indexing",
                    "content": """
An index improves the speed of searching and retrieving records.

Indexes are useful for frequently searched columns.

However, too many indexes can increase storage and slow down insert/update operations.
"""
                }
            ],

            "questions": [
                {
                    "question": "Which JOIN returns matching records from both tables?",
                    "options": ["INNER JOIN", "LEFT JOIN", "CROSS JOIN", "FULL JOIN"],
                    "answer": "INNER JOIN"
                },
                {
                    "question": "What is the main purpose of normalization?",
                    "options": [
                        "Reduce redundancy",
                        "Increase duplication",
                        "Delete tables",
                        "Remove SQL"
                    ],
                    "answer": "Reduce redundancy"
                },
                {
                    "question": "Which constraint prevents NULL values?",
                    "options": ["NOT NULL", "UNIQUE", "CHECK", "DEFAULT"],
                    "answer": "NOT NULL"
                },
                {
                    "question": "What is a view?",
                    "options": [
                        "Virtual table",
                        "Physical server",
                        "Backup file",
                        "Programming language"
                    ],
                    "answer": "Virtual table"
                },
                {
                    "question": "What generally improves search performance?",
                    "options": ["Index", "Trigger", "View", "Constraint"],
                    "answer": "Index"
                }
            ]
        },

        "Advanced": {
            "notes": [
                {
                    "title": "1. Transactions",
                    "content": """
A transaction is a group of database operations treated as one unit.

Transactions follow ACID properties:

Atomicity
Consistency
Isolation
Durability

COMMIT permanently saves changes.
ROLLBACK cancels changes.
"""
                },
                {
                    "title": "2. Stored Procedures",
                    "content": """
A stored procedure is a group of SQL statements stored in the database.

Benefits:
• Reusability
• Better organization
• Reduced repeated code
• Improved security in some scenarios
"""
                },
                {
                    "title": "3. Triggers",
                    "content": """
A trigger automatically executes when a specified database event occurs.

Triggers can respond to:
• INSERT
• UPDATE
• DELETE

They are useful for auditing and enforcing certain business rules.
"""
                },
                {
                    "title": "4. Query Optimization",
                    "content": """
Query optimization attempts to execute database queries efficiently.

Techniques include:
• Proper indexing
• Selecting only required columns
• Avoiding unnecessary joins
• Using efficient conditions
• Analyzing query execution plans
"""
                },
                {
                    "title": "5. Database Security",
                    "content": """
Database security protects data from unauthorized access.

Important techniques:
• Authentication
• Authorization
• Access control
• Encryption
• Backup
• Auditing

Applications should also use parameterized queries to reduce SQL injection risks.
"""
                }
            ],

            "questions": [
                {
                    "question": "Which ACID property means a transaction is all-or-nothing?",
                    "options": ["Atomicity", "Consistency", "Isolation", "Durability"],
                    "answer": "Atomicity"
                },
                {
                    "question": "Which command permanently saves a transaction?",
                    "options": ["COMMIT", "ROLLBACK", "DELETE", "DROP"],
                    "answer": "COMMIT"
                },
                {
                    "question": "What automatically executes after a database event?",
                    "options": ["Trigger", "View", "Index", "Schema"],
                    "answer": "Trigger"
                },
                {
                    "question": "What can improve query search performance?",
                    "options": ["Indexing", "Removing keys", "Deleting tables", "Ignoring constraints"],
                    "answer": "Indexing"
                },
                {
                    "question": "Which attack attempts to inject malicious SQL?",
                    "options": [
                        "SQL Injection",
                        "Phishing",
                        "DDoS",
                        "Buffer Overflow"
                    ],
                    "answer": "SQL Injection"
                }
            ]
        }
    },


    # ========================================================
    # OPERATING SYSTEM
    # ========================================================

    "Operating System": {

        "Beginner": {
            "notes": [
                {
                    "title": "1. Introduction to Operating Systems",
                    "content": """
An Operating System (OS) is system software that manages computer hardware
and provides services to application programs.

Examples:
• Windows
• Linux
• macOS
• Android

Main functions include:
• Process management
• Memory management
• File management
• Device management
• Security
"""
                },
                {
                    "title": "2. Processes",
                    "content": """
A process is a program that is currently executing.

A process has:
• Program code
• Data
• CPU state
• Memory information

The OS manages processes and allocates CPU time among them.
"""
                },
                {
                    "title": "3. Memory Management",
                    "content": """
Memory management controls how RAM is allocated to programs.

The OS keeps track of:
• Used memory
• Free memory
• Memory allocated to processes

Virtual memory allows systems to use disk space as an extension of RAM.
"""
                },
                {
                    "title": "4. File Management",
                    "content": """
The operating system manages files and folders.

Common operations:
• Create
• Read
• Write
• Rename
• Delete

File systems organize data on storage devices.
"""
                },
                {
                    "title": "5. Device Management",
                    "content": """
The OS manages hardware devices such as:
• Keyboard
• Mouse
• Printer
• Disk
• Network devices

Device drivers allow the operating system to communicate with hardware.
"""
                }
            ],

            "questions": [
                {
                    "question": "What is the main role of an operating system?",
                    "options": [
                        "Manage hardware and software resources",
                        "Only browse websites",
                        "Only create documents",
                        "Only play games"
                    ],
                    "answer": "Manage hardware and software resources"
                },
                {
                    "question": "What is a program currently executing called?",
                    "options": ["Process", "File", "Folder", "Driver"],
                    "answer": "Process"
                },
                {
                    "question": "Which component manages RAM?",
                    "options": [
                        "Memory management",
                        "File management",
                        "Printer driver",
                        "Compiler"
                    ],
                    "answer": "Memory management"
                },
                {
                    "question": "What helps the OS communicate with hardware?",
                    "options": ["Device driver", "Browser", "Database", "Compiler"],
                    "answer": "Device driver"
                },
                {
                    "question": "Which is an operating system?",
                    "options": ["Linux", "Python", "MySQL", "HTML"],
                    "answer": "Linux"
                }
            ]
        },

        "Intermediate": {
            "notes": [
                {
                    "title": "1. Process Scheduling",
                    "content": """
Process scheduling decides which process gets CPU time.

Common algorithms:
• FCFS
• SJF
• Round Robin
• Priority Scheduling

Round Robin uses a time quantum and is useful in time-sharing systems.
"""
                },
                {
                    "title": "2. Threads",
                    "content": """
A thread is a smaller unit of execution within a process.

Multiple threads can exist within one process.

Advantages:
• Better responsiveness
• Resource sharing
• Improved concurrency
"""
                },
                {
                    "title": "3. Deadlocks",
                    "content": """
A deadlock occurs when processes wait indefinitely for resources held by each other.

Four necessary conditions are:
• Mutual exclusion
• Hold and wait
• No preemption
• Circular wait
"""
                },
                {
                    "title": "4. Paging",
                    "content": """
Paging divides memory into fixed-size pages and physical memory into frames.

It helps implement virtual memory and reduces external fragmentation.
"""
                },
                {
                    "title": "5. Synchronization",
                    "content": """
Process synchronization coordinates processes that share resources.

Common mechanisms:
• Mutex
• Semaphore
• Monitor

Synchronization helps prevent race conditions.
"""
                }
            ],

            "questions": [
                {
                    "question": "Which scheduling algorithm uses a time quantum?",
                    "options": ["Round Robin", "FCFS", "SJF", "FIFO"],
                    "answer": "Round Robin"
                },
                {
                    "question": "Which is a necessary condition for deadlock?",
                    "options": [
                        "Circular wait",
                        "Compilation",
                        "Paging",
                        "Booting"
                    ],
                    "answer": "Circular wait"
                },
                {
                    "question": "What is a thread?",
                    "options": [
                        "Unit of execution",
                        "Storage device",
                        "Database",
                        "File"
                    ],
                    "answer": "Unit of execution"
                },
                {
                    "question": "Paging divides logical memory into what?",
                    "options": ["Pages", "Segments", "Files", "Blocks only"],
                    "answer": "Pages"
                },
                {
                    "question": "Which mechanism is used for synchronization?",
                    "options": ["Semaphore", "Compiler", "Browser", "Loader"],
                    "answer": "Semaphore"
                }
            ]
        },

        "Advanced": {
            "notes": [
                {
                    "title": "1. Virtual Memory",
                    "content": """
Virtual memory allows a system to execute programs that may require more
memory than the available physical RAM.

Techniques include:
• Demand paging
• Page replacement
• Swapping

Common page replacement algorithms include FIFO, LRU and Optimal.
"""
                },
                {
                    "title": "2. Page Replacement",
                    "content": """
When a required page is not in physical memory, a page fault occurs.

The OS must choose a page to remove.

Algorithms:
• FIFO
• LRU
• Optimal

LRU removes the page that has not been used for the longest time.
"""
                },
                {
                    "title": "3. File Systems",
                    "content": """
A file system manages how files are stored and organized.

Examples include:
• NTFS
• FAT32
• ext4

File systems maintain metadata and structures needed to locate files.
"""
                },
                {
                    "title": "4. Operating System Security",
                    "content": """
OS security protects resources from unauthorized access.

Important mechanisms:
• User authentication
• Permissions
• Access control
• Encryption
• Process isolation
• Security updates
"""
                },
                {
                    "title": "5. Distributed Operating Systems",
                    "content": """
A distributed operating system manages resources across multiple connected
computers.

Goals include:
• Resource sharing
• Load balancing
• Fault tolerance
• Distributed processing

The system attempts to provide users with a unified computing environment.
"""
                }
            ],

            "questions": [
                {
                    "question": "Which page replacement algorithm uses the least recently used page?",
                    "options": ["LRU", "FIFO", "FCFS", "SJF"],
                    "answer": "LRU"
                },
                {
                    "question": "What occurs when a required page is not in memory?",
                    "options": ["Page fault", "Deadlock", "Compile error", "Boot failure"],
                    "answer": "Page fault"
                },
                {
                    "question": "Which is a Linux file system?",
                    "options": ["ext4", "NTFS", "FAT32", "All of these"],
                    "answer": "ext4"
                },
                {
                    "question": "What protects files from unauthorized users?",
                    "options": ["Access control", "Looping", "Paging", "Compilation"],
                    "answer": "Access control"
                },
                {
                    "question": "What does a distributed OS manage?",
                    "options": [
                        "Resources across multiple computers",
                        "Only one file",
                        "Only RAM",
                        "Only a printer"
                    ],
                    "answer": "Resources across multiple computers"
                }
            ]
        }
    },


    # ========================================================
    # APTITUDE
    # ========================================================

    "Aptitude": {

        "Easy": {
            "notes": [
                {
                    "title": "1. Number Basics",
                    "content": """
Numbers are the foundation of aptitude problems.

Important types:
• Natural numbers: 1, 2, 3...
• Whole numbers: 0, 1, 2...
• Integers: ..., -2, -1, 0, 1, 2...
• Even numbers: divisible by 2
• Odd numbers: not divisible by 2

Example:
24 is even because 24 is divisible by 2.
"""
                },
                {
                    "title": "2. Percentages",
                    "content": """
Percentage means a value out of 100.

Formula:

Percentage = (Part / Total) × 100

Example:

If 20 students out of 50 pass:

Percentage = (20/50) × 100
= 40%
"""
                },
                {
                    "title": "3. Profit and Loss",
                    "content": """
Cost Price (CP) is the price paid for an item.

Selling Price (SP) is the price received after selling it.

Profit = SP - CP

Loss = CP - SP

Profit Percentage = (Profit / CP) × 100
"""
                },
                {
                    "title": "4. Ratio",
                    "content": """
A ratio compares two quantities.

Example:

If boys = 20 and girls = 30:

Ratio = 20:30
= 2:3

Ratios can be simplified by dividing both terms by their common factor.
"""
                },
                {
                    "title": "5. Average",
                    "content": """
Average is calculated by:

Average = Sum of values / Number of values

Example:

Numbers: 10, 20, 30

Average = 60/3
= 20
"""
                }
            ],

            "questions": [
                {
                    "question": "What is 20% of 100?",
                    "options": ["10", "20", "30", "40"],
                    "answer": "20"
                },
                {
                    "question": "If CP = ₹100 and SP = ₹120, what is the profit?",
                    "options": ["₹10", "₹20", "₹30", "₹40"],
                    "answer": "₹20"
                },
                {
                    "question": "What is the average of 10 and 20?",
                    "options": ["10", "15", "20", "30"],
                    "answer": "15"
                },
                {
                    "question": "What is the ratio 20:30 in simplest form?",
                    "options": ["1:2", "2:3", "3:2", "2:5"],
                    "answer": "2:3"
                },
                {
                    "question": "Which number is even?",
                    "options": ["11", "15", "18", "21"],
                    "answer": "18"
                }
            ]
        },

        "Medium": {
            "notes": [
                {
                    "title": "1. Time and Work",
                    "content": """
Time and work problems deal with how quickly people or machines complete work.

If a person completes a work in 10 days:

One-day work = 1/10

If another person completes it in 20 days:

One-day work = 1/20

Together:

1/10 + 1/20 = 3/20
"""
                },
                {
                    "title": "2. Speed, Distance and Time",
                    "content": """
The basic formula is:

Speed = Distance / Time

Therefore:

Distance = Speed × Time

Time = Distance / Speed

Example:

A car travels 120 km in 3 hours.

Speed = 120/3
= 40 km/h
"""
                },
                {
                    "title": "3. Simple Interest",
                    "content": """
Simple Interest is calculated using:

SI = (P × R × T) / 100

P = Principal
R = Rate
T = Time

Example:

P = ₹1000
R = 10%
T = 2 years

SI = ₹200
"""
                },
                {
                    "title": "4. Probability",
                    "content": """
Probability measures the chance of an event.

Formula:

Probability = Favorable outcomes / Total outcomes

For a fair coin:

Probability of getting Heads = 1/2.
"""
                },
                {
                    "title": "5. Data Interpretation",
                    "content": """
Data interpretation involves analyzing tables, charts and graphs.

Common calculations:
• Percentage
• Difference
• Ratio
• Average
• Growth rate

Read the data carefully before calculating.
"""
                }
            ],

            "questions": [
                {
                    "question": "A car travels 120 km in 3 hours. What is its speed?",
                    "options": ["30 km/h", "40 km/h", "50 km/h", "60 km/h"],
                    "answer": "40 km/h"
                },
                {
                    "question": "What is the simple interest on ₹1000 at 10% for 2 years?",
                    "options": ["₹100", "₹150", "₹200", "₹250"],
                    "answer": "₹200"
                },
                {
                    "question": "What is the probability of getting heads on a fair coin?",
                    "options": ["1/4", "1/2", "1", "2"],
                    "answer": "1/2"
                },
                {
                    "question": "If a work takes 10 days, what is the one-day work?",
                    "options": ["1/5", "1/10", "10", "5"],
                    "answer": "1/10"
                },
                {
                    "question": "Which formula gives speed?",
                    "options": [
                        "Distance/Time",
                        "Time/Distance",
                        "Distance×Time",
                        "Distance+Time"
                    ],
                    "answer": "Distance/Time"
                }
            ]
        },

        "Hard": {
            "notes": [
                {
                    "title": "1. Compound Interest",
                    "content": """
Compound interest is calculated on the principal plus accumulated interest.

Formula:

A = P(1 + R/100)^T

Compound Interest = A - P

Where:
P = Principal
R = Rate
T = Time
A = Final amount
"""
                },
                {
                    "title": "2. Permutations",
                    "content": """
Permutation deals with arrangements where order matters.

Formula:

nPr = n! / (n-r)!

Example:

Arranging 3 objects from 5:

5P3 = 5! / 2!
= 60
"""
                },
                {
                    "title": "3. Combinations",
                    "content": """
Combination deals with selections where order does not matter.

Formula:

nCr = n! / (r!(n-r)!)

For example, selecting 2 students from 5:

5C2 = 10
"""
                },
                {
                    "title": "4. Advanced Probability",
                    "content": """
Probability can involve multiple events.

For independent events:

P(A and B) = P(A) × P(B)

For mutually exclusive events:

P(A or B) = P(A) + P(B)

Carefully identify the type of event before selecting a formula.
"""
                },
                {
                    "title": "5. Logical Reasoning",
                    "content": """
Logical reasoning tests the ability to identify patterns and relationships.

Common areas:
• Number series
• Coding-decoding
• Blood relations
• Directions
• Seating arrangements
• Syllogisms

The key is to identify the rule or relationship before solving.
"""
                }
            ],

            "questions": [
                {
                    "question": "What is 5P2?",
                    "options": ["10", "20", "25", "15"],
                    "answer": "20"
                },
                {
                    "question": "What is 5C2?",
                    "options": ["5", "10", "15", "20"],
                    "answer": "10"
                },
                {
                    "question": "In permutations, does order matter?",
                    "options": ["Yes", "No", "Sometimes never", "Only for zero"],
                    "answer": "Yes"
                },
                {
                    "question": "Which formula is used for compound amount?",
                    "options": [
                        "P(1+R/100)^T",
                        "P+R+T",
                        "P×R×T",
                        "P/R"
                    ],
                    "answer": "P(1+R/100)^T"
                },
                {
                    "question": "Which topic involves arranging people in positions?",
                    "options": [
                        "Seating arrangement",
                        "Percentage",
                        "Simple interest",
                        "Average"
                    ],
                    "answer": "Seating arrangement"
                }
            ]
        }
    }
}