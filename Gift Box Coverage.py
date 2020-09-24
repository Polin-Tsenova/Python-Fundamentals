import math

side = float(input())
sheets = int(input())
area = float(input())

box_area = 6 * side * side


third = sheets // 3
coverage = (sheets - third) * area + third * 0.25 * area

percentage = (coverage / box_area) * 100
print(f"You can cover {percentage:.2f}% of the box.")
