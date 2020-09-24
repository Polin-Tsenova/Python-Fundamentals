target = list(map(int, input().split("|")))
points = 0

command = input()

while command != "Game over":
    token = command.split("@")
    text = token[0]
    index = int(token[1])
    shoot_length = int(token[2])
    if text == "Shoot Left":
        result = len(target) - ((index + shoot_length) % len(target))
        if 0 <= index < len(target):
            if target[result] < 5:
                points += target[result]
                target[result] = 0
            else:
                points += 5
                target[result] -= 5
        else:
            break
    elif text == "Shoot Right":
        result = (index + shoot_length) % len(target)
        if not 0 <= index < len(target):
            continue
        if target[result] < 5:
            points += target[result]
            target[result] = 0
        else:
            points += 5
            target[result] -= 5
    elif text == "Reverse":
        target.reverse()

    command = input()

new_targets = list(map(str, target))
print(f'{" - ".join(new_targets)}')
print(f"Iskren finished the archery tournament with {points} points!")