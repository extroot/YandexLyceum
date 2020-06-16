commands = {"make_negative": lambda x: x * -1 if x > 0 else x,
            "square": lambda x: x ** 2,
            "strange_command": lambda x: x + 1 if x % 5 == 0 else x}

data = [int(x) for x in input().split()]
for _ in range(int(input())):
    data = list(map(commands[input()], data))
print(*data)


example = ...
example.name = ...
print(example.get().name)
print(example.name)