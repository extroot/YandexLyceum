st = [0, 0, 1]


def tribonacci(n):
    st.append(sum(st[-3:]))
    if n < len(st):
        return st[n]
    return tribonacci(n)
