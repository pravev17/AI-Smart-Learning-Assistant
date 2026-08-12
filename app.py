from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)


# =========================================================
# QUIZ QUESTION BANK
# =========================================================

QUESTION_BANK = {

    # =====================================================
    # PYTHON
    # =====================================================

    "python": {

        "beginner": [
            {
                "question": "What type of language is Python?",
                "options": [
                    "Programming Language",
                    "Markup Language",
                    "Database",
                    "Operating System"
                ],
                "answer": "Programming Language"
            },
            {
                "question": "Which symbol is used for comments in Python?",
                "options": [
                    "#",
                    "//",
                    "/*",
                    "<!--"
                ],
                "answer": "#"
            },
            {
                "question": "Which keyword is used to define a function?",
                "options": [
                    "function",
                    "def",
                    "fun",
                    "define"
                ],
                "answer": "def"
            },
            {
                "question": "Which of the following is a Python list?",
                "options": [
                    "[1, 2, 3]",
                    "(1, 2, 3)",
                    "{1, 2, 3}",
                    "<1, 2, 3>"
                ],
                "answer": "[1, 2, 3]"
            },
            {
                "question": "Which keyword is commonly used for looping through a sequence?",
                "options": [
                    "for",
                    "loop",
                    "repeat",
                    "iterate"
                ],
                "answer": "for"
            }
        ],

        "intermediate": [
            {
                "question": "Which data structure stores key-value pairs in Python?",
                "options": [
                    "List",
                    "Tuple",
                    "Dictionary",
                    "Set"
                ],
                "answer": "Dictionary"
            },
            {
                "question": "What does len() return?",
                "options": [
                    "Data type",
                    "Number of items",
                    "Memory address",
                    "Variable name"
                ],
                "answer": "Number of items"
            },
            {
                "question": "Which keyword is used to handle exceptions?",
                "options": [
                    "try",
                    "check",
                    "error",
                    "handle"
                ],
                "answer": "try"
            },
            {
                "question": "What is the output of 10 // 3?",
                "options": [
                    "3",
                    "3.33",
                    "1",
                    "4"
                ],
                "answer": "3"
            },
            {
                "question": "Which function converts a value into an integer?",
                "options": [
                    "str()",
                    "float()",
                    "int()",
                    "number()"
                ],
                "answer": "int()"
            }
        ],

        "advanced": [
            {
                "question": "Which concept allows a class to inherit properties from another class?",
                "options": [
                    "Inheritance",
                    "Encapsulation",
                    "Iteration",
                    "Compilation"
                ],
                "answer": "Inheritance"
            },
            {
                "question": "What does a Python decorator modify?",
                "options": [
                    "Function or class behavior",
                    "Database",
                    "Operating system",
                    "Hardware"
                ],
                "answer": "Function or class behavior"
            },
            {
                "question": "Which keyword creates a generator value?",
                "options": [
                    "return",
                    "yield",
                    "generate",
                    "next"
                ],
                "answer": "yield"
            },
            {
                "question": "Which method is called when an object is initialized?",
                "options": [
                    "__start__()",
                    "__init__()",
                    "__create__()",
                    "__newobject__()"
                ],
                "answer": "__init__()"
            },
            {
                "question": "What is list comprehension mainly used for?",
                "options": [
                    "Creating lists concisely",
                    "Deleting databases",
                    "Creating classes only",
                    "Managing files only"
                ],
                "answer": "Creating lists concisely"
            }
        ]
    },


    # =====================================================
    # DBMS
    # =====================================================

    "dbms": {

        "beginner": [
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
                "question": "Which language is commonly used to query relational databases?",
                "options": [
                    "SQL",
                    "HTML",
                    "CSS",
                    "Python only"
                ],
                "answer": "SQL"
            },
            {
                "question": "What is a table used for?",
                "options": [
                    "Storing data",
                    "Running an operating system",
                    "Creating images",
                    "Sending emails"
                ],
                "answer": "Storing data"
            },
            {
                "question": "Which key uniquely identifies a record?",
                "options": [
                    "Primary Key",
                    "Foreign Key",
                    "Normal Key",
                    "Secondary Key"
                ],
                "answer": "Primary Key"
            },
            {
                "question": "Which command is used to retrieve data?",
                "options": [
                    "SELECT",
                    "INSERT",
                    "DELETE",
                    "CREATE"
                ],
                "answer": "SELECT"
            }
        ],

        "intermediate": [
            {
                "question": "Which SQL command adds a new record?",
                "options": [
                    "INSERT",
                    "ADD",
                    "PUT",
                    "UPDATE"
                ],
                "answer": "INSERT"
            },
            {
                "question": "Which SQL command modifies existing data?",
                "options": [
                    "CHANGE",
                    "UPDATE",
                    "MODIFY",
                    "EDIT"
                ],
                "answer": "UPDATE"
            },
            {
                "question": "What is a foreign key used for?",
                "options": [
                    "Linking tables",
                    "Deleting tables",
                    "Creating passwords",
                    "Sorting files"
                ],
                "answer": "Linking tables"
            },
            {
                "question": "Which clause filters rows in SQL?",
                "options": [
                    "WHERE",
                    "FILTER",
                    "IF",
                    "CHECK"
                ],
                "answer": "WHERE"
            },
            {
                "question": "Which SQL command removes records?",
                "options": [
                    "REMOVE",
                    "DELETE",
                    "CLEAR",
                    "DROP ROW"
                ],
                "answer": "DELETE"
            }
        ],

        "advanced": [
            {
                "question": "What is normalization used for?",
                "options": [
                    "Reducing data redundancy",
                    "Increasing duplicate data",
                    "Deleting all records",
                    "Creating operating systems"
                ],
                "answer": "Reducing data redundancy"
            },
            {
                "question": "Which normal form removes partial dependency?",
                "options": [
                    "1NF",
                    "2NF",
                    "3NF",
                    "BCNF only"
                ],
                "answer": "2NF"
            },
            {
                "question": "What does ACID stand for in transactions?",
                "options": [
                    "Atomicity, Consistency, Isolation, Durability",
                    "Accuracy, Control, Integrity, Data",
                    "Access, Control, Isolation, Data",
                    "Atomicity, Control, Integrity, Durability"
                ],
                "answer": "Atomicity, Consistency, Isolation, Durability"
            },
            {
                "question": "Which JOIN returns matching rows from both tables?",
                "options": [
                    "INNER JOIN",
                    "OUTER JOIN",
                    "CROSS JOIN",
                    "FULL JOIN"
                ],
                "answer": "INNER JOIN"
            },
            {
                "question": "What is an index mainly used for?",
                "options": [
                    "Improving data retrieval speed",
                    "Deleting records",
                    "Creating backups only",
                    "Changing table names"
                ],
                "answer": "Improving data retrieval speed"
            }
        ]
    },


    # =====================================================
    # OPERATING SYSTEM
    # =====================================================

    "operating_system": {

        "beginner": [
            {
                "question": "What is an Operating System?",
                "options": [
                    "System software",
                    "Application software",
                    "Programming language",
                    "Database"
                ],
                "answer": "System software"
            },
            {
                "question": "Which is an example of an Operating System?",
                "options": [
                    "Windows",
                    "Python",
                    "MySQL",
                    "HTML"
                ],
                "answer": "Windows"
            },
            {
                "question": "What manages computer hardware and software resources?",
                "options": [
                    "Operating System",
                    "Browser",
                    "Compiler",
                    "Text editor"
                ],
                "answer": "Operating System"
            },
            {
                "question": "What is a process?",
                "options": [
                    "A program in execution",
                    "A file only",
                    "A folder",
                    "A hardware device"
                ],
                "answer": "A program in execution"
            },
            {
                "question": "Which component is the core of an operating system?",
                "options": [
                    "Kernel",
                    "Browser",
                    "Keyboard",
                    "Monitor"
                ],
                "answer": "Kernel"
            }
        ],

        "intermediate": [
            {
                "question": "What is multitasking?",
                "options": [
                    "Running multiple tasks",
                    "Deleting files",
                    "Installing software",
                    "Formatting disks"
                ],
                "answer": "Running multiple tasks"
            },
            {
                "question": "Which scheduling algorithm executes processes in arrival order?",
                "options": [
                    "FCFS",
                    "Round Robin",
                    "Priority",
                    "SJF"
                ],
                "answer": "FCFS"
            },
            {
                "question": "What is virtual memory?",
                "options": [
                    "Using disk space as an extension of memory",
                    "A physical CPU",
                    "A network cable",
                    "A type of keyboard"
                ],
                "answer": "Using disk space as an extension of memory"
            },
            {
                "question": "Which technique divides memory into fixed-size blocks?",
                "options": [
                    "Paging",
                    "Scheduling",
                    "Spooling",
                    "Deadlock"
                ],
                "answer": "Paging"
            },
            {
                "question": "What is a thread?",
                "options": [
                    "Smallest unit of CPU execution",
                    "Storage device",
                    "Network protocol",
                    "File system"
                ],
                "answer": "Smallest unit of CPU execution"
            }
        ],

        "advanced": [
            {
                "question": "What is deadlock?",
                "options": [
                    "Processes waiting indefinitely for resources",
                    "Fast process execution",
                    "Memory allocation",
                    "File creation"
                ],
                "answer": "Processes waiting indefinitely for resources"
            },
            {
                "question": "Which is a necessary condition for deadlock?",
                "options": [
                    "Mutual exclusion",
                    "Compilation",
                    "Multitasking",
                    "Paging"
                ],
                "answer": "Mutual exclusion"
            },
            {
                "question": "What is a semaphore used for?",
                "options": [
                    "Process synchronization",
                    "File compression",
                    "Disk formatting",
                    "Network browsing"
                ],
                "answer": "Process synchronization"
            },
            {
                "question": "Which page replacement algorithm removes the page that has not been used for the longest time?",
                "options": [
                    "LRU",
                    "FIFO",
                    "FCFS",
                    "SJF"
                ],
                "answer": "LRU"
            },
            {
                "question": "What does thrashing mainly involve?",
                "options": [
                    "Excessive page swapping",
                    "CPU overheating",
                    "File deletion",
                    "Network failure"
                ],
                "answer": "Excessive page swapping"
            }
        ]
    },


    # =====================================================
    # APTITUDE
    # =====================================================

    "aptitude": {

        "beginner": [
            {
                "question": "What is 20% of 100?",
                "options": [
                    "10",
                    "20",
                    "30",
                    "40"
                ],
                "answer": "20"
            },
            {
                "question": "If a number is 10 and another is 20, what is their sum?",
                "options": [
                    "20",
                    "25",
                    "30",
                    "40"
                ],
                "answer": "30"
            },
            {
                "question": "What is 5 × 6?",
                "options": [
                    "25",
                    "30",
                    "35",
                    "40"
                ],
                "answer": "30"
            },
            {
                "question": "What is the average of 10 and 20?",
                "options": [
                    "10",
                    "15",
                    "20",
                    "25"
                ],
                "answer": "15"
            },
            {
                "question": "What is 100 divided by 10?",
                "options": [
                    "5",
                    "10",
                    "20",
                    "50"
                ],
                "answer": "10"
            }
        ],

        "intermediate": [
            {
                "question": "A product costs ₹500 and has a 10% discount. What is the discount amount?",
                "options": [
                    "₹25",
                    "₹50",
                    "₹75",
                    "₹100"
                ],
                "answer": "₹50"
            },
            {
                "question": "If a car travels 60 km in 1 hour, how far will it travel in 3 hours?",
                "options": [
                    "120 km",
                    "150 km",
                    "180 km",
                    "200 km"
                ],
                "answer": "180 km"
            },
            {
                "question": "What is the ratio 20:40 in simplest form?",
                "options": [
                    "1:2",
                    "2:3",
                    "1:3",
                    "2:1"
                ],
                "answer": "1:2"
            },
            {
                "question": "If 5 workers complete a job in 10 days, this is a simple example of what?",
                "options": [
                    "Time and Work",
                    "Probability",
                    "Profit and Loss",
                    "Permutation"
                ],
                "answer": "Time and Work"
            },
            {
                "question": "What is the simple interest on ₹1000 at 10% per year for 1 year?",
                "options": [
                    "₹10",
                    "₹50",
                    "₹100",
                    "₹200"
                ],
                "answer": "₹100"
            }
        ],

        "advanced": [
            {
                "question": "If a train travels 120 km in 2 hours, what is its average speed?",
                "options": [
                    "40 km/h",
                    "50 km/h",
                    "60 km/h",
                    "80 km/h"
                ],
                "answer": "60 km/h"
            },
            {
                "question": "What is the probability of getting a head when a fair coin is tossed?",
                "options": [
                    "1/4",
                    "1/2",
                    "1",
                    "2"
                ],
                "answer": "1/2"
            },
            {
                "question": "If x + 5 = 15, what is x?",
                "options": [
                    "5",
                    "10",
                    "15",
                    "20"
                ],
                "answer": "10"
            },
            {
                "question": "What is 25% expressed as a fraction?",
                "options": [
                    "1/2",
                    "1/3",
                    "1/4",
                    "3/4"
                ],
                "answer": "1/4"
            },
            {
                "question": "A number increases from 100 to 120. What is the percentage increase?",
                "options": [
                    "10%",
                    "15%",
                    "20%",
                    "25%"
                ],
                "answer": "20%"
            }
        ]
    }
}


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def normalize_subject(subject):

    subject = str(subject).strip().lower()

    subject = (
        subject
        .replace(" ", "_")
        .replace("-", "_")
    )

    if subject in ["os", "operatingsystem"]:
        return "operating_system"

    return subject


def normalize_level(level):

    level = str(level).strip().lower()

    level_map = {
        "easy": "beginner",
        "beginner": "beginner",
        "medium": "intermediate",
        "intermediate": "intermediate",
        "hard": "advanced",
        "advanced": "advanced"
    }

    return level_map.get(level, level)


# =========================================================
# FIND NOTES FILE
# =========================================================

def find_notes_file(subject, level):

    subject_name = normalize_subject(subject)
    level_name = normalize_level(level)

    content_folder = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "content"
    )

    if not os.path.exists(content_folder):
        return None

    def normalize(text):
        return (
            text.lower()
            .replace(" ", "")
            .replace("_", "")
            .replace("-", "")
        )

    for folder_name in os.listdir(content_folder):

        folder_path = os.path.join(
            content_folder,
            folder_name
        )

        if not os.path.isdir(folder_path):
            continue

        if normalize(folder_name) == normalize(subject_name):

            for file_name in os.listdir(folder_path):

                if not file_name.lower().endswith(".txt"):
                    continue

                file_without_extension = os.path.splitext(
                    file_name
                )[0]

                if normalize(file_without_extension) == normalize(level_name):

                    return os.path.join(
                        folder_path,
                        file_name
                    )

    return None


# =========================================================
# GET NOTES
# =========================================================

def get_notes(subject, level):

    file_path = find_notes_file(
        subject,
        level
    )

    if file_path is None:

        return (
            "Notes are not available for "
            + str(subject)
            + " - "
            + str(level)
            + "."
        )

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()

    except Exception as e:

        return "Unable to load notes: " + str(e)


# =========================================================
# LOGIN
# =========================================================

@app.route("/")
def login():

    return render_template(
        "login.html"
    )


# =========================================================
# HOME
# =========================================================

@app.route("/home", methods=["POST"])
def home():

    name = request.form.get(
        "name",
        ""
    )

    regno = request.form.get(
        "regno",
        ""
    )

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

    name = request.form.get(
        "name",
        ""
    )

    regno = request.form.get(
        "regno",
        ""
    )

    subject = request.form.get(
        "subject",
        ""
    )

    return render_template(
        "level.html",
        name=name,
        regno=regno,
        subject=subject
    )


# =========================================================
# RECOMMENDATION + NOTES
# =========================================================

@app.route("/recommendation", methods=["POST"])
def recommendation():

    name = request.form.get(
        "name",
        ""
    )

    regno = request.form.get(
        "regno",
        ""
    )

    subject = request.form.get(
        "subject",
        ""
    )

    level = request.form.get(
        "level",
        ""
    )

    # Save student details
    conn = sqlite3.connect(
        "database/learning.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO students
        (name, regno, subject, level)
        VALUES (?, ?, ?, ?)
        """,
        (
            name,
            regno,
            subject,
            level
        )
    )

    conn.commit()
    conn.close()

    # Recommendations
    actual_level = normalize_level(level)

    if actual_level == "beginner":

        topics = [
            "Basic concepts",
            "Fundamentals",
            "Simple examples",
            "Practice basic questions"
        ]

    elif actual_level == "intermediate":

        topics = [
            "Intermediate concepts",
            "Problem solving",
            "Practical examples",
            "Practice intermediate questions"
        ]

    else:

        topics = [
            "Advanced concepts",
            "Advanced problem solving",
            "Real-world applications",
            "Practice advanced questions"
        ]

    # Get actual notes
    content = get_notes(
        subject,
        level
    )

    return render_template(
        "recommendation.html",
        name=name,
        regno=regno,
        subject=subject,
        level=level,
        topics=topics,
        content=content
    )


# =========================================================
# NOTES PAGE
# =========================================================

@app.route("/notes", methods=["GET", "POST"])
def notes():

    if request.method == "POST":

        name = request.form.get(
            "name",
            ""
        )

        regno = request.form.get(
            "regno",
            ""
        )

        subject = request.form.get(
            "subject",
            ""
        )

        level = request.form.get(
            "level",
            ""
        )

    else:

        name = request.args.get(
            "name",
            ""
        )

        regno = request.args.get(
            "regno",
            ""
        )

        subject = request.args.get(
            "subject",
            ""
        )

        level = request.args.get(
            "level",
            ""
        )

    content = get_notes(
        subject,
        level
    )

    return render_template(
        "notes.html",
        name=name,
        regno=regno,
        subject=subject,
        level=level,
        content=content
    )


# =========================================================
# QUIZ PAGE
# =========================================================

@app.route("/quiz", methods=["POST"])
def quiz():

    name = request.form.get(
        "name",
        ""
    )

    regno = request.form.get(
        "regno",
        ""
    )

    subject = request.form.get(
        "subject",
        ""
    )

    level = request.form.get(
        "level",
        ""
    )

    subject_key = normalize_subject(
        subject
    )

    level_key = normalize_level(
        level
    )

    questions = QUESTION_BANK.get(
        subject_key,
        {}
    ).get(
        level_key,
        []
    )

    return render_template(
        "quiz.html",
        name=name,
        regno=regno,
        subject=subject,
        level=level,
        questions=questions
    )


# =========================================================
# SUBMIT QUIZ
# =========================================================

@app.route("/submit_quiz", methods=["POST"])
def submit_quiz():

    name = request.form.get(
        "name",
        ""
    )

    regno = request.form.get(
        "regno",
        ""
    )

    subject = request.form.get(
        "subject",
        ""
    )

    level = request.form.get(
        "level",
        ""
    )

    subject_key = normalize_subject(
        subject
    )

    level_key = normalize_level(
        level
    )

    questions = QUESTION_BANK.get(
        subject_key,
        {}
    ).get(
        level_key,
        []
    )

    score = 0

    # Check answers
    for index, question in enumerate(
        questions,
        start=1
    ):

        selected_answer = request.form.get(
            "q" + str(index)
        )

        if selected_answer == question["answer"]:

            score += 1

    total_questions = len(
        questions
    )

    if total_questions > 0:

        percentage = (
            score / total_questions
        ) * 100

    else:

        percentage = 0

    # Save result
    conn = sqlite3.connect(
        "database/learning.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO quiz_results
        (name, regno, subject, level, score, percentage)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            name,
            regno,
            subject,
            level,
            score,
            percentage
        )
    )

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
# DASHBOARD
# =========================================================

@app.route("/dashboard", methods=["POST"])
def dashboard():

    name = request.form.get(
        "name",
        ""
    )

    conn = sqlite3.connect(
        "database/learning.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT subject, level
        FROM students
        WHERE name=?
        """,
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
# RUN APP
# =========================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )