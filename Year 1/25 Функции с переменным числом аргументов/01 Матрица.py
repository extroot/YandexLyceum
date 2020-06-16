def matrix(n=1, m=None, a=0):
    m = n if not m else m
    return [[a for _ in range(m)] for _ in range(n)]
