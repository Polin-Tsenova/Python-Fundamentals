key_materials = {
    "fragments": 0,
    "shards": 0,
    "motes": 0
}


legendary_item = {
    "fragments": "Valanyr",
    "shards": "Shadowmourne",
    "motes": "Dragonwrath"
}

junks = {}
winner = ""

while winner == "":
    arg = input().lower().split()
    for i in range(0, len(arg), 2):
        quantity = int(arg[i])
        material = arg[i + 1]
        if material in key_materials:
            key_materials[material] += quantity

            if key_materials[material] >= 250:
                winner = material
                break
        else:
            if material not in junks:
                junks[material] = 0
            junks[material] += quantity

key_materials[winner] -= 250

# winner_name =""
# if winner == "fragments":
#     winner_name = "Valanyr"
# elif winner == "shards":
#     winner_name = "Shadowmourne"
# elif winner == "motes":
#     winner_name = "Dragonwrath"
#
# print(f"{winner_name} obtained")


print(f"{legendary_item[winner]} obtained!")

key_materials = dict(sorted(key_materials.items(), key =lambda el: (-el[1], el[0])))
junks = dict(sorted(junks.items(), key =lambda el: (el[0])))

for k, v in key_materials.items():
    print(f"{k}: {v}")

for k, v in junks.items():
    print(f"{k}: {v}")


#3 Motes 5 stones 5 Shards 6 leathers 255 fragments 7 Shards