forcebook = {}

command = input()
while command != "Lumpawaroo":
    side = ""
    user = ""

    if "|" in command:
        token = command.split(" | ")
        side = token[0]
        user = token[1]
        if side not in forcebook:
            forcebook[side] = []
        if user in forcebook:
            continue
        forcebook[side] += [user]

    elif "->" in command:
        token = command.split(" -> ")
        user = token[0]
        side = token[1]

        side_of_user = ""
        for k, v in forcebook.items():
            if user in v:
                side_of_user = k
                break
        if side_of_user != "":
            forcebook[side_of_user].remove(user)

        if side not in forcebook:
            forcebook[side] = []
        # if user in forcebook.values():
        #     forcebook[side].remove(user)
        forcebook[side] += [user]
        print(f"{user} joins the {side} side!")

    command = input()

forcebook = dict(sorted(forcebook.items(), key=lambda x: (-len(x[1]), x[0])))
for s, u in forcebook.items():
    if len(u) == 0:
        continue

    print(f"Side: {s}, Members: {(len(u))}")

    for i in sorted(u):
        print(f"! {i}")



# input text
# Lighter | Royal
# Darker | DCay
# Ivan Ivanov -> Lighter
# DCay -> Lighter
# Lumpawaroo