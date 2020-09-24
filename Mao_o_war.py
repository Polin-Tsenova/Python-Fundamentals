pirateship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
max_health_capacity = int(input())
count = 0
game_over = False

line = input()
while line != "Retire" and game_over != True:
    token = line.split()
    command = token[0]
    if command == "Fire":
        index = int(token[1])
        demage = int(token[2])
        if 0 <= index < len(warship):
            warship[index] -= demage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                game_over = True
                break
    elif command == "Defend":
        start_index = int(token[1])
        end_index = int(token[2])
        demage = int(token[3])
        if 0 <= start_index < len(pirateship) and 0 <= end_index < len(pirateship):
            for i in range(start_index, end_index + 1):
                pirateship[i] -= demage
                if pirateship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    game_over = True
                    break
    elif command == "Repair":
        index = int(token[1])
        health = int(token[2])
        if 0 <= index < len(pirateship):
            pirateship[index] += health
            if pirateship[index] > max_health_capacity:
                pirateship[index] = max_health_capacity
    elif command == "Status":
        for n in pirateship:
            if n < 0.2 * max_health_capacity:
                count += 1
        print(f"{count} sections need repair.")
    line = input()


if not game_over:
    print(f"Pirate ship status: {sum(pirateship)}")
    print(f"Warship status: {sum(warship)}")
