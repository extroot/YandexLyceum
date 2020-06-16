symb = "ABCDEFGHI"
x = int(input())

for i in range(x, 0, -1):
    for n in symb[:x]:
        print(n, i, sep="", end=" ")
    print()
