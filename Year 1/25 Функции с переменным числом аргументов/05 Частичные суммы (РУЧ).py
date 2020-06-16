def partial_sums(*args):
    out = [0]
    for x in args:
        out.append(out[-1] + x)
    return out
