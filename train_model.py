import cv2
import os
import json
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()

dataset_path = "dataset"

faces = []
ids = []

label_map = {}
current_id = 0

for person in sorted(os.listdir(dataset_path)):

    person_path = os.path.join(dataset_path, person)

    if not os.path.isdir(person_path):
        continue

    label_map[current_id] = person

    for image_name in os.listdir(person_path):

        image_path = os.path.join(person_path, image_name)

        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if image is None:
            continue

        faces.append(image)
        ids.append(current_id)

    current_id += 1

print("Total Faces :", len(faces))
print("Total Persons :", len(label_map))

if len(faces) == 0:
    print("No training images found!")
    exit()

recognizer.train(faces, np.array(ids))
recognizer.save("trainer/trainer.yml")
print("Label Map:", label_map)


with open("trainer/labels.json", "w", encoding="utf-8") as f:
    json.dump(label_map, f, indent=4)

print("Saved Successfully!")

with open("trainer/labels.json", "r", encoding="utf-8") as f:
    print("File Content:")
    print(f.read())
    
print("Training Completed Successfully!")
print("Faces Found:", len(faces))