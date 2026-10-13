
python_students = {"Arun", "Rahul", "Priya"}
data_science_students = {"Rahul", "Priya", "Anu"}
python_students.add("Vijay")
data_science_students.remove("Anu")

print("Students in both courses:", python_students & data_science_students)

print("Students only in Python:", python_students - data_science_students)

all_students = python_students | data_science_students
print("All students:", all_students)

courses = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}

for course, students in courses.items():
    print(f"Course: {course}, Students: {students}")

doubled_courses = {course: students * 2 for course, students in courses.items()}
print("Expected growth:", doubled_courses)