d = dict()
for _ in range(int(input())):
    inp = input().lower()
    s = "".join(sorted(inp))
    if s in d and inp not in d[s]:
        d[s].append(inp)
    elif s in d and inp in d[s]:
        pass
    else:
        d[s] = [inp]

print(d.items())
for _, x in sorted(d.items(), key=lambda x: sorted(x[1])):
    if len(x) > 1:
        print(*sorted(x))
