items = input().split(', ')


while True:
    command = input()
    if command == 'Craft!':
        break
    arg = command.split(' - ')
    name = arg[0]
    if name == 'Collect':
        item = arg[1]
        if item not in items:
            items.append(item)
    elif name == "Drop":
        item = arg[1]
        if item in items:
            items.remove(item)
            # item_index = items.index(item)
            # del items[item_index]
    elif name == 'Combine Items':
        old_item, new_item = arg[1].split(":")
        if old_item in items:
            items.insert((items.index(old_item) + 1), new_item )
    elif name == 'Renew':
        item = arg[1]
        if item in items:
            items.remove(item)
            items.append(item)

print(', '. join(items))

# Iron, Wood, Sword
# Collect - Gold
# Drop - Wood
# Craft!