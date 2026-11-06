import customtkinter as ctk
from tkinter import ttk, messagebox
from PIL import Image

from db.db import get_students, delete_student


class StudentTable(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.build_table()
        self.load_data()

    def build_table(self):

        # Treeview Style
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Treeview",
            background="#1E293B",
            foreground="white",
            fieldbackground="#1E293B",
            rowheight=35,
            font=("Segoe UI", 11)
        )

        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 12, "bold")
        )

        style.map(
            "Treeview",
            background=[("selected", "#2563EB")]
        )

        columns = (
            "Student ID",
            "Name",
            "Course",
            "Mobile",
            "Email",
            "Gender",
            "Images"
        )

        self.tree = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=15
        )

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=140, anchor="center")

        scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def on_double_click(self, event):

         row = self.get_selected()

         if row:

          self.parent.fill_form(row)
    def load_data(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        students = get_students()

        for student in students:

            self.tree.insert(
                "",
                "end",
                values=(
                    student[1],
                    student[2],
                    student[3],
                    student[4],
                    student[5],
                    student[6],
                    student[7]
                )
            )

    def refresh(self):
        self.load_data()

    def get_selected(self):

        selected = self.tree.focus()

        if not selected:
            return None

        return self.tree.item(selected)["values"]

    def on_double_click(self, event):

        row = self.get_selected()

        if row:
            print("Selected :", row)

    def search(self, text):

        for row in self.tree.get_children():
            self.tree.delete(row)

        students = get_students()

        text = text.lower()

        for student in students:

            if (
                text in str(student[1]).lower()
                or text in student[2].lower()
                or text in student[3].lower()
            ):

                self.tree.insert(
                    "",
                    "end",
                    values=(
                        student[1],
                        student[2],
                        student[3],
                        student[4],
                        student[5],
                        student[6],
                        student[7]
                    )
                )

    def update_data(self, data):

        for row in self.tree.get_children():
            self.tree.delete(row)

        for student in data:

            self.tree.insert(
                "",
                "end",
                values=(
                    student[1],
                    student[2],
                    student[3],
                    student[4],
                    student[5],
                    student[6],
                    student[7]
                )
            )

    def delete_selected(self):

        row = self.get_selected()

        if row is None:
            messagebox.showwarning(
                "Warning",
                "Select Student First"
            )
            return

        confirm = messagebox.askyesno(
            "Delete",
            "Delete Selected Student?"
        )

        if confirm:

            delete_student(row[0])

            self.refresh()

            messagebox.showinfo(
                "Success",
                "Student Deleted Successfully"
            )