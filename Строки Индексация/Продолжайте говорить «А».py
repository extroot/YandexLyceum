while True:
    inp = input()
    if inp.lower()[0] != 'а':
        break
    print(inp)


"""
Если нельзя использовать .lower()

while True:
    inp = input()
    if inp[0] != 'а' and inp[0] != 'А':
        break
    print(inp)
"""
