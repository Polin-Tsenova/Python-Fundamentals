neighborhood = list(map(int, input().split('@')))
start_index = 0
last_position = 0
house_count = 0

while True:
    command = input()
    if command == "Love!":
        print(f"Cupid's last position was {last_position}.")
        break
    else:
        jump_length = int(command.split()[1])

        r = start_index + jump_length
        if r > len(neighborhood):
            start_index = 0
            r = 0
        result = r % len(neighborhood)
        if neighborhood[result] == 0:
            print(f"Place {result} already had Valentine's day.")
        else:
            neighborhood[result] -= 2
            if neighborhood[result] == 0:
                print(f"Place {result} has Valentine's day.")
    last_position = result
    start_index = last_position


for i in range(len(neighborhood)):
    if neighborhood[i] == 0:
        continue
    house_count += 1

if house_count == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {house_count} places.")


# Test Input
# 2@4@2
# Jump 2
# Jump 2
# Jump 8
# Jump 3
# Jump 1
# Love!
