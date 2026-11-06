import sqlite3

# Database connect
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Student Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    student_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT,
    course TEXT,
    semester TEXT
)
""")
# Admin Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS admin(
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
""")

# Default Admin
cursor.execute("""
INSERT OR IGNORE INTO admin(username,password)
VALUES('Chahat','chahatbhai')
""")

conn.commit()
conn.close()

print("✅ Database Created Successfully")
