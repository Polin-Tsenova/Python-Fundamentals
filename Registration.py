import re

count = int(input())
pattern = r"U\$(?P<user>[A-Z][a-z]{2,})U\$P\@\$(?P<password>[A-Za-z]{5,}\d+)P\@\$"
total = 0

for i in range(count):
    registration = input()
    match = re.match(pattern, registration)
    if match is None:
        print("Invalid username or password")
        continue

    total += 1
    print("Registration was successful")
    print(f"Username: {match[1]}, Password: {match[2]}")


print(f"Successful registrations: {total}")

# Input test
# 3
# U$MichaelU$P@$asdqwe123P@$
# U$NameU$P@$PasswordP@$
# U$UserU$P@$ad2P@$
