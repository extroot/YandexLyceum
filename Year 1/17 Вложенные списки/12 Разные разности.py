st = [int(input()) for _ in range(int(input()))]
out = []
for i in range(len(st)):
    for j in range(len(st)):
        out.append(st[i] - st[j])
for x in sorted(set(out)):
    print(x)
