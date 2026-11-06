import customtkinter as ctk
from tkinter import messagebox

from components.student_table import StudentTable
from db.db import (
    add_student,
    get_students,
    update_student,
    delete_student
)


class StudentPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        
        # Build UI First
        self.build_ui()

        # Initialize Table
        self.table = StudentTable(self)
        self.table.pack(fill="both", expand=True, padx=20, pady=10)

        # Configure Delete Button Action
        self.delete_btn.configure(
            command=self.table.delete_selected
        )

        # Bind Search Entry KeyRelease Event
        self.search_entry.bind(
            "<KeyRelease>",
            lambda e: self.table.search(self.search_entry.get())
        )

        # Load Initial Table Data
        self.refresh_table()

    # ==========================
    # Clear Form
    # ==========================
    def clear_fields(self):
        self.id_entry.delete(0, "end")
        self.name_entry.delete(0, "end")
        self.course_entry.delete(0, "end")
        self.mobile_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.gender.set("Male")

    # ==========================
    # Fill Form (From Selected Row)
    # ==========================
    def fill_form(self, row):
        self.clear_fields()

        self.id_entry.insert(0, row[0])
        self.name_entry.insert(0, row[1])
        self.course_entry.insert(0, row[2])
        self.mobile_entry.insert(0, row[3])
        self.email_entry.insert(0, row[4])
        self.gender.set(row[5])

    # ==========================
    # Add Student
    # ==========================
    def add_student(self):
        student_id = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        course = self.course_entry.get().strip()
        mobile = self.mobile_entry.get().strip()
        email = self.email_entry.get().strip()
        gender = self.gender.get()

        if student_id == "" or name == "":
            messagebox.showerror(
                "Error",
                "Student ID and Name are required."
            )
            return

        try:
            add_student(
                student_id,
                name,
                course,
                mobile,
                email,
                gender
            )

            messagebox.showinfo(
                "Success",
                "Student Added Successfully."
            )

            self.clear_fields()
            self.refresh_table()
            self.search_entry.delete(0, "end")

        except Exception as e:
            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # ==========================
    # Refresh Table
    # ==========================
    def refresh_table(self):
        data = get_students()

        if hasattr(self.table, "update_data"):
            self.table.update_data(data)

    # ==========================
    # Update Student
    # ==========================
    def update_student_data(self):
        student_id = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        course = self.course_entry.get().strip()
        mobile = self.mobile_entry.get().strip()
        email = self.email_entry.get().strip()
        gender = self.gender.get()

        if student_id == "":
            messagebox.showwarning(
                "Warning",
                "Select a student first."
            )
            return

        try:
            update_student(
                student_id,
                name,
                course,
                mobile,
                email,
                gender
            )

            messagebox.showinfo(
                "Success",
                "Student Updated Successfully."
            )

            self.refresh_table()
            self.clear_fields()

        except Exception as e:
            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # ==========================
    # Build UI Layout
    # ==========================
    def build_ui(self):
        # Title
        title = ctk.CTkLabel(
            self,
            text="👨 Student Management",
            font=("Segoe UI", 28, "bold")
        )
        title.pack(pady=20)

        # Search Frame
        search_frame = ctk.CTkFrame(self, fg_color="transparent")
        search_frame.pack(fill="x", padx=20, pady=10)

        self.search_entry = ctk.CTkEntry(
            search_frame,
            width=300,
            placeholder_text="Search Student..."
        )
        self.search_entry.pack(side="left", padx=10)

        self.search_btn = ctk.CTkButton(
            search_frame,
            text="🔍 Search",
            width=120,
            command=lambda: self.table.search(self.search_entry.get())
        )
        self.search_btn.pack(side="left", padx=5)

        self.refresh_btn = ctk.CTkButton(
            search_frame,
            text="🔄 Refresh",
            width=120,
            command=self.refresh_table
        )
        self.refresh_btn.pack(side="left", padx=5)

        # Form Frame
        form = ctk.CTkFrame(self)
        form.pack(fill="x", padx=20, pady=10)

        # Student ID
        ctk.CTkLabel(form, text="Student ID").grid(row=0, column=0, padx=10, pady=10)
        self.id_entry = ctk.CTkEntry(form, width=220)
        self.id_entry.grid(row=0, column=1)

        # Name
        ctk.CTkLabel(form, text="Name").grid(row=1, column=0, padx=10, pady=10)
        self.name_entry = ctk.CTkEntry(form, width=220)
        self.name_entry.grid(row=1, column=1)

        # Course
        ctk.CTkLabel(form, text="Course").grid(row=2, column=0, padx=10, pady=10)
        self.course_entry = ctk.CTkEntry(form, width=220)
        self.course_entry.grid(row=2, column=1)

        # Mobile
        ctk.CTkLabel(form, text="Mobile").grid(row=0, column=2, padx=10, pady=10)
        self.mobile_entry = ctk.CTkEntry(form, width=220)
        self.mobile_entry.grid(row=0, column=3)

        # Email
        ctk.CTkLabel(form, text="Email").grid(row=1, column=2, padx=10, pady=10)
        self.email_entry = ctk.CTkEntry(form, width=220)
        self.email_entry.grid(row=1, column=3)

        # Gender
        ctk.CTkLabel(form, text="Gender").grid(row=2, column=2, padx=10, pady=10)
        self.gender = ctk.CTkComboBox(
            form,
            values=["Male", "Female", "Other"],
            width=220
        )
        self.gender.grid(row=2, column=3)
        self.gender.set("Male")

        # Action Buttons Frame
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=20)

        self.add_btn = ctk.CTkButton(
            button_frame,
            text="➕ Add Student",
            width=150,
            command=self.add_student
        )
        self.add_btn.pack(side="left", padx=10)

        self.update_btn = ctk.CTkButton(
            button_frame,
            text="✏ Update",
            width=150,
            command=self.update_student_data
        )
        self.update_btn.pack(side="left", padx=10)

        self.delete_btn = ctk.CTkButton(
            button_frame,
            text="🗑 Delete",
            width=150
        )
        self.delete_btn.pack(side="left", padx=10)

        self.clear_btn = ctk.CTkButton(
            button_frame,
            text="🧹 Clear",
            width=150,
            command=self.clear_fields
        )
        self.clear_btn.pack(side="left", padx=10)