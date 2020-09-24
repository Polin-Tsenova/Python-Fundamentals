health_dict = {}
energy_dict = {}

while True:
    commands = input()
    if commands == "Results":
        break

    tokens = commands.split(":")
    action = tokens[0]
    if action == "Add":
        person = tokens[1]
        health = int(tokens[2])
        energy = int(tokens[3])
        if person in health_dict and person in energy_dict:
            health_dict[person] += health
            continue
        health_dict[person] = health
        energy_dict[person] = energy
    if action == "Attack":
        attacker = tokens[1]
        defender = tokens[2]
        demade = int(tokens[3])
        if attacker in health_dict and attacker in energy_dict and \
            defender in health_dict and defender in energy_dict:
            health_dict[defender] -= demade
            if health_dict[defender] <= 0:
                print(f"{defender} was disqualified!")
                del health_dict[defender]
                del energy_dict[defender]
            energy_dict[attacker] -= 1
            if energy_dict[attacker] == 0:
                print(f"{attacker} was disqualified!")
                del health_dict[attacker]
                del energy_dict[attacker]
    if action == "Delete":
        user = tokens[1]
        if user == "All":
            health_dict.clear()
            energy_dict.clear()
            continue
        if user not in health_dict and user not in energy_dict:
            continue
        del energy_dict[user]
        del health_dict[user]

health_dict = dict(sorted(health_dict.items(), key= lambda x: (-x[1], x[0])))

print(f"People count: {len(energy_dict)}")
for k,v in health_dict.items():
    print(f"{k} - {health_dict[k]} - {energy_dict[k]}")


