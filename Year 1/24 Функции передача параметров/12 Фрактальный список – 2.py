def defractalize(fractal):
    for x in fractal:
        if not str(x).isdigit():
            del(fractal[fractal.index(x)])
