likes = {}
unlikes = {}
count = 0

while True:
    commands = input()
    if commands == "Stop":
        break
    tokens = commands.split("-")
    action = tokens[0]
    guest = tokens[1]
    meal = tokens[2]
    if action == "Like":
        if guest not in likes and guest not in unlikes:
            likes[guest] = []
            unlikes[guest] = []
        if meal in likes[guest] or meal in unlikes[guest]:
            continue
        likes[guest] += [meal]
    if action == "Unlike":
        if guest not in likes and guest not in unlikes:
            print(f"{guest} is not at the party.")
            continue
        if meal not in likes[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
            continue
        print(f"{guest} doesn't like the {meal}.")
        likes[guest].remove(meal)
        count += 1


likes = dict(sorted(likes.items(), key=lambda x: (-len(x[1]),x[0])))

for k, v in likes.items():
    print(f"{k}: {', '.join(v)}")

print(f"Unliked meals: {count}")
