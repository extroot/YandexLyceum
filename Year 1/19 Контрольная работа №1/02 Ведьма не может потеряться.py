st = sorted([int(input()) for _ in range(int(input()))], reverse=True)
out = []
for i in range(len(st)):
    for j in range(i + 1, len(st)):
        s = st[i] + st[j]
        if s % 8 != 1:
            # print(st[i], st[j], s)
            out.append(s)
if out:
    print(f"{max(out):g}")
else:
    print(-1)

"""
elif len(st) == 1 and st[0] % 8 != 1:
    print(f"{st[0]:g}")
"""
