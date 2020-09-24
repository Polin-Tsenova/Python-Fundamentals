array = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        print(", ".join(map(str,array)))
        break
    arg = command.split()
    name = arg[0]
    if name == 'swap':
        index1 = int(arg[1])
        index2 = int(arg[2])
        array[index1], array[index2] = array[index2], array[index1]
    if name == 'multiply':
        index1 = int(arg[1])
        index2 = int(arg[2])
        array[index1] = array[index1] * array[index2]
    if name == 'decrease':
        for i in range(len(array)):
            array[i] -= 1
