n = int(input())
registered_cars = {}

for i in range(n):
    line = input().split(" ")
    command = line[0]
    username = line[1]
    if command == "register":
        license_plate_num = line[2]
        if username not in registered_cars:
            registered_cars[username] = ""
        if license_plate_num in registered_cars.values():
            print(f"ERROR: already registered with plate number {license_plate_num}")
            continue
        registered_cars[username] += license_plate_num
        print(f"{username} registered {registered_cars[username]} successfully")
    elif command == "unregister":
        if username not in registered_cars:
            print(f"ERROR: user {username} not found")
        else:
            del registered_cars[username]
            print(f"{username} unregistered successfully ")


for u, l in registered_cars.items():
    print(f"{u} => {l}")
