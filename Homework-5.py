frontend = {"Arun", "Rahul", "Priya"}
backend = {"Rahul", "Vijay", "Anu"}
backend.add("Kiran")
frontend.remove("Arun")

print("Students in both courses:", frontend & backend)

print("Students only in Backend:", backend - frontend)

all_students = frontend | backend
print("Total unique students:", len(all_students))

courses = {
    "Frontend": len(frontend),
    "Backend": len(backend)
}

for course, students in courses.items():
    print(f"Course: {course}, Students: {students}")

new_courses = {
    course: students for course, students in courses.items()
}
new_courses["Fullstack"] = sum(courses.values())

print("Updated courses:", new_courses)