cb = []
ch = []
pb = []

for _ in range(int(input())):
    cb.append(input())
    ch.append(int(input()))

for _ in range(len(cb) // 2):
    pb.append(cb[ch.index(max(ch))])
    cb.remove(cb[ch.index(max(ch))])
    ch.remove(max(ch))

for x in pb:
    print(min(pb))
    pb.remove(min(pb))

for x in cb:
    print(min(cb))
    cb.remove(min(cb))
