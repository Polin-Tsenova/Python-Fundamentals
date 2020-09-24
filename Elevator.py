import math
people = int(input())
capacity = int(input())

elevator_courses = math.ceil(people / capacity)
print(elevator_courses)