city = set()

for _ in range(int(input())):
    city.add(input())
if input() in city:
    print("TRY ANOTHER")
else:
    print("OK")
