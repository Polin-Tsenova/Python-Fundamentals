import re

string = input()

pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"

match = re.findall(pattern, string)

destinations = []
travel_points = 0

for element in match:
    destinations.append(element[1])

for dest in destinations:
    travel_points += len(dest)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
