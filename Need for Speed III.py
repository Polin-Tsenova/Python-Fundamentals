n = int(input())
mile_dict = {}
fuel_dict = {}

for i in range(n):
    car, mileage, fuel = input().split("|")
    mile_dict[car] = int(mileage)
    fuel_dict[car] = int(fuel)

while True:
    command = input()
    if command == "Stop":
        break
    token = command.split(" : ")
    name = token[0]
    car = token[1]
    if name == "Drive":
        distance = int(token[2])
        fuel = int(token[3])
        if fuel_dict[car] - fuel > 0:
            mile_dict[car] += distance
            fuel_dict[car] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        elif fuel_dict[car] - fuel < 0:
            print("Not enough fuel to make that ride")
        if mile_dict[car] > 100000:
            print(f"Time to sell the {car}!")
            del mile_dict[car]
            del fuel_dict[car]
    if name == "Refuel":
        fuel = int(token[2])
        if fuel_dict[car] + fuel > 75:
            temp = fuel_dict[car]
            fuel_dict[car] = 75
            print(f"{car} refueled with {75 - temp} liters")
        else:
            fuel_dict[car] += fuel
            print(f"{car} refueled with {fuel} liters")
    if name == "Revert":
        kilometers = int(token[2])
        if mile_dict[car] - kilometers < 10000:
            mile_dict[car] = 10000
            continue
        mile_dict[car] -= kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")

mile_dict = dict(sorted(mile_dict.items(), key = lambda x: (-x[1], x[0])))

for k, v in mile_dict.items():
    print(f"{k} -> Mileage: {mile_dict[k]} kms, Fuel in the tank: {fuel_dict[k]} lt.")