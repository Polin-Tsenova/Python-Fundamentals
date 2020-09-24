fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_repairs = 0
sword_repairs = 0
shield_repairs = 0
armor_repairs = 0


for i in range(1,fights_count + 1):
    if i % 2 == 0:
        helmet_repairs += 1
    if i % 3 == 0:
        sword_repairs += 1
        if i % 2 == 0:
            shield_repairs += 1
            if shield_repairs % 2 == 0:
                armor_repairs += 1
expenses = helmet_repairs * helmet_price + sword_repairs * sword_price \
           + shield_repairs * shield_price + armor_repairs * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")





