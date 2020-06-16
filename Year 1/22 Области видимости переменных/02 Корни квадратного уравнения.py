def larger_root(b, c):
    return max(root(b, c))


def smaller_root(b, c):
    return min(root(b, c))


def discriminant(a, b, c):
    return b ** 2 - (4 * a * c)


def root(b, c):
    d = discriminant(1, b, c)
    return (-b + d ** 0.5) / 2, (-b - d ** 0.5) / 2


def main():
    b, c = float(input()), float(input())
    print(discriminant(1, b, c))
    print(*sorted(root(b, c)))
