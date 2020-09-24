import math
biscuits_per_day = int(input())
workers = int(input())
competition = int(input())
total = 0

for i in range(30):
    if i % 3 == 0:
        total += math.floor(0.75 * biscuits_per_day * workers)
    else:
        total += biscuits_per_day * workers

print(f"You have produced {total} biscuits for the past month.")

# percentage = (total - competition/ total) * 100
if total > competition:
    percentage = ((total - competition) / competition) * 100
    print(f"You produce {percentage:.2f} percent more biscuits.")
elif total < competition:
    percentage = ((competition - total) / competition) * 100
    print(f"You produce {percentage:.2f} percent less biscuits.")