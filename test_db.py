from db.db import *

add_student(
    "101",
    "Chahat",
    "BCA",
    "9876543210",
    "chahat@gmail.com",
    "male",
    100
)

print(get_students())
print("Total Students :", total_students())