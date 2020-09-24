text = input()
result = ""

for ch in text:
    result += f"{ch}{ch}"

print(result)