text = input()
encrypted_text = ""
new_char = ""

for ch in text:
    new_char = chr(ord(ch) + 3)
    encrypted_text += new_char

print(encrypted_text)

# input text
# Programming is cool!
