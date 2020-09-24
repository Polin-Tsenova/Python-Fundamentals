message = input()
sum = 0

while True:
    commands = input()
    if commands == "Finish":
        break
    tokens = commands.split()
    action = tokens[0]
    if action == "Replace":
        current_char = tokens[1]
        new_char = tokens[2]
        message = message.replace(current_char, new_char)
        print(message)
    if action == "Cut":
        start = int(tokens[1])
        end = int(tokens[2])
        if not 0 < start < end+1 <= len(message):
            print("Invalid indexes!")
            continue
        substring = message[start:end+1]
        message = message.replace(substring, "", 1)
        print(message)
    if action == "Make":
        how = tokens[1]
        if how == "Upper":
            message = message.upper()
            print(message)
        if how == "Lower":
            message = message.lower()
            print(message)
    if action == "Check":
        string = tokens[1]
        if string in message:
            print(f"Message contains {string}")
        if string not in message:
            print(f"Message doesn't contain {string}")
    if action == "Sum":
        start = int(tokens[1])
        end = int(tokens[2])
        if not 0 < start < end+1 <= len(message):
            print("Invalid indexes!")
            continue
        substring = message[start:end + 1]
        for i in substring:
            sum += ord(i)
        print(sum)
        sum = 0
