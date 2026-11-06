from dashboard import total_students, today_attendance, camera_status
import customtkinter as ctk
from tkinter import messagebox
import subprocess
import os
from datetime import datetime 
from PIL import Image, ImageTk
import recognize_faces
from pages.students import StudentPage
# ---------------- Appearance ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
PRIMARY = "#3B82F6"
SUCCESS = "#10B981"
WARNING = "#F59E0B"
DANGER = "#EF4444"

BG = "transparent"
CARD = "#1E293B"
SIDEBAR = "#111827"

# ---------------- Window ----------------
app = ctk.CTk()
app.title("Face Recognition Attendance System")
app.geometry("1450x850")
app.minsize(1300, 800)
# ===========================
# Background Image
# ===========================

bg_image = ctk.CTkImage(
    light_image=Image.open("image/background.png"),
    dark_image=Image.open("image/background.png"),
    size=(1400, 800)
)

bg_label = ctk.CTkLabel(
    app,
    image=bg_image,
    text=""
)

bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.lower()

# ---------------- Functions ----------------

def capture_faces():
    subprocess.run(["python", "capture_faces.py"])

def train_model():
    subprocess.run(["python", "train_model.py"])
    messagebox.showinfo("Success", "Model Trained Successfully!")



def start_attendance():
    global attendance_running

    if attendance_running:
        return

    attendance_running = True

    status_label.configure(
        text="🟢 Attendance Running",
        text_color="green"
    )

    subprocess.Popen(["python", "recognize_faces.py"])

def open_attendance():
    folder = "attendance"
    if os.path.exists(folder):
        os.startfile(folder)
    else:
        messagebox.showwarning("Warning", "Attendance folder not found!")

def students():
    messagebox.showinfo("Students", "Student Management Coming Soon")

def dashboard():
    messagebox.showinfo("Dashboard", "Dashboard Coming Soon")

def settings():
    messagebox.showinfo("Settings", "Settings Coming Soon")

def exit_app():
    app.destroy()

# ---------------- Sidebar ----------------

sidebar = ctk.CTkFrame(
    app,
    width=260,
    fg_color=SIDEBAR,
    corner_radius=0
)
sidebar.pack(side="left", fill="y")

title = ctk.CTkLabel(
    sidebar,
    text="🎓 FRAS",
    font=("Segoe UI", 32, "bold"),
    text_color="white"
)

title.pack(pady=30)

buttons = [
("👤 Register Student", students),
("📷 Capture Faces", capture_faces),
("🧠 Train Model", train_model),
("✅ Start Attendance", start_attendance),
("📄 Attendance", open_attendance),
("📊 Dashboard", dashboard),
("⚙ Settings", settings),
("❌ Exit", exit_app)
]

for text,cmd in buttons:

    btn = ctk.CTkButton(
    sidebar,
    text=text,
    command=cmd,
    width=220,
    height=48,
    corner_radius=12,
    fg_color="#1F2937",
    hover_color=PRIMARY,
    font=("Segoe UI", 15, "bold")
)
    

    btn.pack(pady=8)

# ---------------- Main Area ----------------
main = ctk.CTkFrame(
    app,
    fg_color="transparent"
)


topbar = ctk.CTkFrame(main, height=70, fg_color="#111827")
topbar.pack(fill="x", padx=15, pady=15)
student_page = StudentPage(main)
student_page.pack(fill="both", expand=True)

ctk.CTkLabel(
    topbar,
    text="Face Recognition Attendance System",
    font=("Segoe UI", 24, "bold")
).pack(side="left", padx=20)

ctk.CTkEntry(
    topbar,
    placeholder_text="Search Student...",
    width=250
).pack(side="right", padx=15)

ctk.CTkButton(
    topbar,
    text="🔔",
    width=40
).pack(side="right")
main.pack(fill="both", expand=True)

heading = ctk.CTkLabel(
    main,
    text="FACE RECOGNITION ATTENDANCE SYSTEM",
    font=("Arial",28,"bold")
)

heading.pack(pady=20)

# ---------------- Date & Time ----------------

time_label = ctk.CTkLabel(main,font=("Arial",18))
time_label.pack()

def update_time():

    now = datetime.now()

    current = now.strftime("%d-%m-%Y   %I:%M:%S %p")

    time_label.configure(text=current)

    app.after(1000,update_time)

update_time()

# ---------------- Dashboard Cards ----------------

card_frame = ctk.CTkFrame(main)
card_frame.pack(pady=30)

card1 = ctk.CTkFrame(card_frame,width=220,height=120)
card1.grid(row=0,column=0,padx=20)

ctk.CTkLabel(card1,text="👨‍🎓 Total Students",font=("Arial",18,"bold")).pack(pady=10)
ctk.CTkLabel(card1,text="1",font=("Arial",35)).pack()
ctk.CTkLabel
    

card2 = ctk.CTkFrame(card_frame,width=220,height=120)
card2.grid(row=0,column=1,padx=20)

ctk.CTkLabel(card2,text="✅ Attendance Today",font=("Arial",18,"bold")).pack(pady=10)
ctk.CTkLabel(card2,text="0",font=("Arial",35)).pack()
ctk.CTkLabel

card3 = ctk.CTkFrame(card_frame,width=220,height=120)
card3.grid(row=0,column=2,padx=20)
ctk.CTkLabel(
    card3,
    text="📷 Camera Status",
    font=("Segoe UI",18,"bold")
).pack(pady=10)

camera_label = ctk.CTkLabel(
    card3,
    text=camera_status(),
    font=("Segoe UI",25,"bold"),
    text_color="green"
)
camera_label.pack()

camera_frame = ctk.CTkFrame(
    main,
    width=850,
    height=350,
    fg_color=CARD,
    corner_radius=15
)
camera_label = ctk.CTkLabel(
    camera_frame,
    text=""
)

camera_label.pack(fill="both", expand=True)
camera_frame.pack(pady=20)

camera_frame.pack_propagate(False)

ctk.CTkLabel(
    camera_frame,
    text="📷 LIVE CAMERA PREVIEW",
    font=("Segoe UI",20,"bold")
).pack(pady=20)
attendance_btn = ctk.CTkButton(
    sidebar,
    text="📷 Start Attendance",
    width=220,
    height=45,
    corner_radius=12,
    fg_color="#2563EB",
    hover_color="#1D4ED8",
    font=("Segoe UI", 15, "bold")
)
attendance_btn.pack(pady=8)
status_label = ctk.CTkLabel(
    topbar,
    text="🔴 Attendance Stopped",
    font=("Segoe UI", 15, "bold"),
    text_color="red"
)
status_label.pack(side="right", padx=15)
# ===============================
# Bottom Section
# ===============================

bottom_frame = ctk.CTkFrame(
    main,
    fg_color="transparent"
)
bottom_frame.pack(fill="both", expand=True, padx=20, pady=15)
attendance_frame = ctk.CTkFrame(
    bottom_frame,
    fg_color="#1E293B",
    corner_radius=15
)

attendance_frame.pack(side="left", fill="both", expand=True, padx=(0,10))

title = ctk.CTkLabel(
    attendance_frame,
    text="📋 Attendance Today",
    font=("Segoe UI",18,"bold")
)

title.pack(pady=10)
header = ctk.CTkFrame(attendance_frame, fg_color="#334155")
header.pack(fill="x", padx=10)

ctk.CTkLabel(header,text="Name",width=120).pack(side="left")
ctk.CTkLabel(header,text="Time",width=100).pack(side="left")
ctk.CTkLabel(header,text="Status",width=100).pack(side="left")
attendance_rows=[]

attendance_rows = []

attendance_rows = []

def refresh_table():
    global attendance_rows

    for widget in attendance_rows:
        widget.destroy()

    attendance_rows = []

    data = load_attendance()

    for row in data:
        frame = ctk.CTkFrame(attendance_frame, fg_color="transparent")
        frame.pack(fill="x", padx=10, pady=2)

        attendance_rows.append(frame)

        ctk.CTkLabel(frame, text=row[0], width=120).pack(side="left")
        ctk.CTkLabel(frame, text=row[3], width=100).pack(side="left")
        ctk.CTkLabel(frame, text="Present", width=100).pack(side="left")

    app.after(2000, refresh_table)

# ===== Function yahin khatam =====

notification_frame = ctk.CTkFrame(
    bottom_frame,
    width=320,
    fg_color="#1E293B",
    corner_radius=15
)

notification_frame.pack(side="right", fill="y")
notification_frame.pack_propagate(False)

ctk.CTkLabel(
    notification_frame,
    text="🔔 Notifications",
    font=("Segoe UI", 18, "bold")
).pack(pady=10)

#Notification 
notifications = [
    "✔ Camera Connected",
    "✔ Student Registered",
    "✔ Model Trained",
    "✔ Attendance Saved",
]

for msg in notifications:

    ctk.CTkLabel(
        notification_frame,
        text=msg,
        anchor="w",
        font=("Segoe UI",14)
    ).pack(fill="x", padx=15, pady=5)

# ---------------- Bottom ----------------

bottom = ctk.CTkFrame(main,height=60)
bottom.pack(side="bottom",fill="x")

ctk.CTkLabel(
    bottom,
    text="Developed by Chahat Mishra | Face Recognition Attendance System",
    font=("Arial",15)
).pack(pady=15)
attendance_rows = []
app.mainloop()
import csv
import os
from datetime import datetime

def load_attendance():

    today = datetime.now().strftime("%d-%m-%Y")

    filename = f"attendance/Attendance_{today}.csv"

    if not os.path.exists(filename):
        return []

    data=[]

    with open(filename,"r") as file:

        reader=csv.reader(file)

        next(reader,None)

        for row in reader:
            data.append(row)

    return data