quantity_bought = int(input())
days = int(input())

cost = 0
christmas_spirit = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity_bought += 2
    if day % 2 == 0:
        cost += 2 * quantity_bought
        christmas_spirit += 5
    if day % 3 == 0:
        cost += 8 * quantity_bought
        christmas_spirit += 13
    if day % 5 == 0:
        cost += 15 * quantity_bought
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        cost += 23
        christmas_spirit -= 20
        if day == days:
            christmas_spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {christmas_spirit}")
