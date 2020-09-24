message = input()

while True:
    commands = input()
    if commands == "Travel":
        print(f"Ready for world tour! Planned stops: {message}")
        break
    tokens = commands.split(":")
    action = tokens[0]
    if action == "Add Stop":
        index = int(tokens[1])
        txt = tokens[2]
        if not 0 < index <= len(message):
            continue
        message = message[:index] + txt + message[index:]
        print(message)
    if action == "Remove Stop":
        start = int(tokens[1])
        end = int(tokens[2])
        if 0 < start < end and end + 1 <= len(message):
            substring = message[start:end + 1]
            message = message.replace(substring, "", 1)
            print(message)
        else:
           continue
    if action == "Switch":
        old_txt = tokens[1]
        new_txt = tokens[2]
        if old_txt not in message:
            continue
        message = message.replace(old_txt, new_txt)
        print(message)