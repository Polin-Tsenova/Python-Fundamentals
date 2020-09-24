email_string = input()
commands= {}

while True:
    command = input().split()
    instruction = command[0]
    if instruction == "Complete":
        break
    if instruction == "Make":
        action = command[1]
        if action == "Upper":
            email_string = email_string.upper()
        elif action == "Lower":
            email_string = email_string.lower()
        print(email_string)
    if instruction == "GetDomain":
        count = int(command[1])
        print(email_string[len(email_string) - count:])
    if instruction == "GetUsername":
        if "@" not in email_string:
            print(f"The email {email_string} doesn't contain the @ symbol.")
            continue
        user = ""
        for letter in email_string:
            if letter == "@":
                break
            user += letter
        print(user)
    if instruction == "Replace":
        char = command[1]
        email_string = email_string.replace(char, "-")
        print(email_string)
    if instruction == "Encrypt":
        for i in email_string:
            print(ord(i), end = " ")

# Input Text
# Mike123@somemail.com
# Make Upper
# GetDomain 3
# GetUsername
# Encrypt
# Complete


