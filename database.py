import sqlite3

conn = sqlite3.connect("database/learning.db")
cursor = conn.cursor()

# Student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    regno TEXT,
    subject TEXT,
    level TEXT
)
""")

# Quiz results table
cursor.execute("""
CREATE TABLE IF NOT EXISTS quiz_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    regno TEXT,
    subject TEXT,
    level TEXT,
    score INTEGER,
    percentage REAL
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")