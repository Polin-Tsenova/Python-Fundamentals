loots = input().split("|")
stolen_items = []
average_treasure_gain = 0
item_gain = 0

command = input()
while command != "Yohoho!":
    token = command.split()
    command_text = token[0]
    if command_text == "Loot":
        for i in token[1::]:
            if i not in loots:
                loots.insert(0, i)
    elif command_text == "Drop":
        index = int(token[1])
        if 0 <= index < len(loots):
            loots.append(loots.pop(index))
    elif command_text == "Steal":
        count = int(token[1])
        stolen_items = []
        if count <= len(loots):
            stolen_items = loots[-count::]
            for i in range(count):
                loots.pop()
        else:
            stolen_items = loots.copy()
            loots.clear()
        print(", ".join(stolen_items))
    command = input()

if loots:
    for item in loots:
        item_gain += len(item)
    average_treasure_gain = item_gain / len(loots)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits")
else:
    print(f"Failed treasure hunt.")