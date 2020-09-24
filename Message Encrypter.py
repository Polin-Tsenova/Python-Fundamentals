import re
n = int(input())

pattern = r"(\*|\@)([A-Z][a-z]{2,})\1:\s((\[[A-Za-z]\]\|){3})$"
encrypt = []

for i in range(n):
    message = input()

    match = re.search(pattern,message)

    if match is None:
        print("Valid message not found!")
        continue

    for elem in match[3]:
        if elem.isalpha():
            encrypt.append(str(ord(elem)))

    print(f"{match[2]}: {' '.join(encrypt)}")

    encrypt.clear()
