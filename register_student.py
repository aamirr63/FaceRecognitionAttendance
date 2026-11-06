import sqlite3
import os

def register_student(student_id, name, department, course, semester):

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO students(student_id,name,department,course,semester)
        VALUES(?,?,?,?,?)
        """,(student_id,name,department,course,semester))

        conn.commit()

        # Dataset Folder
        folder_name = f"{name.lower()}_{student_id}"
        folder_path = os.path.join("dataset",folder_name)

        os.makedirs(folder_path,exist_ok=True)

        print("✅ Student Registered Successfully")
        print("Folder Created :",folder_path)

    except sqlite3.IntegrityError:

        print("❌ Student ID Already Exists")

    conn.close()


if __name__=="__main__":

    student_id=input("Student ID : ")
    name=input("Student Name : ")
    department=input("Department : ")
    course=input("Course : ")
    semester=input("Semester : ")

    register_student(student_id,name,department,course,semester)