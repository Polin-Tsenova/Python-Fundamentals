fires_level = input().split("#")
water = int(input())

fires_level_list = []

for f in fires_level:
    fires_level_list.append(f)

#print(fires_level_list)

# for i in range(len(fires_level)):
#     fires_level_list.append(i)
#

fires_list = []

for j in range(len(fires_level_list)):
    token = fires_level_list[j]
    level = token.split(" ")
    if level[0] == "High" and (int(level[2]) >= 81 and int(level[2]) <= 125):
        fires_list.append(int(level[2]))
    elif level[0] == "Medium" and (int(level[2]) >= 51 and int(level[2]) <= 80):
        fires_list.append(int(level[2]))
    elif level[0] == "Low" and (int(level[2]) >= 1 and int(level[2]) <= 50):
        fires_list.append(int(level[2]))
#print(fires_list)

total_fire = 0
# for i in fires_list:
#     water -= i
#     if water < 0:
#
#         continue
#     else:
#         total_fire += i


print("Cells:")
for cells in fires_list:
    water -= cells
    if water < 0:
        continue
    else:
        total_fire += cells
        print(f" - {cells}")

effort = total_fire * 0.25
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
#print(water)