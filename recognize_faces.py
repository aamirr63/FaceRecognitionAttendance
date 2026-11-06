import csv
import os
from datetime import datetime
import cv2
import json

# Load trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/trainer.yml")

# Load labels
with open("trainer/labels.json", "r") as f:
    labels = json.load(f)

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
def mark_attendance(name):
    today = datetime.now().strftime("%d-%m-%Y")
    current_time = datetime.now().strftime("%H:%M:%S")

    filename = f"attendance/Attendance_{today}.csv"

    # Attendance folder create
    os.makedirs("attendance", exist_ok=True)

    already_marked = False

    if os.path.exists(filename):
     with open(filename, "r", newline="") as f:
        reader = csv.reader(f)

        student_name = name.split("_")[0]

        for row in reader:
            if len(row) > 0 and row[0] == student_name:
                already_marked = True
                break

    if not already_marked:

        student = name.split("_")

        student_name = student[0]
        student_id = student[1]

        with open(filename, "a", newline="") as f:

            writer = csv.writer(f)

            if f.tell() == 0:
                writer.writerow(["Name", "ID", "Date", "Time"])

            writer.writerow([
                student_name,
                student_id,
                today,
                current_time
            ])

        print(f"{student_name} Attendance Marked")
marked_names = set()
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(100, 100)
    )

    for (x, y, w, h) in faces:

        face = gray[y:y+h, x:x+w]

        label, confidence = recognizer.predict(face)

        if confidence < 70:

            name = labels.get(str(label), "Unknown")

            if name not in marked_names:
                mark_attendance(name)
                marked_names.add(name)

            color = (0, 255, 0)
            text = f"{name} ({confidence:.1f})"

        else:
            color = (0, 0, 255)
            text = "Unknown"

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

        cv2.putText(
            frame,
            text,
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2
        )

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) == 27:   # ESC
        break

camera.release()
cv2.destroyAllWindows()
def start_recognition(label):
    

    camera = cv2.VideoCapture(0)

    def update():

        ret, frame = camera.read()

        if ret:

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Face detection
            faces = face_cascade.detectMultiScale(
                gray,
                1.2,
                5
            )

            # Yahan tumhara pura recognition code rahega

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            img = Image.fromarray(rgb)

            imgtk = ImageTk.PhotoImage(img)

            label.imgtk = imgtk

            label.configure(image=imgtk)

        label.after(10, update)

    update()