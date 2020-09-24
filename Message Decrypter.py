import re

n = int(input())

pattern = r"^([$%])([A-Z][a-z]{2,})\1:\s(\[[0-9]{1,}\]\|\[[0-9]{1,}\]\|\[[0-9]{1,}\]\|)$"
decrypted = ''

number = r"\d+"

for i in range(n):
    message = input()

    match = re.fullmatch(pattern, message)

    if match is None:
        print("Valid message not found!")
        continue

    regex = re.findall(number, match[3])

    for i in regex:
        decrypted += chr(int(i))

    print(f"{match[2]}: {decrypted}")

    decrypted = ''

