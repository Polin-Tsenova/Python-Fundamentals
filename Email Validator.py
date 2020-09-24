email = input()
encription = []

while True:
    command = input()
    if command == "Complete":
        break

    tokens = command.split()
    action = tokens[0]
    if action == "Make":
        how = tokens[1]
        if how == "Upper":
            email = email.upper()
            print(email)
        if how == "Lower":
            email = email.lower()
            print(email)
    if action == "GetDomain":
        count = int(tokens[1])
        print(email[len(email)-count:])
    if action == "GetUsername":
        if '@' not in email:
            print(f"The email {email} doesn't contain the @ symbol.")
            continue
        print(email[:email.index('@')])
    if action == "Replace":
        char = tokens[1]
        email = email.replace(char, "-")
        print(email)
    if action == "Encrypt":
        for i in email:
            encription.append(ord(i))
        print(" ".join(map(str, encription)))

