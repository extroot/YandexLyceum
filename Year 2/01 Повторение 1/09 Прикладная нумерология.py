hours = sorted([str(x).rjust(2, '0') for x in input().split()], key=lambda x: int(x))
minutes = sorted([str(x).rjust(2, '0') for x in input().split()], key=lambda x: int(x))


for i in hours:
    for j in minutes:
        if sum([int(x) for x in i]) != sum([int(x) for x in j]):
            print(f"{i}:{j}")
