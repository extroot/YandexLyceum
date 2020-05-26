inp = int(input())
br = [int(input()) for i in range(inp)] * 2
for _ in range(int(input())):
    br[(int(input()) - 1) * inp + int(input())] += int(input())
print(*br[:inp])
print(*br[inp:])
s = 0
for i in range(len(br) // 2):
    if br[i] == br[inp + i]:
        s += 1
print(s)
