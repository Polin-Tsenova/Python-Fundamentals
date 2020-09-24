text = input()

for i in range(len(text)):
    if text[i] == ":":
        if i + 1 >= len(text):
            continue
        if text[i + 1] != " ":
            print(f":{text[i + 1]}")


# input text
# There are so many emoticons nowadays :P. I have many ideas :O what input to place here :)