courses = {}

command = input()
while command != "end":
    course_name, student_name = command.split(" : ")
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

    command = input()

courses = dict(sorted(courses.items(), key=lambda x: len(x[1]), reverse=True))

for course, student in courses.items():
    print(f"{course}: {len(student)}")
    for s in sorted(student):
        print(f"-- {''.join(s)}")

#Input text
# Algorithms : Jay Moore
# Programming Basics : Martin Taylor
# Python Fundamentals : John Anderson
# Python Fundamentals : Andrew Robinson
# Algorithms : Bob Jackson
# Python Fundamentals : Clark Lewis
# end