import sqlite3
from datetime import datetime

DB_NAME = "db/students.db"


# ==========================
# Database Connection
# ==========================

def connect_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    return conn, cursor


# ==========================
# Create Tables
# ==========================

def create_tables():
    conn, cursor = connect_db()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT UNIQUE,
        name TEXT,
        course TEXT,
        mobile TEXT,
        email TEXT,
        gender TEXT,
        image_count INTEGER DEFAULT 0,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()


# ==========================
# Add Student
# ==========================

def add_student(
    student_id,
    name,
    course,
    mobile,
    email,
    gender,
):

    conn, cursor = connect_db()

    cursor.execute("""
    INSERT INTO students
    (
        student_id,
        name,
        course,
        mobile,
        email,
        gender,
        image_count,
        created_at
    )

    VALUES(?,?,?,?,?,?,?,?)
    """,

    (
        student_id,
        name,
        course,
        mobile,
        email,
        gender,
        image_count,
        datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    ))

    conn.commit()
    conn.close()


# ==========================
# Get All Students
# ==========================

def get_students():

    conn, cursor = connect_db()

    cursor.execute("SELECT * FROM students")

    rows = cursor.fetchall()

    conn.close()

    return rows


# ==========================
# Search Student
# ==========================

def search_student(keyword):

    conn, cursor = connect_db()

    cursor.execute("""

    SELECT * FROM students

    WHERE

    student_id LIKE ?

    OR

    name LIKE ?

    """,

    (f"%{keyword}%", f"%{keyword}%"))

    rows = cursor.fetchall()

    conn.close()

    return rows


# ==========================
# Delete Student
# ==========================

def delete_student(student_id):

    conn, cursor = connect_db()

    cursor.execute(

        "DELETE FROM students WHERE student_id=?",

        (student_id,)
    )

    conn.commit()

    conn.close()


# ==========================
# Update Student
# ==========================

def update_student(student_id,
                   name,
                   course,
                   mobile,
                   email,
                   gender):

    conn, cursor = connect_db()

    cursor.execute("""

    UPDATE students

    SET

    name=?,
    course=?,
    mobile=?,
    email=?,
    gender=?

    WHERE student_id=?

    """,

    (
        name,
        course,
        mobile,
        email,
        gender,
        student_id
    ))

    conn.commit()

    conn.close()


# ==========================
# Total Students
# ==========================

def total_students():

    conn, cursor = connect_db()

    cursor.execute("SELECT COUNT(*) FROM students")

    total = cursor.fetchone()[0]

    conn.close()

    return total


# ==========================
# Run Once
# ==========================

create_tables()