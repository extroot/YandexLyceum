import sys
data = list(map(lambda x: (x.rstrip('\n'), sum([ord(c) - ord('A') + 1
                                                for c in x.upper().rstrip('\n')])), sys.stdin))
print("\n".join(map(lambda x: x[0], sorted(data, key=lambda x: (x[1], x[0])))))
