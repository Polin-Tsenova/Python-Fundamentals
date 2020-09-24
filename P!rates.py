targets_pop = {}
targets_gold = {}

while True:
    command = input()
    if command == "Sail":
        break
    token = command.split('||')
    city = token[0]
    population = int(token[1])
    gold = int(token[2])
    if city in targets_pop and targets_gold:
        targets_pop[city] += population
        targets_gold[city] += gold
        continue
    targets_pop[city] = population
    targets_gold[city] = gold


while True:
    command = input()
    if command == "End":
        break
    events = command.split("=>")
    name = events[0]
    city = events[1]
    if name == "Plunder":
        people = int(events[2])
        gold = int(events[3])
        targets_pop[city] -= people
        targets_gold[city] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        if targets_pop[city] <= 0 or targets_gold[city] <= 0:
            del targets_pop[city]
            del targets_gold[city]
            print(f"{city} has been wiped off the map!")

    if name == "Prosper":
        gold = int(events[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            continue
        targets_gold[city] += gold
        print(f"{gold} gold added to the city treasury. {city} now has {targets_gold[city]} gold.")


targets_gold = dict(sorted(targets_gold.items(), key=lambda x: (-x[1],x[0])))
# targets_pop = dict(sorted(targets_pop.items(), key=lambda x: x[1]))

print(f"Ahoy, Captain! There are {len(targets_pop)} wealthy settlements to go to:")
for k, v in targets_gold.items():
    print(f"{k} -> Population: {targets_pop[k]} citizens, Gold: {targets_gold[k]} kg")

