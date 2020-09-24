budget = float(input())
floor_price = float(input())

eggs_pack_price = 0.75 * floor_price
milk_liter_price = 1.25 * floor_price

cozonac_price = eggs_pack_price + floor_price + 0.25 * milk_liter_price
is_true = True
colored_eggs = 0
count_of_cozonacs = 0

while is_true:
    budget = budget - cozonac_price
    colored_eggs += 3
    count_of_cozonacs += 1
    current_count_of_cozonacs = count_of_cozonacs
    if count_of_cozonacs % 3 == 0:
        lost_eggs = current_count_of_cozonacs - 2
        colored_eggs = colored_eggs - lost_eggs
    if budget - cozonac_price <= 0:
        is_true = False
        break


print(f"You made {count_of_cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
