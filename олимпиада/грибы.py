import math
n = int(input())
lst = [int(i) for i in input().split()]


def my_gcd(some_list):
    a = some_list.pop(0)
    while len(some_list) > 0:
        b = some_list.pop(0)
        a = math.gcd(a, b)
    return a


print(my_gcd(lst))
