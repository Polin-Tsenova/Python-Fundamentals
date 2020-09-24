n = int(input())
word = input()

sentances = []
filtered = []
for i in range(n):
    current_sentence = input()
    sentances.append(current_sentence)
    if word in current_sentence:
        filtered. append(current_sentence)

print(sentances)
print(filtered)
