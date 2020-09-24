stores = {}

while True:
    command = input()
    if command == "END":
        break
    token = command.split("->")
    command_text = token[0]
    store = token[1]
    if command_text == "Add":
        items = token[2].split(",")
        if store not in stores:
            stores[store] = []
        for item in items:
            if item in stores[store]:
                continue
            stores[store] += [item]
    if command_text == "Remove":
        if store not in stores:
            continue
        del stores[store]

stores = dict(sorted(stores.items(), key = lambda x: (len(x[1]), x[0]), reverse=True))

print("Stores list:")
for st, itm in stores.items():
    print(f"{st}")
    # print("".join(itm))
    for i in sorted(itm):
        print(f"<<{''.join(i)}>>")


# Test Input
# Add->PeakSports->Map,Navigation,Compass
# Add->Paragon->Sunscreen
# Add->Groceries->Dried-fruit,Nuts
# Add->Groceries->Nuts
# Add->Paragon->Tent
# Remove->Paragon
# Add->Pharmacy->Pain-killers
# END

# Test Input 2
# Add->Peak->Waterproof,Umbrella
# Add->Groceries->Water,Juice,Food
# Add->Peak->Tent
# Add->Peak->Sleeping-Bag
# Add->Peak->Jacket
# Add->Groceries->Lighter
# Remove->Groceries
# Remove->Store
# END