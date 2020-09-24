tanks = input().split(",")
n = int(input())

for i in range(n):
    command = input()
    token = command.split(", ")
    instruction = token[0]
    if instruction == "Add":
        tank_name = token[1]
        if tank_name in tanks:
            print("Tank is already bought")
            continue
        print("Tank successfully bought")
        tanks.append(tank_name)
    elif instruction == "Remove":
        tank_name = token[1]
        if tank_name not in tanks:
            print("Tank not found")
            continue
        print("Tank successfully sold")
        tanks.remove(tank_name)
    elif instruction == "Remove At":
        idx = int(token[1])
        if not 0 <= idx <= len(tanks):
            print("Index out of range")
            continue
        print("Tank successfully sold")
        tanks.pop(idx)
    elif instruction == "Insert":
        idx = int(token[1])
        tank_name = token[2]
        if 0 <= idx <= len(tanks):
            if tank_name in tanks:
                print("Tank is already bought")
            else:
                print("Tank successfully bought")
                tanks.insert(idx, tank_name)
        else:
            print("Index out of range")

print(", ".join(tanks))