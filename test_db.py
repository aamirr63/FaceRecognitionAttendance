from db.db import *

add_student(
    "101",
    "Aamir",
    "Mac",
    "6395810160",
    "m.aamirr63@gmail.com",
    "male",
    100
)

print(get_students())
print("Total Students :", total_students())