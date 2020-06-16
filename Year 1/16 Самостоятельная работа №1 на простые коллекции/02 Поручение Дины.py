numbers = []
inp = input().split()
k, m = int(inp[0]), int(inp[1])
for num in input().split():
    num = int(num)
    if num % k != m and num not in numbers:
        numbers.append(num)
print(*numbers)
