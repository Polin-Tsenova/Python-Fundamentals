n = int(input())
students = {}

for i in range(n):
    student_name = input()
    grade = float(input())
    if student_name not in students:
        students[student_name] = []
    students[student_name] += [grade]

average_grade = dict((key, sum(value)/len(value)) for key, value in students.items())
filtered_average_grade = dict((key, value) for key, value in average_grade.items() if value >=4.50)

for k,v in sorted(filtered_average_grade.items(), key=lambda x: x[1], reverse=True):
    print(f"{k} -> {v:.2f}")

#input test
# 5
# John
# 5.5
# John
# 4.5
# Alice
# 6
# Alice
# 3
# George
# 5