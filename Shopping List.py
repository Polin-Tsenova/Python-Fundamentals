groceries = input().split('!')
# print(groceries)

while True:
    command = input()
    if command == 'Go Shopping!':
        break
    token = command.split()
    type = token[0]
    if type == "Urgent":
        item = token[1]
        if item in groceries:
            continue
        groceries.insert(0, item)
    elif type == "Unnecessary":
        item = token[1]
        if item not in groceries:
            continue
        # del groceries[groceries.index(item)]
        groceries.remove(item)
    elif type == "Correct":
        old_item = token[1]
        new_item = token[2]
        if old_item not in groceries:
            continue
        old_item_index = groceries.index(old_item)
        groceries[old_item_index] = new_item
    elif type == "Rearrange":
        item = token[1]
        if item in groceries:
            # del groceries[groceries.index(item)]
            groceries.remove(item)
            groceries.append(item)


print(', '.join(groceries))

# Milk!Pepper!Salt!Water!Banana!Grapes
# Urgent Salt
# Unnecessary Grapes
# Correct Pepper Onion
# Rearrange Grapes
# Correct Tomatoes Potatoes
# Go Shopping!