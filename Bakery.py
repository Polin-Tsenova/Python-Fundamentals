food = input().split()
bakery = {}

for i in range(0, len(food), 2):
    key = food[i]
    value = food[i + 1]
    bakery[key] = int(value)
print(bakery)