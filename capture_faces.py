import cv2
import os
import sqlite3

# ---------------- DATABASE ----------------

student_id = input("Enter Student ID: ")

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT name FROM students WHERE student_id=?",
    (student_id,)
)

student = cursor.fetchone()

conn.close()

if student is None:
    print("❌ Student ID Not Found!")
    exit()

student_name = student[0]

print(f"\nStudent Found : {student_name}")

# ---------------- DATASET ----------------

path = os.path.join("dataset", f"{student_name.lower()}_{student_id}")
os.makedirs(path, exist_ok=True)

# ---------------- CAMERA ----------------

camera = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

count = 0

print("\n📷 Camera Started...")

while True:

    ret, frame = camera.read()

    if not ret:
        print("Camera Error!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:

        count += 1

        face = gray[y:y+h, x:x+w]

        cv2.imwrite(
            os.path.join(path, f"{count}.jpg"),
            face
        )

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"{student_name} ({count}/100)",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

    cv2.imshow("Capture Faces", frame)

    key = cv2.waitKey(1)

    if key == 27 or count >= 100:
        break

camera.release()
cv2.destroyAllWindows()

print(f"\n✅ {count} Images Captured Successfully!")