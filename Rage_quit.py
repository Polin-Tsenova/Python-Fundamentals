string = input()
result = ""
current_string = ""

for i in range(len(string)):
    if string[i].isdigit():
        num = string[i]
        counter = i + 1
        while counter < len(string) and string[counter].isdigit():
            num += string[counter]
            counter += 1
        result += current_string.upper() * int(num)
        current_string = ""
    else:
        current_string += string[i]

print(f"Unique symbols used: {len(set(result))}")
print(result)

# input text
# aSd2&5s@1