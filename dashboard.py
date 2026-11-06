import sqlite3
import csv
import os
from datetime import datetime
import cv2

def total_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]

    conn.close()
    return count


def today_attendance():
    today = datetime.now().strftime("%d-%m-%Y")
    filename = f"attendance/Attendance_{today}.csv"

    if not os.path.exists(filename):
        return 0

    with open(filename, "r") as f:
        return max(sum(1 for _ in f) - 1, 0)


def camera_status():
    cam = cv2.VideoCapture(0)

    if cam.isOpened():
        cam.release()
        return "🟢 Connected"

    return "🔴 Disconnected"